from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools.function_tool import FunctionTool
from terraform_dev.main import *
from add_dev.main import *
from google.genai import types
from .utils.prompts import ADD_INSTRUCTION_PROMPT, VALIDATION_PROMPT, INPUT_PROMPT, TERRAFORM_INSTRUCTION_PROMPT, REVIEW_TERRAFORM_INSTRUCTION_PROMPT, PR_RAISE_PROMPT
class AddModel(BaseModel):
    application_name: str
    technical_architecture: Optional[dict[str, Technical_Architecture]] = None
    devops_and_operations: Optional[dict[str, Development_and_Operations]] = None
    risks_and_assumptions: Optional[dict[str, Risks_Assumptions_and_Decisions]] = None
    appendix: Optional[dict[str, Appendix]] = None


def read_csv_file(file_content: str) -> dict:
    """Reads a CSV file from uploaded content and returns its contents in JSON format.

    Args:
        file_content (str): The content of the uploaded CSV file as a string.

    Returns:
        dict: A dictionary with 'status' and 'result' (JSON string) or 'error_message'.
    """
    try:
        if not file_content or not isinstance(file_content, str):
            return {
                "status": "error",
                "error_message": "Invalid or empty CSV file content"
            }

        # Convert file content to a StringIO object for pandas
        csv_file = io.StringIO(file_content)
        # Read the CSV file using pandas
        df = pd.read_csv(csv_file)

        # Convert NaN to None for JSON serialization (to get null)
        df = df.where(pd.notnull(df), None)
        # Convert DataFrame to list of dictionaries with all columns
        data_list = df.to_dict('records')
        # Create the desired JSON structure
        json_output = {"data": data_list}

        # Return JSON as a string
        return {
            "status": "success",
            "result": json.dumps(json_output, indent=2, ensure_ascii=False)
        }
    except pd.errors.EmptyDataError:
        return {
            "status": "error",
            "error_message": "CSV file is empty or invalid"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error reading CSV file: {str(e)}"
        }


# Create the ADK tool
csv_tool = FunctionTool(read_csv_file)

async def get_add_document_contents(technology_stack: str, user_input: str, ap_name: str, m_name: str, mail: str, configurations: str, env_type:str, region: str, service_domain: str, dev_cost: Optional[str]="2000", qa_cost: Optional[str]="3000", prod_cost: Optional[str]="5000"):

    # Run all four functions concurrently using asyncio.gather
    tech_arch_task, dev_ops_task, risks_task, appendix_task = await asyncio.gather(
        tech_arch(technology_stack, user_input, configurations,ap_name, m_name, mail, env_type, region, service_domain),
        Development_and_Operations(technology_stack, ap_name, m_name, mail, dev_cost, qa_cost, prod_cost),
        risksAssumptions(technology_stack, ap_name, m_name, mail),
        Appendix(technology_stack, ap_name, m_name, mail)
    )

    # Combine results into a single dictionary
    combined_results = {
        "technical_architecture": tech_arch_task,
        "devops_and_operations": dev_ops_task,
        "risks_and_assumptions": risks_task,
        "appendix": appendix_task
    }

    print("Combined Results:", combined_results)
    return combined_results

GEMINI_MODEL = "gemini-2.5-flash-preview-05-20"
MAX_TOKENS = 65000
TEMPERATURE_VALUE = 0.2

input_gathering_agent = LlmAgent(
    name="InputGatheringAgent",
    model=GEMINI_MODEL,
    description="Agent needs to gather inputs from the csv file.",
    instruction=INPUT_PROMPT,
    output_key='UserInput',
    tools= [csv_tool],
    generate_content_config=types.GenerateContentConfig(
            temperature=TEMPERATURE_VALUE,
            max_output_tokens=MAX_TOKENS
        )
)

validation_agent = LlmAgent(
    name = "InputValidationAgent",
    model=GEMINI_MODEL,
    description="Agent needs to validate the response of InputGatheringAgent",
    instruction=VALIDATION_PROMPT,
    tools=[validate_input],
    output_key='ValidatedInput',
    generate_content_config=types.GenerateContentConfig(
            temperature=TEMPERATURE_VALUE,
            max_output_tokens=MAX_TOKENS
        )
)

add_generation_agent = LlmAgent(
    name = "AddGenerationAgent",
    model= GEMINI_MODEL,
    description="Agent needs to validate the response of InputValidationAgent and InputGatheringAgent",
    instruction=ADD_INSTRUCTION_PROMPT,
    tools=[get_add_document_contents],
    output_key='AddGenerationOutput',
    generate_content_config=types.GenerateContentConfig(
            temperature=TEMPERATURE_VALUE,
            max_output_tokens=MAX_TOKENS
        )
)

terraform_agent = LlmAgent(
    name = "TerraformGenerationAgent",
    model= GEMINI_MODEL,
    description="Agent needs to validate the response of InputValidationAgent",
    instruction=TERRAFORM_INSTRUCTION_PROMPT,
    tools=[bulk_terraform],
    output_key='TerraformGenerationOutput',
    generate_content_config=types.GenerateContentConfig(
            temperature=TEMPERATURE_VALUE,
            max_output_tokens=MAX_TOKENS
        )
)

class ReviewModel(BaseModel):
    status: str
    review_comments: str

review_terraform_agent = LlmAgent(
    name= "ReviewTerraformAgent",
    model= GEMINI_MODEL,
    description="Agent to review the code that has all the input values.",
    instruction=REVIEW_TERRAFORM_INSTRUCTION_PROMPT,
    # output_schema = ReviewModel,
    output_key= "ReviewTerraformOutput",
    generate_content_config= types.GenerateContentConfig(
        temperature= TEMPERATURE_VALUE,
        max_output_tokens= MAX_TOKENS
    )
)
pr_raise_tool = FunctionTool(bulk_commit)
pr_raise_agent = LlmAgent(
    name= "PrRaiseAgent",
    model= GEMINI_MODEL,
    description= "Agent to raise the Github PR.",
    instruction=PR_RAISE_PROMPT,
    output_key= "PrRaiseOutput",
    tools=[pr_raise_tool],
    generate_content_config= types.GenerateContentConfig(
        temperature= TEMPERATURE_VALUE,
        max_output_tokens= MAX_TOKENS        
    )
)

code_pipeline_agent = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[input_gathering_agent, validation_agent, add_generation_agent, terraform_agent, review_terraform_agent, pr_raise_agent],
    description="Executes a sequence of gathering the input from csv file, validating it and generate the add document based on it.",
    # The agents will run in the order provided: Writer -> Reviewer -> Refactorer
)

# For ADK tools compatibility, the root agent must be named `root_agent`
root_agent = code_pipeline_agent

