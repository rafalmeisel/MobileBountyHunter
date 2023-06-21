# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import requests
import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://firebase.google.com/docs/database/web/start?hl=pl
# Valid Google FirebaseIo Url: https://example.firebaseio.com
# Valid Google FirebaseIo Url: https://my-firebase.firebaseio.com
# Valid Google FirebaseIo Url: https://test-app.firebaseio.com

def check_string_google_firebaseio(file_content):
    
    google_firebaseio_regex = 'https.*firebaseio.com'
    google_firebaseio_items_list = []

    google_firebaseio_items_list = re.findall(google_firebaseio_regex, file_content)
    
    return google_firebaseio_items_list

def send_request_to_firebase(firebase_url):
    response = requests.get(firebase_url + "/.json")
    data = str(response.json())
    
    return data

def run_check_string_google_firebaseio(application_package_system, application_package_name, file_name, file_content):

    google_firebaseio_items_list = check_string_google_firebaseio(file_content)
    
    if len(google_firebaseio_items_list) > 0:
        for google_firebaseio_item in google_firebaseio_items_list:
            
            firebase_response_data = send_request_to_firebase(google_firebaseio_item)

            if "Permission denied" in firebase_response_data:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.SECURED, "FirebaseIo", google_firebaseio_item + " permission denied.")
                
            elif "deactivated" in firebase_response_data:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.SECURED, "FirebaseIo", google_firebaseio_item + " deactivated.")
                
            elif len(firebase_response_data) == 0:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.HIGH, IssueStatus.VULNERABLE, "FirebaseIo", google_firebaseio_item + " is open.")
                
            else:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.TO_VERIFY, "FirebaseIo", google_firebaseio_item)
                
                
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "FirebaseIo", "")