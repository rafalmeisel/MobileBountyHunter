from source_code.config_file_manager import get_android_output_directory_relative_path

from source_code.android_tests.check_android_manifest_allow_backup import run_check_android_manifest_allow_backup
from source_code.android_tests.check_android_manifest_debuggable import run_check_android_manifest_debuggable
from source_code.android_tests.check_android_manifest_exported import run_check_android_manifest_exported

from source_code.android_tests.check_files_extention_config import search_config_files_with_config_extensions
from source_code.android_tests.check_files_extention_db import search_files_with_db_extensions
from source_code.android_tests.check_files_extention_sqlite import search_files_with_sqlite_extensions

from source_code.android_tests.check_report_file import *

from source_code.android_tests.check_string_aws_bucket import run_check_string_aws_bucket
from source_code.android_tests.check_string_aws_long_term_access_key import run_check_string_aws_long_term_access_key
from source_code.android_tests.check_string_aws_secret_access_key import run_check_string_aws_secret_access_key
from source_code.android_tests.check_string_aws_short_term_access_key import run_check_string_aws_short_term_access_key
from source_code.android_tests.check_string_cloudinary import run_check_string_cloudinary
from source_code.android_tests.check_string_google_api_key import run_check_string_google_api_key
from source_code.android_tests.check_string_google_app_spot import run_check_string_google_app_spot
from source_code.android_tests.check_string_google_firebaseio import run_check_string_google_firebaseio
from source_code.android_tests.check_string_google_oauth_access_token import run_check_string_google_oauth_access_token
from source_code.android_tests.check_string_google_oauth_authorization_code import run_check_string_google_oauth_authorization_code
from source_code.android_tests.check_string_google_oauth_refresh_token import run_check_string_google_oauth_refresh_token
from source_code.android_tests.check_string_google_user_content import run_check_string_google_user_content
from source_code.android_tests.check_string_javascript_enabled import run_check_string_javascript_enabled
from source_code.android_tests.check_string_push_io_application_identifier import run_check_string_push_io_application_identifier

import xml.etree.ElementTree as ET


import os
from termcolor import colored

android_manifest_relative_file_path = ""
android_res_values_strings_relative_file_path = ""
application_package_system = "Android"

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

    with open(android_manifest_relative_file_path, "r") as file:
        android_manifest_content = file.read()
        android_manifest_content_xml = ET.ElementTree(ET.fromstring(android_manifest_content))

    android_values_strings_basename = os.path.basename(android_res_values_strings_relative_file_path)

    with open(android_res_values_strings_relative_file_path, "r") as file:
        android_values_strings_content = file.read()
    
    run_check_android_manifest_allow_backup(application_package_system, application_package_name, android_manifest_basename, android_manifest_content_xml)
    run_check_android_manifest_debuggable(application_package_system, application_package_name, android_manifest_basename, android_manifest_content_xml)
    run_check_android_manifest_exported(application_package_system, application_package_name, android_manifest_basename, android_manifest_content_xml)
    
    search_config_files_with_config_extensions(application_package_system, application_package_name)
    search_files_with_db_extensions(application_package_system, application_package_name)
    search_files_with_sqlite_extensions(application_package_system, application_package_name)
    
    check_exported_activity_with_java_script_enabled(application_package_system, application_package_name)
    
    run_check_string_aws_bucket(application_package_system, application_package_name, android_values_strings_basename, android_manifest_content)
    run_check_string_aws_long_term_access_key(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_aws_secret_access_key(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_aws_short_term_access_key(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_cloudinary(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_google_api_key(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_google_app_spot(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_google_firebaseio(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_google_oauth_access_token(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_google_oauth_authorization_code(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_google_oauth_refresh_token(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_google_user_content(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)
    run_check_string_javascript_enabled(application_package_system, application_package_name)
    run_check_string_push_io_application_identifier(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content)


    

def run_android_tests_in_android_output_directory():
    
    output_directory_application_package_names_relative_path = get_android_output_directory_relative_path()
    output_directory_android_applications = [d for d in os.listdir(output_directory_application_package_names_relative_path) if os.path.isdir(os.path.join(output_directory_application_package_names_relative_path, d))]
    
    for application_package_name in output_directory_android_applications:
        run_tests_android_application(application_package_name)