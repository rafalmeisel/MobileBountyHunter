import pathlib
import os
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus
from source_code.report_manager import copy_file_to_dedicated_report_directory
from source_code.config_file_manager import get_android_output_directory_relative_path
from source_code.config_file_manager import get_dedicated_mobile_bounty_hunter_report_directory_relative_path

def search_config_files_with_config_extensions(application_package_system, application_package_name):
    
    issue_type = "Config file"

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    dedicated_mobile_bounty_hunter_report_directory_relative_path = get_dedicated_mobile_bounty_hunter_report_directory_relative_path()
    android_application_directory_relative_path = pathlib.Path(android_output_directory_relative_path, dedicated_mobile_bounty_hunter_report_directory_relative_path, application_package_name)
    

    config_files_list = [f for f in android_application_directory_relative_path.rglob("*config*") if f.is_file()]
    
    if len(config_files_list) > 0:

        for config_file_path in config_files_list:
            
            config_file_basename = os.path.basename(config_file_path)
            android_dedicated_report_application_directory_destination_file_path = pathlib.Path(android_application_directory_relative_path, config_file_basename)
            report_issue(application_package_system, application_package_name, config_file_basename, IssueSeverity.MEDIUM, IssueStatus.TO_VERIFY, issue_type, str(config_file_path))
            copy_file_to_dedicated_report_directory(str(config_file_path), str(android_dedicated_report_application_directory_destination_file_path))

    else:
        report_issue(application_package_system, application_package_name, "", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")