import pathlib
from sourceCode.reporting import report
from sourceCode.reporting import reportEnums
import re

def checksExportedActivityWithJavaScriptEnabled(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME):
    
    # From: pl.application.apk: AndroidManifest: exported: activity:pl.app.ChatActivity: FOUND!
    # Find: ChatActivity

    exportedActivityFromReportRegex = r'exported.*(\.(?=[^.]*$))(.*):'
    javascriptEnabledActivityFromReportRegex = r'(\/(?=[^/]*$))(.*).java: JavaScriptEnabled'

    exportedActivityList = []
    javaScriptEnabledActivityList = []

    reportFileAbsolutePath = report.getAbsolutePathToDedicatedApplicationReport(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)
    reportFileContent = open(reportFileAbsolutePath, "r").readlines()

    for line in reportFileContent:
        if re.search(exportedActivityFromReportRegex, line):
            exportedActivityName = re.search(exportedActivityFromReportRegex, line).group(2)
            exportedActivityList.append(exportedActivityName)
    
    for line in reportFileContent:
        if re.search(javascriptEnabledActivityFromReportRegex, line):
            javaScriptEnabledActivityName = re.search(javascriptEnabledActivityFromReportRegex, line)
            javaScriptEnabledActivityList.append(javaScriptEnabledActivityName)

    commonActivities = set(exportedActivityList) & set(javaScriptEnabledActivityList)

    for activityName in commonActivities:
        report.reportStatusVulnerableWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "Report", "Exported + JavaScriptEnabled", activityName)

    if len(commonActivities) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "Report", "Export with JavaScriptEnabled")