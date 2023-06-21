# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import requests
import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://stackoverflow.com/questions/46905157/how-to-change-the-target-url-in-google-app-engine
# Valid Google App Spot: example.appspot.com
# Valid Google App Spot: my-app.appspot.com
# Valid Google App Spot: app-name.appspot.com

def check_string_google_app_spot(file_content):
    
    google_app_spot_regex = '[a-zA-Z0-9-]+\.appspot\.com'
    google_app_spot_items_list = []

    google_app_spot_items_list = re.findall(google_app_spot_regex, file_content)
    
    return google_app_spot_items_list

def send_request_to_google_app_spot(google_app_spot):
    try:
        response = requests.get("https://" + google_app_spot)
        response_body = response.text
        return response_body
    except:
        return ""

def run_check_string_google_app_spot(application_package_system, application_package_name, file_name, file_content):

    google_app_spot_items_list = check_string_google_app_spot(file_content)
    
    if len(google_app_spot_items_list) > 0:
        for google_app_spot_item in google_app_spot_items_list:

            google_app_spot_response_data = send_request_to_google_app_spot(google_app_spot_item)

            if len(google_app_spot_response_data) == 0 :
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.TO_VERIFY, "Google App Spot", "Invalid URL: " + google_app_spot_item)

            elif "Error: Page not found" in google_app_spot_response_data:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.SECURED, "Google App Spot", "Error: Page not found: " + google_app_spot_item)
            
            elif "Error: Server Error" in google_app_spot_response_data:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.TO_VERIFY, "Google App Spot", "Error: Server Error: " + google_app_spot_item)                

            else:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.TO_VERIFY, "Google App Spot", google_app_spot_item)
                
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google App Spot", "")