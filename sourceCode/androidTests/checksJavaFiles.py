import pathlib
from sourceCode.reporting import report
from sourceCode.reporting import reportEnums

def findJavaScriptEnabled(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + "/" + "smali" + "/"
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    print(applicationDirectoryPathLib)
    javaFilesList = [f for f in applicationDirectoryPathLib.rglob("*.smali") if f.is_file()]

    if len(javaFilesList) > 0:

        for javaFilePath in javaFilesList:
            with open(javaFilePath, "r") as f:
                content = f.read()
                if "setjavascriptenabled" in content.lower():
                    report.reportStatusToVerifyWithoutTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, str(javaFilePath), "JavaScriptEnabled")
                    report.copyFileToDedicatedReportDirectory(str(javaFilePath), OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)

    else:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "JavaScriptEnabled")