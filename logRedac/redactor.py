import sys
import gzip
import shutil
import re


def copyFile(srcFile):
    dstFile = srcFile + '.redact'
    shutil.copy2(srcFile, dstFile)
    try:
        gunzipFile(dstFile)
        print("copy successful")
    except:
        print("failed to copy")

def gunzipFile(log):
    # will gunzip file, and then call redact with gunzipped file.
    print("gunzip called")
    counter = 0
    redactCount = 0
    with gzip.open(log, 'rb') as f:
        for line in f.readlines():
            counter = counter + 1
            socialMatch = re.search("Fred", line)
            #socialReplace = re.sub(EX, 'xxx-xxx-xxxx', line)
            if socialMatch:
                redactCount = redactCount + 1
                print("Fred found")
        print(redactCount)
        print(counter)
#def redact(line, counter):
    #will redact documents and log
    # FOR LOGGING: log name of file redacted, total lines, and lines redacted
    #print("redact called", counter)


def main():
    param = sys.argv
    copyFile(param[1])
    try:
        if param[1]:
            print("Argument supplied: {}".format(param[1]))
            # copy file

    except:
        print("Incorrect parameters")

main()
