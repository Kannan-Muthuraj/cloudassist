#!/usr/bin/env python3
"""
Simple test script for WordGenerator
"""

from word_generator import WordGenerator
import os


def test_word_generator():
    print("Testing Word Generator...")

    # Create test data
    test_data = {
        'mmUnit': 'Test Unit',
        'apName': 'Test Application',
        'mName': 'TEST-001',
        'authorName': 'Test User',
        'formattedDate': '2024-01-01',

        # HTML content
        'htmlAppOverviewData': '''
            <p>This is a <b>test</b> application overview with <i>formatting</i>.</p>
            <p>Special text: $highlighted content$</p>
            <ul>
                <li>Feature 1</li>
                <li>Feature 2</li>
            </ul>
        ''',

        'htmlBNData': '<p>Business needs for the <b>test application</b></p>',
        'htmlKFData': '<ul><li>Key Feature 1</li><li>Key Feature 2</li></ul>',
        'htmlUSData': '<p>As a user, I want to $test the document$</p>',
        'htmlLAData': '<p>Logical architecture description</p>',
        'htmlDMData': '<p>Deployment model description</p>',

        # Other data
        'tsData': 'Python, Docker, GKE, PostgreSQL, Redis',

        # Tables
        'paData': [
            {
                'group': 'admin-group',
                'owners': 'admin@test.com',
                'description': 'Administrative access',
                'environment': 'Production'
            },
            {
                'group': 'dev-group',
                'owners': 'dev@test.com',
                'description': 'Development access',
                'environment': 'Development'
            }
        ],

        'frData': [
            {
                'network': '10.0.0.0/24',
                'actions': 'Allow',
                'sourceip': '0.0.0.0/0',
                'destination': '10.0.0.1',
                'port': '443',
                'protocol': 'TCP',
                'direction': 'Ingress'
            }
        ],

        'iamData': [
            {
                'service': 'Cloud Storage',
                'principal': 'test-service@test.iam',
                'environment': 'Production',
                'permission': 'storage.admin, storage.viewer'
            }
        ],

        'osmData': [
            {
                'component': 'Frontend',
                'dev': 'Dev Team',
                'prod': 'SRE Team',
                'qa': 'QA Team',
                'uat': 'UAT Team'
            }
        ],

        'htmlKCDataTable': [
            {
                'service': 'API Gateway',
                'dev': 'dev-api.test.com',
                'prod': 'api.test.com',
                'qa': 'qa-api.test.com'
            }
        ],

        'fileName': 'test.xlsx'
    }

    try:
        # Create Word Generator instance
        generator = WordGenerator()

        # Generate document
        filename = generator.generate_document(test_data)

        # Check if file exists
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            print(f"✓ Success! Document generated: {filename}")
            print(f"  File size: {file_size:,} bytes")
            print(f"  Location: {os.path.abspath(filename)}")
        else:
            print("✗ Error: File was not created")

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_word_generator()
