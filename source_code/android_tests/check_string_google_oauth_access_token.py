# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://stackoverflow.com/questions/10291696/does-my-google-oauth2-token-look-right
# [2023.06.21] Reference: https://github.com/google/oauth2l/blob/master/README.md
# Valid Google OAuth Access Token: ya29.AHES67zeEn-RDg9CA5gGKMLKuG4uVB7W4O4WjNr-NBfY6Dtad4vbIZ
# Valid Google OAuth Access Token: ya29.zyxwvutsrqpnmolkjihgfedcba
# Valid Google OAuth Access Token: ya29.KAJSDH91231k23nAJSNDAKj-utsrqpnmolkjihgASJKL12

def check_string_google_oauth_access_token(file_content):
    
    google_oauth_access_token_regex = 'ya29\.[0-9A-Za-z\-_]+'
    google_oauth_access_token_items_list = []

    google_oauth_access_token_items_list = re.findall(google_oauth_access_token_regex, file_content)
    
    return google_oauth_access_token_items_list


def run_check_string_google_oauth_access_token(application_package_system, application_package_name, file_name, file_content):

    google_oauth_access_token_items_list = check_string_google_oauth_access_token(file_content)
    
    if len(google_oauth_access_token_items_list) > 0:
        for google_oauth_access_token_item in google_oauth_access_token_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.VULNERABLE, "Google OAuth Access Token", google_oauth_access_token_item)
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google OAuth Access Token", "")