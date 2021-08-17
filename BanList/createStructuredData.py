import sys

# Gets the parameter if it exists. Otherwise return None
# parameterToGet = parameter needed to be obtained.
def getParameter(parameterToGet):
    # check the total number of records in the args.
    if len(sys.argv) >= parameterToGet + 1:
        return sys.argv[parameterToGet]
    else:
        return None

# Gets the data from the file.
def getDataFromFile(filePath):
    with open(filePath, 'r') as f:
        data = f.read()

    recordsInFile = data.splitlines()
    f.close()

    return recordsInFile

# Updates the ini file that lioranboard pulls for processing.
def updateIniFile(recordsInFile, recordsPerRun, iniFilePath):
    with open(iniFilePath, 'a') as f:
        recordsForRun = ""
        run = 1
        for i in range(len(recordsInFile)):
            if i > 0 and i % recordsPerRun == 0:
                recordsForRun = recordsForRun[:-1]
                f.write('run_' + str(run) + '="' + recordsForRun + '"\n')
                recordsForRun = ""
                run += 1
            else:
                recordsForRun += recordsInFile[i] + ','

    f.close()

# The file path for the text file.
filePath = getParameter(1)
# The file path for the ini file used by lioranboard.
iniFilePath = getParameter(2)
# The number of records you want to process at a time.
recordsPerRun = int(getParameter(3))

recordsInFile = getDataFromFile(filePath)
updateIniFile = updateIniFile(recordsInFile, recordsPerRun, iniFilePath)