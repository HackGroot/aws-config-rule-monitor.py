import boto3
import logging

# Specify the AWS region to monitor
region = 'us-west-2'

# Create a Config client
config_client = boto3.client('config', region_name=region)

# Define a function to check for compliance with a Config rule
def check_rule_compliance(config_rule_name):
    try:
        # Get the latest evaluation results for the Config rule
        response = config_client.get_compliance_details_by_config_rule(
            ConfigRuleName=config_rule_name
        )
        evaluation_results = response['EvaluationResults']

        # Check if the latest evaluation result is NON_COMPLIANT
        latest_result = evaluation_results[-1]
        if latest_result['ComplianceType'] == 'NON_COMPLIANT':
            # Take remediation action
            logging.error(f'Config rule {config_rule_name} is non-compliant.')
            # Replace the logging statement above with your remediation action(s)
        else:
            logging.info(f'Config rule {config_rule_name} is compliant.')
    except Exception as e:
        logging.error(f'Error checking compliance for rule {config_rule_name}: {str(e)}')

# Main function
def main():
    # Configure logging
    logging.basicConfig(filename='config_rule_monitor.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')

    # Specify the Config rules to monitor
    config_rule_names = ['<your-config-rule-name-1>', '<your-config-rule-name-2>']

    # Check compliance for each Config rule
    for rule_name in config_rule_names:
        check_rule_compliance(rule_name)

if __name__ == '__main__':
    main()
