# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# Cloudinary Basic Auth
# cloudinary://api_key:api_secret@cloud_name
# cloudinary://123456789:abcdefghijk@example-cloud

def check_string_cloudinary(file_content):
    
    cloudinary_regex = 'cloudinary:\/\/[a-zA-Z0-9_-]+:[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+'
    cloudinary_items_list = []

    cloudinary_items_list = re.findall(cloudinary_regex, file_content)
    
    return cloudinary_items_list


def run_check_string_cloudinary(application_package_system, application_package_name, file_name, file_content):

    cloudinary_items_list = check_string_cloudinary(file_content)
    
    if len(cloudinary_items_list) > 0:
        for cloudinary_item in cloudinary_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.VULNERABLE, "Cloudinary", cloudinary_item)
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Cloudinary", "")