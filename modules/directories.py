import os

def createInputDirectory(INPUT_DIRECTORY_PATH):
    
    if not os.path.exists(INPUT_DIRECTORY_PATH):
        os.makedirs(INPUT_DIRECTORY_PATH)
        os.chmod(INPUT_DIRECTORY_PATH, 0o766)
        print("Created directory: " + INPUT_DIRECTORY_PATH)        

def createOutputDirectory(OUTPUT_DIRECTORY_PATH):
    
    if not os.path.exists(OUTPUT_DIRECTORY_PATH):
        os.makedirs(OUTPUT_DIRECTORY_PATH)
        os.chmod(OUTPUT_DIRECTORY_PATH, 0o766)
        print("Created directory: " + OUTPUT_DIRECTORY_PATH)
        
def createInputAnalyzedDirectory(INPUT_ANALYZED_DIRECTORY_PATH):
    
    if not os.path.exists(INPUT_ANALYZED_DIRECTORY_PATH):
        os.makedirs(INPUT_ANALYZED_DIRECTORY_PATH)
        os.chmod(INPUT_ANALYZED_DIRECTORY_PATH, 0o766)
        print("Created directory: " + INPUT_ANALYZED_DIRECTORY_PATH)

def createOutputAnalyzedDirectory(OUTPUT_ANALYZED_DIRECTORY_PATH):
    
    if not os.path.exists(OUTPUT_ANALYZED_DIRECTORY_PATH):
        os.makedirs(OUTPUT_ANALYZED_DIRECTORY_PATH)
        os.chmod(OUTPUT_ANALYZED_DIRECTORY_PATH, 0o766)
        print("Created directory: " + OUTPUT_ANALYZED_DIRECTORY_PATH)

def createResultFile(RESULT_FILE_PATH):
    
    if not os.path.exists(RESULT_FILE_PATH):
        f = open(RESULT_FILE_PATH, "x")
        os.chmod(RESULT_FILE_PATH, 0o766)
        print("Created file: " + RESULT_FILE_PATH)

def createDeveloperProfileUrlsFile(DEVELOPERS_URLS_PROFILE_FILE):

    if not os.path.exists(DEVELOPERS_URLS_PROFILE_FILE):
        f = open(DEVELOPERS_URLS_PROFILE_FILE, "r")
        os.chmod(DEVELOPERS_URLS_PROFILE_FILE, 0o766)
        print("Created file: " + DEVELOPERS_URLS_PROFILE_FILE + " - Please provide the Developers Urls from Google Play in this file.")

def createApplicationListFile(APPLICATION_LIST_FILE_PATH):

    if not os.path.exists(APPLICATION_LIST_FILE_PATH):
        f = open(APPLICATION_LIST_FILE_PATH, "r")
        os.chmod(APPLICATION_LIST_FILE_PATH, 0o766)
        print("Created file: " + APPLICATION_LIST_FILE_PATH + " - Please provide the list with Application Package Names in this file.")

def createDeveloperProfileUrlsFile(DEVELOPERS_URLS_PROFILE_FILE):

    if not os.path.exists(DEVELOPERS_URLS_PROFILE_FILE):
        f = open(DEVELOPERS_URLS_PROFILE_FILE, "r")
        os.chmod(DEVELOPERS_URLS_PROFILE_FILE, 0o766)
        print("Created file: " + DEVELOPERS_URLS_PROFILE_FILE + " - Please provide the Developers Urls in this file.")

def clearResultFile(RESULT_FILE_PATH):

    resultFile = open(RESULT_FILE_PATH, "r+")
    resultFile.truncate(0)
    resultFile.close()

def clearApplicationListFile(APPLICATION_LIST_FILE):

    resultFile = open(APPLICATION_LIST_FILE, "r+")
    resultFile.truncate(0)
    resultFile.close()
    
def createDirectories(DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)

    createDeveloperProfileUrlsFile(DEVELOPERS_URLS_PROFILE_FILE)
    createApplicationListFile(APPLICATION_LIST_FILE_PATH)
    createInputDirectory(INPUT_DIRECTORY_PATH)
    createInputAnalyzedDirectory(INPUT_ANALYZED_DIRECTORY_PATH)
    createOutputDirectory(OUTPUT_DIRECTORY_PATH)
    createOutputAnalyzedDirectory(OUTPUT_ANALYZED_DIRECTORY_PATH)
    createResultFile(RESULT_FILE_PATH)
