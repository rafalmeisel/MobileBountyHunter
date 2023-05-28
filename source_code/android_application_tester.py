from source_code.config_file_manager import get_android_output_directory_relative_path
from source_code.config_file_manager import get_android_decompiling_tool
from source_code.android_tests.check_android_manifest import *
from source_code.android_tests.check_res_values_strings import *
from source_code.android_tests.check_files_names import *
from source_code.android_tests.check_smali_files import *
from source_code.android_tests.check_report_file import *

import os
from termcolor import colored

android_manifest_relative_file_path = ""
android_res_values_strings_relative_file_path = ""

def run_tests_android_application(application_package_name):
    
    android_output_directory_relative_path = get_android_output_directory_relative_path()
    
    android_application_jadx_resources_directory_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "resources")
    android_application_jadx_sources_directory_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "sources")

    # Check if android application was decompiled with Jadx, "resources" and "source" directories should be locaten in application directory
    if os.path.exists(android_application_jadx_resources_directory_path) and os.path.exists(android_application_jadx_sources_directory_path):
        android_manifest_relative_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "resources/AndroidManifest.xml")
        android_res_values_strings_relative_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "resources/res/values/strings.xml")

    else:
        android_manifest_relative_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "AndroidManifest.xml")
        android_res_values_strings_relative_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, "res/values/strings.xml")

    print("Analyzing application: " + colored(application_package_name, 'cyan'))
    
    android_manifest_basename = os.path.basename(android_manifest_relative_file_path)
    android_manifest_content = open(android_manifest_relative_file_path, "r").readlines()
    
    android_values_strings_basename = os.path.basename(android_res_values_strings_relative_file_path)
    android_values_strings_content = open(android_res_values_strings_relative_file_path, "r").readlines()
    
    checks_android_manifest_debuggable(application_package_system, application_package_name, android_manifest_basename, android_manifest_content)
    checks_android_manifest_allow_backup(application_package_system, application_package_name, android_manifest_basename, android_manifest_content)
    checks_android_manifest_exported(application_package_system, application_package_name, android_manifest_basename, android_manifest_content)
    
    check_res_values_strings_cloudinary(application_package_system, application_package_name, android_manifest_basename, android_manifest_content)
    check_res_values_strings_aws_long_term_access_keys(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_aws_short_term_access_keys(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_aws_secret_access_key(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_aws_bucket(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_push_io_application_identifier(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_firebase_url(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_aws_bucket(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_google_api_key(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_google_cloud_platform_google_user_content(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_google_oauth_access_token(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    check_res_values_strings_google_app_spot(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)

    search_files_with_sqlite_extensions(application_package_name)
    search_files_with_db_extensions(application_package_name)
    
    search_config_files_with_any_extensions(application_package_name)

    check_java_script_enabled(application_package_name)
    check_exported_activity_with_java_script_enabled(application_package_name)

def run_android_tests_in_android_output_directory():
    
    output_directory_application_package_names_relative_path = get_android_output_directory_relative_path()
    output_directory_android_applications = [d for d in os.listdir(output_directory_application_package_names_relative_path) if os.path.isdir(os.path.join(output_directory_application_package_names_relative_path, d))]
    
    for application_package_name in output_directory_android_applications:
        run_tests_android_application(application_package_name)