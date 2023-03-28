# from modules.environment import *
from modules.thirdPartySoftware import installThirdPartySoftware
from modules.directories import createDirectories
import modules.applicationManager

import sys
import getopt

# Parameters:
# -h / help - show help
# -f / apkFile - analyze specified application file
# -i / inputDirectory - analyze all applications in input
# -o / outputDirectory - output directory
# -l / apksListFile - analyze application listed in file
# -p / developersUrlsProfileFile - analyze applications from developers urls
# -u / storeUrl - analyze specified URL - can be url to specified android/ios apk, specified android/ios developer

def main(argv):
    
    USER_CHOICE=""
    INPUT_DIRECTORY_PATH = "./workspace/input/"
    INPUT_ANALYZED_DIRECTORY_PATH = "./workspace/input_analyzed/"
    OUTPUT_DIRECTORY_PATH = "./workspace/output/"
    OUTPUT_ANALYZED_DIRECTORY_PATH = "./workspace/output_analyzed/"
    RESULT_FILE_PATH = "./workspace/results.txt"
    APPLICATION_LIST_FILE_PATH = "./workspace/apksList.txt"
    DEVELOPERS_URLS_PROFILE_FILE = "./workspace/developersUrlsProfile.txt"
    APK_FILE = ""
    STORE_URL = ""


    print("APPLICATION_LIST_FILE_PATH" + APPLICATION_LIST_FILE_PATH)
    print("DEVELOPERS_URLS_PROFILE_FILE" + DEVELOPERS_URLS_PROFILE_FILE)

    opts, args = getopt.getopt(argv,"hf:iolpu:",["apkFile=", "inputDirectory=", "outputDirectory=", "apksListFile=", "developersUrlsProfileFile=", "storeUrl="])
   
    for opt, arg in opts:
        if opt == '-h':
            print ('main.py -h [help] -a [all] -f <apkFile> -i <inputDirectory> -u <urlToStore>')
            sys.exit()

        elif opt in ("-f", "--apkFile"):
            if len(arg)>0:
                APK_FILE = arg
            USER_CHOICE="apkFile"

        elif opt in ("-i", "--inputDirectory"):
            if len(arg)>0:
                INPUT_DIRECTORY_PATH = arg
            USER_CHOICE="inputDirectory"

        elif opt in ("-o", "--outputDirectory"):
            if len(arg)>0:
                OUTPUT_DIRECTORY_PATH = arg
            USER_CHOICE="outputDirectory"

        elif opt in ("-l", "--apksListFile"):
            if len(arg)>0:
                APPLICATION_LIST_FILE_PATH = arg
            USER_CHOICE="apksListFile"

        elif opt in ("-p", "--developersUrlsProfileFile"):
            if len(arg)>0:
                DEVELOPERS_URLS_PROFILE_FILE = arg
            USER_CHOICE="developersUrlsProfileFile"
            
        elif opt in ("-u", "--storeUrl"):
            if len(arg)>0:
                STORE_URL = arg
            USER_CHOICE="storeUrl"

    installThirdPartySoftware()
    createDirectories(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)

    # TODO: 
    # When running application as "inputDirectory", "outputDirectory", GooglePlay/AppStore application flag is not set (currently only for URLs).
    # What needs to do: Determine if application is GooglePlay or AppStore earlier.

    match USER_CHOICE:
        case "apkFile":
            print("Analyze selected apkFile. Will be added later.")

        case "inputDirectory":
            print("Analyze selected inputDirectory")
            modules.applicationManager.analyzeInputDirectory(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)

        case "outputDirectory":
            print("Analyze selected outputDirectory")
            modules.applicationManager.analyzeOutputDirectory(OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)

        case "apksListFile":
            print("Analyze selected apksListFile")
            modules.applicationManager.analyzeApplicationFromList(APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)

        case "developersUrlsProfileFile":
            print("Analyze selected developersUrlsProfileFile")
            modules.applicationManager.runAnalyzeApplicationFromDeveloperProfileList(DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)

        case "storeUrl":
            print("Analyze selected storeUrl. Will be added later.")

        case _:
            print("Default")

    

if __name__ == '__main__':
    main(sys.argv[1:])