import sys
import gzip
import shutil
import re
import io


def gunzipFile(srcFile):
    # will gunzip file, and then call redact with gunzipped file.
    # regex for SSN
    regex = re.compile(b"\d{3}-\d{2}-\d{4}")
    print("opened " + srcFile)
    dstFile = srcFile + '.redact.gz'
    totalCount = 0
    redactCount = 0
    gunzipped = gzip.open(srcFile, 'rb')
    f = io.BufferedReader(gunzipped)
    with gzip.open(dstFile, 'wb') as r:
        #with gzip.open(dstFile, 'wb') as r:
        for line in f:
            # if the search term is not found, the line will be written to the new file.
            totalCount = totalCount + 1
            socialMatch = re.search(regex, line)
            if not socialMatch:
                r.write(line)
            else:
                redactCount = redactCount + 1
    print("closed " + srcFile)
    logger(srcFile, totalCount, redactCount)


def logger(srcFile, totalCount, redactCount):
# name of each file processed, a count of the total number of lines in log file, count of the total number of lines redacted
# The audit log may additionally contain any other information you feel is pertinent
# The audit log must not contain any information from the redacted lines.
    with open("redact.log", 'a+') as logFile:
        logFile.write("File redacted: {}\n".format(srcFile))
        logFile.write("Total lines: {}\n".format(totalCount))
        logFile.write("Lines redacted: {}\n-----------------------\n".format(redactCount))



def main():
    param = sys.argv
    #try:
    directory = param[1]
    filesToFilter = param[2:]
    for item in filesToFilter:
        toProcess = directory + item
        gunzipFile(toProcess)
    #except:
    #    print("Incorrect parameters")

main()
