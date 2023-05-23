from source_code.config_file_manager import get_android_output_directory_relative_path
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
    
    output_directory_application_package_names_relative_path = get_android_output_directory_relative_path()

    # if outputDirectoryApplicationPackageNames:
    #     first_folder = outputDirectoryApplicationPackageNames[0]
    resources_folder = os.path.join(output_directory_application_package_names_relative_path, application_package_name, "resources")
    sources_folder = os.path.join(output_directory_application_package_names_relative_path, application_package_name, "sources")

    # Application was decompiled with Jadx
    if os.path.isdir(resources_folder) and os.path.isdir(sources_folder):
        android_manifest_relative_file_path = "resources/AndroidManifest.xml"
        android_res_values_strings_relative_file_path = "resources/res/values/strings.xml"
    
    # Application was decompiled with apktools
    else:
        android_manifest_relative_file_path = "AndroidManifest.xml"
        android_res_values_strings_relative_file_path = "res/values/strings.xml"


    # for application_package_name in outputDirectoryApplicationPackageNames:
    print("Analyzing application: " + colored(application_package_name, 'cyan'))

    checks_android_manifest_debuggable(application_package_name, android_manifest_relative_file_path)
    checks_android_manifest_allow_backup(application_package_name, android_manifest_relative_file_path)
    checks_android_manifest_exported(application_package_name, android_manifest_relative_file_path)
    checks_android_manifest_cloudinary(application_package_name, android_manifest_relative_file_path)
    
    check_res_values_strings_aws_long_term_access_keys(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_aws_short_term_access_keys(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_aws_secret_access_key(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_aws_bucket(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_push_io_application_identifier(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_firebase_url(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_aws_bucket(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_google_api_key(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_google_cloud_platform_google_user_content(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_google_oauth_access_token(application_package_name, android_res_values_strings_relative_file_path)
    check_res_values_strings_google_app_spot(application_package_name, android_res_values_strings_relative_file_path)

    search_files_with_sqlite_extensions(application_package_name)
    search_files_with_db_extensions(application_package_name)
    
    search_config_files_with_any_extensions(application_package_name)

    find_java_script_enabled(application_package_name)
    check_exported_activity_with_java_script_enabled(application_package_name)

def run_android_tests_in_android_output_directory():
    
    output_directory_application_package_names_relative_path = get_android_output_directory_relative_path()
    output_directory_android_applications = [d for d in os.listdir(output_directory_application_package_names_relative_path) if os.path.isdir(os.path.join(output_directory_application_package_names_relative_path, d))]
    
    for application_package_name in output_directory_android_applications:
        run_tests_android_application(application_package_name)