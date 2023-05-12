from termcolor import colored
import pathlib

# Any file with extension .sqlite or .db

def searchFilesWithSqliteExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, RESULT_FILE_PATH):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    sqliteFilesList = list(applicationDirectoryPathLib.rglob("*.sqlite"))
    
    resultFile = open(RESULT_FILE_PATH, "a")

    if(len(sqliteFilesList) > 0):

        for sqliteFilePath in sqliteFilesList:
            print(APPLICATION_PACKAGE_NAME + ": Sqlite database: " + colored(str(sqliteFilePath), 'red'))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": Sqlite database: " + str(sqliteFilePath) + "\n")
        
        resultFile.close()

    else:
        print(APPLICATION_PACKAGE_NAME + ": Sqlite database: " + colored("Not found", 'blue'))
        resultFile.write(APPLICATION_PACKAGE_NAME + ": Sqlite database: Not found" + "\n")

def searchFilesWithDbExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, RESULT_FILE_PATH):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    dbFilesList = list(applicationDirectoryPathLib.rglob("*.db"))
    
    resultFile = open(RESULT_FILE_PATH, "a")

    if(len(dbFilesList) > 0):

        for dbFilePath in dbFilesList:
            print(APPLICATION_PACKAGE_NAME + ": DB database: " + colored(str(dbFilePath), 'red'))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": DB database: " + str(dbFilePath) + "\n")
        
        resultFile.close()

    else:
        print(APPLICATION_PACKAGE_NAME + ": DB database: " + colored("Not found", 'blue'))
        resultFile.write(APPLICATION_PACKAGE_NAME + ": DB database: Not found" + "\n")

def searchConfigFilesWithAnyExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, RESULT_FILE_PATH):
    
    applicationDirectoryPath = OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME
    applicationDirectoryPathLib = pathlib.Path(applicationDirectoryPath)
    configFilesList = list(applicationDirectoryPathLib.rglob("*config*"))

    resultFile = open(RESULT_FILE_PATH, "a")

    if(len(configFilesList) > 0):

        for configFileList in configFilesList:
            print(APPLICATION_PACKAGE_NAME + ": Config file: " + colored(str(configFileList), 'red'))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": Config file: " + str(configFileList) + "\n")
        
        resultFile.close()

    else:
        print(APPLICATION_PACKAGE_NAME + ": Config file: " + colored("Not found", 'blue'))
        resultFile.write(APPLICATION_PACKAGE_NAME + ": Config file: Not found" + "\n")