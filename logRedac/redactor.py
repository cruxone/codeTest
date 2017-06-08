import sys
import gzip
import shutil
import re


def copyFile(srcFile):
    dstFile = srcFile + '.redact.gz'
    shutil.copy2(srcFile, dstFile)
    print("New file is: {}".format(dstFile))
    try:
        gunzipFile(dstFile)
        print("copy successful")
    except:
        print("failed to copy")

def gunzipFile(log):
    # will gunzip file, and then call redact with gunzipped file.
    regex = r"\d{3}-\d{2}-\d{4}"
    # open file in read mode to grab contents
    openFile = gzip.open(log, 'rb')
    contents = openFile.readlines()
    # close read file
    openFile.close()
    # open file in write mode
    openFile = gzip.open(log, 'w')
    # sort through contents
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

#def redact(line, counter):
    #will redact documents and log
    # FOR LOGGING: log name of file redacted, total lines, and lines redacted
    #print("redact called", counter)


def main():
    param = sys.argv
    try:
        if param[1]:
            copyFile(param[1])
    except:
        print("Incorrect parameters")

main()
