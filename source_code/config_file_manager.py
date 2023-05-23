import json
import shutil
import os

def create_config_runtime_file():
    shutil.copyfile('./workspace/config/config.json', './workspace/config/config_runtime.json')


def delete_config_runtime_file():
    os.remove('./workspace/config/config_runtime.json')


def read_config_runtime_file():
    with open('./workspace/config/config_runtime.json') as config_runtime_file:
        config_runtime_file_contents = json.load(config_runtime_file)
    return config_runtime_file_contents


def write_config_runtime_file(key, value):
    with open('./workspace/config/config_runtime.json') as config_runtime_file:
        config_runtime_file_contents = json.load(config_runtime_file)
        config_runtime_file_contents[key] = value
    return config_runtime_file_contents


def set_android_decompiling_tool(decompiling_tool):
    write_config_runtime_file("androidDecompilingTool", decompiling_tool)


def set_ios_decompiling_tool(decompiling_tool):
    write_config_runtime_file("iosDecompilingTool", decompiling_tool)


def get_global_mobile_bounty_hunter_report_file_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["globalMobileBountyHunterReportFileRelativePath"]


def get_dedicated_mobile_bounty_hunter_report_file_name():
    config_file_json = read_config_runtime_file()
    return config_file_json["dedicatedMobileBountyHunterReportFileName"]


def get_dedicated_mobile_bounty_hunter_report_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["dedicatedMobileBountyHunterReportDirectoryRelativePath"]


def get_android_store_urls_list_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidStoreUrlsListRelativePath"]


def get_android_application_package_name_list_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidApplicationPackageNameListRelativePath"]


def get_ios_application_package_name_list_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosApplicationPackageNameListRelativePath"]


def get_android_decompiling_tool():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidDecompilingTool"]


def get_android_input_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidInputDirectoryRelativePath"]


def get_android_input_analyzed_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidInputAnalyzedDirectoryRelativePath"]


def get_android_output_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidOutputDirectoryRelativePath"]


def get_android_output_analyzed_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidOutputAnalyzedDirectoryRelativePath"]


def get_ios_store_urls_list_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosStoreUrlsListRelativePath"]


def get_ios_input_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosInputDirectoryRelativePath"]


def get_ios_input_analyzed_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosInputAnalyzedDirectoryRelativePath"]


def get_ios_output_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosOutputDirectoryRelativePath"]


def get_ios_output_analyzed_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosOutputAnalyzedDirectoryRelativePath"]