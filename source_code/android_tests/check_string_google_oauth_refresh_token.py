# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://stackoverflow.com/questions/10291696/does-my-google-oauth2-token-look-right
# Valid Google OAuth Refresh Token: 1//0gd2xhT4mpKx-CgYIARAAGBASNwF-L9IrrYekXHq_dI5g7A4a4z6ZX0eRvzYg-9Zbo2bkRr3LiN0DlwS8gJ-Rg7zWK_TFlbOcNu8
# Valid Google OAuth Refresh Token: 1/Ry68
# Valid Google OAuth Refresh Token: 1/KAJSDH91231k23nAJSNDAKj-utsrqpnmolkjihgASJKL12

def check_string_google_oauth_refresh_token(file_content):
    
    google_oauth_refresh_token_regex = '1\/.[0-9A-Za-z\-_\/]+'
    google_oauth_refresh_token_items_list = []

    google_oauth_refresh_token_items_list = re.findall(google_oauth_refresh_token_regex, file_content)
    
    return google_oauth_refresh_token_items_list


def run_check_string_google_oauth_refresh_token(application_package_system, application_package_name, file_name, file_content):

    google_oauth_refresh_token_items_list = check_string_google_oauth_refresh_token(file_content)
    
    if len(google_oauth_refresh_token_items_list) > 0:
        for google_oauth_refresh_token_item in google_oauth_refresh_token_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.VULNERABLE, "Google OAuth Access Token", google_oauth_refresh_token_item)
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google OAuth Access Token", "")