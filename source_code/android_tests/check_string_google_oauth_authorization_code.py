# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://stackoverflow.com/questions/10291696/does-my-google-oauth2-token-look-right
# [2023.06.21] Reference: https://developers.google.com/identity/protocols/oauth2/web-server?hl=pl
# Valid Google Authorization Code: 4/Omoy
# Valid Google Authorization Code: 4/P7q-oMsCeLvIaQm6bTrgtp7
# Valid Google Authorization Code: 4/P7q7W91a-oMsCesrqpnmolkjsrqpnm7W91agASJKL12

def check_string_google_oauth_authorization_code(file_content):
    
    google_oauth_authorization_code_regex = '4\/[0-9A-Za-z\-_]+'
    google_oauth_authorization_code_items_list = []

    google_oauth_authorization_code_items_list = re.findall(google_oauth_authorization_code_regex, file_content)
    
    return google_oauth_authorization_code_items_list


def run_check_string_google_oauth_authorization_code(application_package_system, application_package_name, file_name, file_content):

    google_oauth_authorization_code_items_list = check_string_google_oauth_authorization_code(file_content)
    
    if len(google_oauth_authorization_code_items_list) > 0:
        for google_oauth_authorization_code_item in google_oauth_authorization_code_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.VULNERABLE, "Google Authorization Code", google_oauth_authorization_code_item)
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google Authorization Code", "")