# from modules.environment import *
from modules.environment import prepareEnvironment
from modules.directories import createDirectories

INPUT_DIRECTORY_PATH = "./workspace/input"
INPUT_ANALYZED_DIRECTORY_PATH = "./workspace/input_analyzed"
OUTPUT_DIRECTORY_PATH = "./workspace/output"
OUTPUT_ANALYZED_DIRECTORY_PATH = "./workspace/output_analyzed"
RESULT_FILE_PATH = "./workspace/results.txt"

prepareEnvironment()
createDirectories(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)