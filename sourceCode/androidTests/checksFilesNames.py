from termcolor import colored
import pathlib
from sourceCode.reporting import report
from sourceCode.reporting import reportEnums

# Any file with extension .sqlite or .db

def searchFilesWithSqliteExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, RESULT_FILE_PATH):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    sqliteFilesList = list(applicationDirectoryPathLib.rglob("*.sqlite"))
    
    if(len(sqliteFilesList) > 0):

        for sqliteFilePath in sqliteFilesList:

            report.reportStatusToVerifyWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "Sqlite database", sqliteFilePath)
            report.copyFileToDedicatedReportDirectory(sqliteFilePath, OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)

    else:
        report.reportStatusNotFoundWithoutTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "Sqlite database")
        

def searchFilesWithDbExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, RESULT_FILE_PATH):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    dbFilesList = list(applicationDirectoryPathLib.rglob("*.db"))

    if(len(dbFilesList) > 0):

        for dbFilePath in dbFilesList:

            report.reportStatusToVerifyWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "DB database", dbFilePath)
            report.copyFileToDedicatedReportDirectory(dbFilePath, OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)

    else:
        report.reportStatusNotFoundWithoutTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "DB database")


def searchConfigFilesWithAnyExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, RESULT_FILE_PATH):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    configFilesList = list(applicationDirectoryPathLib.rglob("*config*"))

    if(len(configFilesList) > 0):

        for configFileList in configFilesList:
            report.reportStatusToVerifyWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "Config file", str(configFileList))
            report.copyFileToDedicatedReportDirectory(str(configFileList), OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)

    else:
        report.reportStatusNotFoundWithoutTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "", "Config file")