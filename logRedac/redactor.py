import sys
import gzip
import shutil
import re
import io


def gunzipFile(srcFile):
    # will gunzip file, and then call redact with gunzipped file.
    # regex for SSN
    try:
        regex = re.compile(b"\d{3}-\d{2}-\d{4}")
        print("Opened " + srcFile)
        dstFile = srcFile + '.redact.gz'
        # count of all lines in log file
        totalCount = 0
        # count of redacted lines
        redactCount = 0
        gunzipped = gzip.open(srcFile, 'rb')
        # read in src file, io.BufferedReader offers better performance than gzip.open()
        f = io.BufferedReader(gunzipped)
        with gzip.open(dstFile, 'wb') as redactedFile:
            #with gzip.open(dstFile, 'wb') as r:
            for line in f:
                # if the search term is not found, the line will be written to the new file.
                totalCount = totalCount + 1
                socialMatch = re.search(regex, line)
                # if a match is not found, the file will be written to the new file
                if not socialMatch:
                    redactedFile.write(line)
                else:
                    redactCount = redactCount + 1
        print("Closed " + srcFile)
        # send src file, and counts to log function
        logger(srcFile, totalCount, redactCount)
    except:
        print("Error in ")


def logger(srcFile, totalCount, redactCount):
# writes an appended log file containing line counts and src file for each entry
    with open("redact.log", 'a+') as logFile:
        logFile.write("File redacted: {}\n".format(srcFile))
        logFile.write("Total lines: {}\n".format(totalCount))
        logFile.write("Lines redacted: {}\n-----------------------\n".format(redactCount))



def main():
    param = sys.argv
    try:
        directory = param[1]
        filesToFilter = param[2:]
        for item in filesToFilter:
            toProcess = directory + item
            gunzipFile(toProcess)
    except:
        print("Incorrect parameters." +
        "\nParameters are root directory of logs and then each file like so (note the trailing / in the directory):" +
        " ~/Desktop/Logs/ log1.log.gz log2.log.gz")

main()
