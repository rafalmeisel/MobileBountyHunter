import pathlib
from source_code.report_manager import report_status_to_verify_without_token_value
from source_code.report_manager import report_status_not_found
from source_code.report_manager import copy_file_to_dedicated_report_directory
from source_code.config_file_manager import get_android_output_directory_relative_path
from source_code.config_file_manager import get_dedicated_mobile_bounty_hunter_report_directory_relative_path

def find_java_script_enabled(application_package_name):
    
    android_output_directory_relative_path = get_android_output_directory_relative_path()
    dedicated_mobile_bounty_hunter_report_directory_relative_path = get_dedicated_mobile_bounty_hunter_report_directory_relative_path()
    android_application_dedicated_report_directory = pathlib.Path(android_output_directory_relative_path, application_package_name, dedicated_mobile_bounty_hunter_report_directory_relative_path)

    android_application_smali_directory_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "smali")

    smali_files_list = [f for f in android_application_smali_directory_path.rglob("*.smali") if f.is_file()]

    if len(smali_files_list) > 0:

        for smali_file_path in smali_files_list:
            with open(smali_file_path, "r") as smali_file:
                content = smali_file.read()
                if "setjavascriptenabled" in content.lower():
                    report_status_to_verify_without_token_value(application_package_name, str(smali_file_path), "JavaScriptEnabled")
                    copy_file_to_dedicated_report_directory(str(smali_file_path), str(android_application_dedicated_report_directory))

    else:
        report_status_not_found("Android", application_package_name, "", "JavaScriptEnabled")