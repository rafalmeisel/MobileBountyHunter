# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import re
import os
import pathlib
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus
from source_code.report_manager import copy_file_to_dedicated_report_directory
from source_code.config_file_manager import get_android_output_directory_relative_path
from source_code.config_file_manager import get_dedicated_mobile_bounty_hunter_report_directory_relative_path
from source_code.config_file_manager import get_android_decompiling_tool

def check_string_javascript_enabled(file_content):
    
    javascript_enabled_regex = 'setJavaScriptEnabled'
    javascript_enabled_items_list = []

    javascript_enabled_items_list = re.findall(javascript_enabled_regex, file_content)
    
    return javascript_enabled_items_list


def run_check_string_javascript_enabled(application_package_system, application_package_name):

    javascript_enabled_found = False

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    dedicated_mobile_bounty_hunter_report_directory_relative_path = get_dedicated_mobile_bounty_hunter_report_directory_relative_path()
    
    file_regex = ""
    android_application_smali_directory_path = ""

    if get_android_decompiling_tool() == "jadx":
        file_regex = "*.java"
        android_application_smali_directory_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "sources")
    elif get_android_decompiling_tool() == "apktool":
        file_regex = "*.smali"
        android_application_smali_directory_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "smali")

    files_list = [f for f in android_application_smali_directory_path.rglob(file_regex) if f.is_file()]

    if len(files_list) > 0:
        for file_path in files_list:
            android_application_dedicated_report_directory = pathlib.Path(android_output_directory_relative_path, application_package_name, dedicated_mobile_bounty_hunter_report_directory_relative_path, os.path.basename(file_path))
            
            file_name = os.path.basename(file_path)

            with open(file_path, "r") as file:
                file_content = file.read()

            javascript_enabled_items_list = check_string_javascript_enabled(file_content)
            
            if len(javascript_enabled_items_list) > 0:
                javascript_enabled_found = True
                for javascript_enabled_item in javascript_enabled_items_list:
                    report_issue(application_package_system, application_package_name, file_name, IssueSeverity.MEDIUM, IssueStatus.TO_VERIFY, "JavaScriptEnabled", javascript_enabled_item)
                    copy_file_to_dedicated_report_directory(str(file_path), str(android_application_dedicated_report_directory))
    
    if not (javascript_enabled_found):
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "JavaScriptEnabled", "")