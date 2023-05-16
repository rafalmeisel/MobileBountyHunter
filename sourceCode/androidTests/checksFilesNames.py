from termcolor import colored
import pathlib
from sourceCode.reporting import report
from sourceCode.reporting import reportEnums

# Any file with extension .sqlite or .db

def searchFilesWithSqliteExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    sqliteFilesList = [f for f in applicationDirectoryPathLib.rglob("*.sqlite") if f.is_file()]

    if len(sqliteFilesList) > 0:

        for sqliteFilePath in sqliteFilesList:

            report.reportStatusToVerifyWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "Sqlite database", sqliteFilePath)
            report.copyFileToDedicatedReportDirectory(sqliteFilePath, OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)

    else:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "Sqlite database")
        

def searchFilesWithDbExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)

    dbFilesList = [f for f in applicationDirectoryPathLib.rglob("*.db") if f.is_file()]

    if len(dbFilesList) > 0:
        for dbFilePath in dbFilesList:

            report.reportStatusToVerifyWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "DB database", dbFilePath)
            report.copyFileToDedicatedReportDirectory(dbFilePath, OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)

    else:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "DB database")


def searchConfigFilesWithAnyExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    configFilesList = [f for f in applicationDirectoryPathLib.rglob("*config*") if f.is_file()]
    
    if len(configFilesList) > 0:

        for configFileList in configFilesList:
            report.reportStatusToVerifyWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "Config file", str(configFileList))
            report.copyFileToDedicatedReportDirectory(str(configFileList), OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)

    else:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "Config file")