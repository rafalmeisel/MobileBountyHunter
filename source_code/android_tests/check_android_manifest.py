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

application_package_system = "Android"

def checks_android_manifest_debuggable(application_package_name, android_manifest_relative_file_path):
    
    debuggable_activity_true_regex='.*debuggable="true".*'
    debuggable_activity_type_value=""
    debuggable_activity_type_regex='(?:<)(.*?) (?=android)'
    debuggable_activity_name_value=""
    debuggable_activity_name_regex='(?:(name="))(.*?)(?=")'
    is_debuggable_flag=False

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_manifest_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_manifest_relative_file_path)
    android_manifest_file_content = open(android_manifest_file_path, "r").readlines()

    for line in android_manifest_file_content:
        if re.search(debuggable_activity_true_regex, line):
            if re.search(debuggable_activity_name_regex, line):
                debuggable_activity_name_value = str(re.search(debuggable_activity_name_regex, line).group(2))

            debuggable_activity_type_value = str(re.search(debuggable_activity_type_regex, line).group(1))
            report_issue(application_package_system, application_package_name, "AndroidManifest", IssueSeverity.LOW, IssueStatus.VULNERABLE, "Debug", debuggable_activity_type_value + ":" + debuggable_activity_name_value)
            # report_status_found_with_token_value("Android", application_package_name, "AndroidManifest", "Debug", debuggable_activity_type_value + ":" + debuggable_activity_name_value)
            
            is_debuggable_flag = True

        else:
            is_debuggable_flag = is_debuggable_flag or False

    if not is_debuggable_flag:
        # report_status_not_found("Android", application_package_name, "AndroidManifest", "Debug")
        report_issue(application_package_system, application_package_name, "AndroidManifest", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Debug", "")


def checks_android_manifest_allow_backup(application_package_name, android_manifest_relative_file_path):
    
    allow_backup_activity_true_regex='.*allowBackup="true".*'
    allow_backup_activity_type_value=""
    allow_backup_activity_type_regex='(?:<)(.*?) (?=android)'
    allow_backup_activity_name_value=""
    allow_backup_activity_name_regex='(?:(name="))(.*?)(?=")'
    is_allow_backup_flag=False

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_manifest_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_manifest_relative_file_path)
    android_manifest_file_content = open(android_manifest_file_path, "r").readlines()
   
    for line in android_manifest_file_content:
        if re.search(allow_backup_activity_true_regex, line):
            if re.search(allow_backup_activity_name_regex, line):
                allow_backup_activity_name_value = str(re.search(allow_backup_activity_name_regex, line).group(2))
            
            allow_backup_activity_type_value = str(re.search(allow_backup_activity_type_regex, line).group(1))
            report_issue(application_package_system, application_package_name, "AndroidManifest", IssueSeverity.LOW, IssueStatus.VULNERABLE, "allowBackup", allow_backup_activity_type_value + ":" + allow_backup_activity_name_value)
            # report_status_found_with_token_value("Android", application_package_name, "AndroidManifest", "allowBackup", allow_backup_activity_type_value + ":" + allow_backup_activity_name_value)
            
            is_allow_backup_flag = True
            
        else:
            is_allow_backup_flag = is_allow_backup_flag or False

    if not is_allow_backup_flag:
        report_issue(application_package_system, application_package_name, "AndroidManifest", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "allowBackup", "")
        # report_status_not_found("Android", application_package_name, "AndroidManifest", "allowBackup")

def checks_android_manifest_exported(application_package_name, android_manifest_relative_file_path):
    
    exported_activity_true_regex='.*exported="true".*'
    exported_activity_type_value=""
    exported_activity_type_regex='(?:<)(.*?) (?=android)'
    exported_activity_name_value=""
    exported_activity_name_regex='(?:(name="))(.*?)(?=")'
    is_exported_flag = False

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_manifest_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_manifest_relative_file_path)
    android_manifest_file_content = open(android_manifest_file_path, "r").readlines()
    
    for line in android_manifest_file_content:
        if re.search(exported_activity_true_regex, line):
            if re.search(exported_activity_name_regex, line):
                exported_activity_name_value = str(re.search(exported_activity_name_regex, line).group(2))
            
            exported_activity_type_value = str(re.search(exported_activity_type_regex, line).group(1))
            report_issue(application_package_system, application_package_name, "AndroidManifest", IssueSeverity.LOW, IssueStatus.TO_VERIFY, "exported", exported_activity_type_value + ":" + exported_activity_name_value)
            # report_status_found_with_token_value("Android", application_package_name, "AndroidManifest", "exported", exported_activity_type_value + ":" + exported_activity_name_value)

            is_exported_flag = True
        
        else:
            is_exported_flag = is_exported_flag or False

    if not is_exported_flag:
        report_issue(application_package_system, application_package_name, "AndroidManifest", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "exported", "")
        # report_status_not_found("Android", application_package_name, "AndroidManifest", "exported")


def checks_android_manifest_cloudinary(application_package_name, android_manifest_relative_file_path):
    
    cloudinary_regex = 'cloudinary:\/\/.*(?="|\')'
    cloudinary_value = ""
    is_cloudinary_flag = False

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_manifest_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_manifest_relative_file_path)
    android_manifest_file_content = open(android_manifest_file_path, "r").readlines()
    
    for line in android_manifest_file_content:
        if re.search(cloudinary_regex, line):
            cloudinary_value = re.search(cloudinary_regex, line).group(0)
            report_issue(application_package_system, application_package_name, "AndroidManifest", IssueSeverity.INFORMATIVE, IssueStatus.TO_VERIFY, "Cloudinary", "")
            # report_status_found_with_token_value("Android", application_package_name, "AndroidManifest", "Cloudinary", str(cloudinary_value))

            is_cloudinary_flag = True
        
        else:
            is_cloudinary_flag= is_cloudinary_flag or False

    if not is_cloudinary_flag:
        report_issue(application_package_system, application_package_name, "AndroidManifest", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Cloudinary", "")
        # report_status_not_found("Android", application_package_name, "AndroidManifest", "Cloudinary")