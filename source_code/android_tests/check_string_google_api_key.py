# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import requests
import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://stackoverflow.com/questions/70204768/why-google-map-api-key-have-39-chars
# Valid Google API Key: AIzaSyCmD-JJN2Hx2kEa5j8d4VUZ6Z4_qBXYZ13
# Valid Google API Key: AIzaSyDLRbfN8EiAMjcfsXuvE_CKfSlZ3E17xyz
# Valid Google API Key: AIzaSyDLR_asd8EiAMjcfsXuvE_CKfSl12317xy

def check_string_google_api_key(file_content):
    
    google_api_key_regex = 'AIza[0-9A-Za-z-_]{35}'
    google_api_key_items_list = []

    google_api_key_items_list = re.findall(google_api_key_regex, file_content)
    
    return google_api_key_items_list

def send_request_to_google_api(google_api_key):
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountains+View,+CA&key=" + google_api_key)
    data = str(response.json())

    return data

def run_check_string_google_api_key(application_package_system, application_package_name, file_name, file_content):

    google_api_key_items_list = check_string_google_api_key(file_content)
    
    if len(google_api_key_items_list) > 0:
        for google_api_key_item in google_api_key_items_list:
            
            googleApiResponseData = send_request_to_google_api(google_api_key_item)

            if "REQUEST_DENIED" in googleApiResponseData:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.SECURED, "Google API Key", google_api_key_item + " permission denied.")
                
            else:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.VULNERABLE, "Google API Key", google_api_key_item + " is open.")
                
                
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google API Key", "")