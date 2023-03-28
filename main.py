# from modules.environment import *
from modules.thirdPartySoftware import installThirdPartySoftware
from modules.directories import createDirectories
from modules.applicationManager import runAnalyzeApplicationFromDeveloperProfileList

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

    opts, args = getopt.getopt(argv,"hf:i:o:l:p:u:",["apkFile=", "inputDirectory=", "outputDirectory=", "apksListFile=", "developersUrlsProfileFile=", "storeUrl="])
   
    for opt, arg in opts:
        if opt == '-h':
            print ('main.py -h [help] -a [all] -f <apkFile> -i <inputDirectory> -u <urlToStore>')
            sys.exit()
        elif opt in ("-f", "--apkFile"):
            APK_FILE = arg
        elif opt in ("-i", "--inputDirectory"):
            INPUT_DIRECTORY_PATH = arg
        elif opt in ("-o", "--outputDirectory"):
            OUTPUT_DIRECTORY_PATH = arg
        elif opt in ("-l", "--apksListFile"):
            APPLICATION_LIST_FILE_PATH = arg
        elif opt in ("-p", "--developersUrlsProfileFile"):
            DEVELOPERS_URLS_PROFILE_FILE = arg
        elif opt in ("-u", "--storeUrl"):
            STORE_URL = arg

    installThirdPartySoftware()
    createDirectories(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)
    runAnalyzeApplicationFromDeveloperProfileList(DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)

if __name__ == '__main__':
    main(sys.argv[1:])