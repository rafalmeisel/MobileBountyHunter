import os

def createInputDirectory(INPUT_DIRECTORY_PATH):
    
    if os.path.exists(INPUT_DIRECTORY_PATH):
        print("Detected directory: " + INPUT_DIRECTORY_PATH)
    else:
        os.makedirs(INPUT_DIRECTORY_PATH)
        print("Created directory: " + INPUT_DIRECTORY_PATH)

def createOutputDirectory(OUTPUT_DIRECTORY_PATH):
    
    if os.path.exists(OUTPUT_DIRECTORY_PATH):
        print("Detected directory: " + OUTPUT_DIRECTORY_PATH)
    else:
        os.makedirs(OUTPUT_DIRECTORY_PATH)
        print("Created directory: " + OUTPUT_DIRECTORY_PATH)

def createInputAnalyzedDirectory(INPUT_ANALYZED_DIRECTORY_PATH):
    
    if os.path.exists(INPUT_ANALYZED_DIRECTORY_PATH):
        print("Detected directory: " + INPUT_ANALYZED_DIRECTORY_PATH)
    else:
        os.makedirs(INPUT_ANALYZED_DIRECTORY_PATH)
        print("Created directory: " + INPUT_ANALYZED_DIRECTORY_PATH)

def createOutputAnalyzedDirectory(OUTPUT_ANALYZED_DIRECTORY_PATH):
    
    if os.path.exists(OUTPUT_ANALYZED_DIRECTORY_PATH):
        print("Detected directory: " + OUTPUT_ANALYZED_DIRECTORY_PATH)
    else:
        os.makedirs(OUTPUT_ANALYZED_DIRECTORY_PATH)
        print("Created directory: " + OUTPUT_ANALYZED_DIRECTORY_PATH)

def createResultFile(RESULT_FILE_PATH):
    
    if os.path.exists(RESULT_FILE_PATH):
        print("Detected file: " + RESULT_FILE_PATH)
    else:
        f = open(RESULT_FILE_PATH, "x")
        os.chmod(RESULT_FILE_PATH, 766)
        print("Created file: " + RESULT_FILE_PATH)

def createDirectories(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH):

    createInputDirectory(INPUT_DIRECTORY_PATH)
    createInputAnalyzedDirectory(INPUT_ANALYZED_DIRECTORY_PATH)
    createOutputDirectory(OUTPUT_DIRECTORY_PATH)
    createOutputAnalyzedDirectory(OUTPUT_ANALYZED_DIRECTORY_PATH)
    createResultFile(RESULT_FILE_PATH)
