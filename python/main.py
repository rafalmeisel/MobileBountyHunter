# from modules.environment import *
from modules.environment import prepareEnvironment
from modules.directories import createDirectories

import sys
import getopt

INPUT_DIRECTORY_PATH = "./workspace/input"
INPUT_ANALYZED_DIRECTORY_PATH = "./workspace/input_analyzed"
OUTPUT_DIRECTORY_PATH = "./workspace/output"
OUTPUT_ANALYZED_DIRECTORY_PATH = "./workspace/output_analyzed"
RESULT_FILE_PATH = "./workspace/results.txt"
APKS_LIST_FILE="./workspace/apksList.txt"
DEVELOPERS_URLS_PROFILE_FILE="./workspace/developersUrls.txt"
APK_FILE=""
STORE_URL=""

# Parameters:
# -h / help - show help
# -f / apkFile - analyze specified application file
# -i / inputDirectory - analyze all applications in input
# -o / outputDirectory - output directory
# -l / apksListFile - analyze application listed in file
# -p / developersUrlsProfileFile - analyze applications from developers urls
# -u / storeUrl - analyze specified URL - can be url to specified android/ios apk, specified android/ios developer

def main(argv):

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
            APKS_LIST_FILE = arg
        elif opt in ("-p", "--developersUrlsProfileFile"):
            DEVELOPERS_URLS_PROFILE_FILE = arg
        elif opt in ("-u", "--storeUrl"):
            STORE_URL = arg

    prepareEnvironment()
    createDirectories(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)


if __name__ == '__main__':
    main(sys.argv[1:])