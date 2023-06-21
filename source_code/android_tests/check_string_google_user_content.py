# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://developers.google.com/identity/openid-connect/openid-connect?hl=pl
# Valid Google User Content: 1234567890.apps.googleusercontent.com
# Valid Google User Content: 1234567890-abc123def456.apps.googleusercontent.com
# Valid Google User Content: example.apps.googleusercontent.com

def check_string_google_user_content(file_content):
    
    google_user_content_regex = '[0-9A-Za-z_-]*\.apps\.googleusercontent\.com'
    google_user_content_items_list = []

    google_user_content_items_list = re.findall(google_user_content_regex, file_content)
    
    return google_user_content_items_list


def run_check_string_google_user_content(application_package_system, application_package_name, file_name, file_content):

    google_user_content_items_list = check_string_google_user_content(file_content)
    
    if len(google_user_content_items_list) > 0:
        for google_user_content_item in google_user_content_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.FOUND, "Google User Content", google_user_content_item)
                
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google User Content", "")