# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# Valid AWS Long Term Key: AKS3G7H9T1F4J2K6L8M
# Valid AWS Long Term Key: AKabcdefgh1234567
# Valid AWS Long Term Key: AK1234567890ABCDEFG
# Valid AWS Long Term Key: AKSDFGHJKLZXCVBNM

def check_string_aws_long_term_access_key(file_content):
    
    aws_long_term_access_key_regex = 'AK[A-Za-z0-9]{18}'
    aws_long_term_access_key_items_list = []

    aws_long_term_access_key_items_list = re.findall(aws_long_term_access_key_regex, file_content)
    
    return aws_long_term_access_key_items_list


def run_check_string_aws_long_term_access_key(application_package_system, application_package_name, file_name, file_content):

    aws_long_term_access_key_items_list = check_string_aws_long_term_access_key(file_content)
    
    if len(aws_long_term_access_key_items_list) > 0:
        for aws_long_term_access_key_item in aws_long_term_access_key_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.VULNERABLE, "AWS Long Term Access Key", aws_long_term_access_key_item)
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "AWS Long Term Access Key", "")