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

def run_android_tests(application_package_name):
    
    output_directory_application_package_names_relative_path = get_android_output_directory_relative_path()

    # if outputDirectoryApplicationPackageNames:
    #     first_folder = outputDirectoryApplicationPackageNames[0]
    resources_folder = os.path.join(output_directory_application_package_names_relative_path, application_package_name, "resources")
    sources_folder = os.path.join(output_directory_application_package_names_relative_path, application_package_name, "sources")

    # Application was decompiled with Jadx
    if os.path.isdir(resources_folder) and os.path.isdir(sources_folder):
        android_manifest_relative_file_path = "/resources/AndroidManifest.xml"
        android_res_values_strings_relative_file_path = "/resources/res/values/strings.xml"
    
    # Application was decompiled with apktools
    else:
        android_manifest_relative_file_path = "/AndroidManifest.xml"
        android_res_values_strings_relative_file_path = "/res/values/strings.xml"


    # for application_package_name in outputDirectoryApplicationPackageNames:
    print("Analyzing application: " + colored(application_package_name, 'cyan'))

    # checksAndroidManifestDebuggable(application_package_name, android_manifest_relative_file_path)
    # checksAndroidManifestAllowBackup(application_package_name, android_manifest_relative_file_path)
    # checksAndroidManifestExported(application_package_name, android_manifest_relative_file_path)
    # checksAndroidManifestCloudinary(application_package_name, android_manifest_relative_file_path)
    
    # checksResValuesStringsAwsLongTermAccessKeys(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringsAwsShortTermAccessKeys(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringsAwSecretAccessKey(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringsAwsBucket(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringsPushIoApplicationIdentifier(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringsFirebaseUrl(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringsAwsBucket(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringGoogleApiKey(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringGoogleCloudPlatformGoogleUserContent(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringGoogleOAuthAccessToken(application_package_name, android_res_values_strings_relative_file_path)
    # checksResValuesStringGoogleAppSpot(application_package_name, android_res_values_strings_relative_file_path)

    search_files_with_sqlite_extensions(application_package_name)
    search_files_with_db_extensions(application_package_name)
    
    search_config_files_with_any_extensions(application_package_name)

    find_java_script_enabled(application_package_name)
    check_exported_activity_with_java_script_enabled(application_package_name)