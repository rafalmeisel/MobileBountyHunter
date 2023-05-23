import pathlib
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus
from source_code.config_file_manager import get_android_output_directory_relative_path
from source_code.config_file_manager import get_dedicated_mobile_bounty_hunter_report_directory_relative_path
from source_code.config_file_manager import get_dedicated_mobile_bounty_hunter_report_file_name
import re

application_package_system = "Android"

def check_exported_activity_with_java_script_enabled(application_package_name):
    
    # From: pl.application.apk: AndroidManifest: exported: activity:pl.app.ChatActivity: FOUND!
    # Find: ChatActivity

    exported_activity_from_report_regex = r'exported.*(\.(?=[^.]*$))(.*):'
    java_script_enabled_activity_from_report_regex = r'(\/(?=[^/]*$))(.*).java: JavaScriptEnabled'

    exported_activity_list = []
    java_script_enabled_activity_list = []

    dedicated_report_file_path = pathlib.Path(get_android_output_directory_relative_path(), application_package_name, get_dedicated_mobile_bounty_hunter_report_directory_relative_path(), get_dedicated_mobile_bounty_hunter_report_file_name())
    report_file_content = open(dedicated_report_file_path, "r").readlines()

    for line in report_file_content:
        if re.search(exported_activity_from_report_regex, line):
            exportedActivityName = re.search(exported_activity_from_report_regex, line).group(2)
            exported_activity_list.append(exportedActivityName)
    
    for line in report_file_content:
        if re.search(java_script_enabled_activity_from_report_regex, line):
            javaScriptEnabledActivityName = re.search(java_script_enabled_activity_from_report_regex, line)
            java_script_enabled_activity_list.append(javaScriptEnabledActivityName)

    commonActivities = set(exported_activity_list) & set(java_script_enabled_activity_list)

    for activityName in commonActivities:
        report_issue(application_package_system, application_package_name, "Report", IssueSeverity.MEDIUM, IssueStatus.VULNERABLE, "Exported + JavaScriptEnabled", activityName)
        # report_status_vulnerable_with_token_value("Android", application_package_name, "Report", "Exported + JavaScriptEnabled", activityName)

    if len(commonActivities) == 0:
        report_issue(application_package_system, application_package_name, "Report", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Export with JavaScriptEnabled", "")
        # report_status_not_found("Android", application_package_name, "Report", "Export with JavaScriptEnabled")