# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop-mobile/ios/in-app-msg.htm
# Valid PushIo Application Identifier: pio-ABEgGFd_CNo9NOL_87c6k2GzI
# Valid PushIo Application Identifier: pio-njj1jjNNGg
# Valid PushIo Application Identifier: pio-Aasdasdkq_askjndk1jn2

def check_string_push_io_application_identifier(file_content):
    
    push_io_application_identifier_regex = 'pio-[0-9A-Za-z-_]*'
    push_io_application_identifier_items_list = []

    push_io_application_identifier_items_list = re.findall(push_io_application_identifier_regex, file_content)
    
    return push_io_application_identifier_items_list

def run_check_string_push_io_application_identifier(application_package_system, application_package_name, file_name, file_content):

    push_io_application_identifier_items_list = check_string_push_io_application_identifier(file_content)
    
    if len(push_io_application_identifier_items_list) > 0:
        for push_io_application_identifier_item in push_io_application_identifier_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.FOUND, "PushIo Application Identifier", push_io_application_identifier_item)
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "PushIo Application Identifier", "")