import json

def read_config_file_contents():
    with open('./workspace/config/config_runtime.json') as config_file:
        config_file_contents = config_file.read()
    return config_file_contents


def get_config_file_json():
    config_file_json = json.loads(read_config_file_contents())
    return config_file_json


def get_global_mobile_bounty_hunter_report_file_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["globalMobileBountyHunterReportFileRelativePath"]


def get_dedicated_mobile_bounty_hunter_report_file_name():
    config_file_json = get_config_file_json()
    return config_file_json["dedicatedMobileBountyHunterReportFileName"]


def get_dedicated_mobile_bounty_hunter_report_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["dedicatedMobileBountyHunterReportDirectoryRelativePath"]


def get_store_urls_list_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["storeUrlsListRelativePath"]


def get_application_package_name_list_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["applicationPackageNameListRelativePath"]


def append_to_application_package_name_list(application_package_name):
    application_package_name_list_relative_path = get_application_package_name_list_relative_path()
    application_package_name_list_file = open(application_package_name_list_relative_path, "a")
    application_package_name_list_file.write(application_package_name+"\n")
    application_package_name_list_file.close()

def get_android_decompiling_tool():
    config_file_json = get_config_file_json()
    return config_file_json["androidDecompilingTool"]


def get_android_input_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["androidInputDirectoryRelativePath"]


def get_android_input_analyzed_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["androidInputAnalyzedDirectoryRelativePath"]


def get_android_output_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["androidOutputDirectoryRelativePath"]


def get_android_output_analyzed_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["androidOutputAnalyzedDirectoryRelativePath"]


def get_ios_input_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["iosInputDirectoryRelativePath"]


def get_ios_input_analyzed_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["iosInputAnalyzedDirectoryRelativePath"]


def get_ios_output_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["iosOutputDirectoryRelativePath"]


def get_ios_output_analyzed_directory_relative_path():
    config_file_json = get_config_file_json()
    return config_file_json["iosOutputAnalyzedDirectoryRelativePath"]