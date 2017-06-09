import sys
import gzip
import shutil
import re


def copyFile(srcFile):
    dstFile = srcFile + '.redact.gz'
    # copying source file, copies permissions and most metadata
    shutil.copy2(srcFile, dstFile)
    print("New file is: {}".format(dstFile))
    try:
        gunzipFile(dstFile)
        print("copy successful")
    except:
        print("failed to copy")

def gunzipFile(log):
    # will gunzip file, and then call redact with gunzipped file.
    # regex for SSN
    regex = r"\d{3}-\d{2}-\d{4}"
    # open file in read mode to grab contents
    openFile = gzip.open(log, 'rb')
    print("opened " + log)
    contents = openFile.readlines()
    # close read file
    openFile.close()
    # open file in write mode
    openFile = gzip.open(log, 'w')
    # sort through contents
    counter = 0
    for line in contents:
        # if the search term is not found, the line will be written to the new file.
        # This takes care of duplicates in the same line as well.
        socialMatch = re.search(regex, line)
        if not socialMatch:
            openFile.write(line)
        else:
            counter = counter + 1
    print("sensitive data found: {} times.".format(counter))
    # close write mode file
    openFile.close()
    print("closed " + log)

def main():
    param = sys.argv
    try:
        directory = param[1]
        count = 0
        filesToFilter = param[2:]
        for item in filesToFilter:
            toProcess = directory + item
            copyFile(toProcess)
    except:
        print("Incorrect parameters")

main()
