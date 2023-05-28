from termcolor import colored
import re
import pathlib
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus
from source_code.config_file_manager import get_android_output_directory_relative_path

# Interesting things in AndroidManifest:
# - Exported components
# - Api keys
# - Custom deep link schemas
# - http deep link scheme
# - Deep link hosts
# - Schema endpoints
# - Deep link pathPatterns

def checks_android_manifest_debuggable(application_package_system, application_package_name, file_name, file_content):
    
    debuggable_activity_true_regex='.*debuggable="true".*'
    debuggable_activity_type_value=""
    debuggable_activity_type_regex='(?:<)(.*?) (?=android)'
    debuggable_activity_name_value=""
    debuggable_activity_name_regex='(?:(name="))(.*?)(?=")'
    is_debuggable_flag=False
    issue_type = "Debug"

    for line in file_content:
        if re.search(debuggable_activity_true_regex, line):
            if re.search(debuggable_activity_name_regex, line):
                debuggable_activity_name_value = str(re.search(debuggable_activity_name_regex, line).group(2))

            debuggable_activity_type_value = str(re.search(debuggable_activity_type_regex, line).group(1))
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.VULNERABLE, issue_type, debuggable_activity_type_value + ":" + debuggable_activity_name_value)
            
            is_debuggable_flag = True

        else:
            is_debuggable_flag = is_debuggable_flag or False

    if not is_debuggable_flag:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")


def checks_android_manifest_allow_backup(application_package_system, application_package_name, file_name, file_content):
    
    allow_backup_activity_true_regex='.*allowBackup="true".*'
    allow_backup_activity_type_value=""
    allow_backup_activity_type_regex='(?:<)(.*?) (?=android)'
    allow_backup_activity_name_value=""
    allow_backup_activity_name_regex='(?:(name="))(.*?)(?=")'
    is_allow_backup_flag=False
    issue_type = "allowBackup"
    
   
    for line in file_content:
        if re.search(allow_backup_activity_true_regex, line):
            if re.search(allow_backup_activity_name_regex, line):
                allow_backup_activity_name_value = str(re.search(allow_backup_activity_name_regex, line).group(2))
            
            allow_backup_activity_type_value = str(re.search(allow_backup_activity_type_regex, line).group(1))
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.VULNERABLE, issue_type, allow_backup_activity_type_value + ":" + allow_backup_activity_name_value)
            
            is_allow_backup_flag = True
            
        else:
            is_allow_backup_flag = is_allow_backup_flag or False

    if not is_allow_backup_flag:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")

def checks_android_manifest_exported(application_package_system, application_package_name, file_name, file_content):
    
    exported_activity_true_regex='.*exported="true".*'
    exported_activity_type_value=""
    exported_activity_type_regex='(?:<)(.*?) (?=android)'
    exported_activity_name_value=""
    exported_activity_name_regex='(?:(name="))(.*?)(?=")'
    is_exported_flag = False
    issue_type = "exported"
    
    for line in file_content:
        if re.search(exported_activity_true_regex, line):
            if re.search(exported_activity_name_regex, line):
                exported_activity_name_value = str(re.search(exported_activity_name_regex, line).group(2))
            
            exported_activity_type_value = str(re.search(exported_activity_type_regex, line).group(1))
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.TO_VERIFY, issue_type, exported_activity_type_value + ":" + exported_activity_name_value)

            is_exported_flag = True
        
        else:
            is_exported_flag = is_exported_flag or False

    if not is_exported_flag:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")