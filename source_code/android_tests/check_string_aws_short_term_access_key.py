# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# Valid AWS Short Term Access Key: AS123456789012345678
# Valid AWS Short Term Access Key: ASABCDEFGHIJKLMNOPTR
# Valid AWS Short Term Access Key: AS9876543210ZYXWVUTP
# Valid AWS Short Term Access Key: AS1B2C3D4E5F6G7H8I9J

def check_string_aws_short_term_access_key(file_content):
    
    aws_short_term_access_key_regex = 'AS[A-Za-z0-9]{18}'
    aws_short_term_access_key_items_list = []

    aws_short_term_access_key_items_list = re.findall(aws_short_term_access_key_regex, file_content)
    
    return aws_short_term_access_key_items_list


def run_check_string_aws_short_term_access_key(application_package_system, application_package_name, file_name, file_content):

    aws_short_term_access_key_items_list = check_string_aws_short_term_access_key(file_content)
    
    if len(aws_short_term_access_key_items_list) > 0:
        for aws_short_term_access_key_item in aws_short_term_access_key_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.VULNERABLE, "AWS Short Term Access Key", aws_short_term_access_key_item)
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "AWS Short Term Access Key", "")