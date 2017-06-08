import sys
import gzip
import re


def copyFile():
    #called by main(), will copy file then send new file to gunzipFile()
    print("cp called")
    logToRedact = "test"
    gunzipFile(logToRedact)

def gunzipFile(log):
    # will gunzip file, and then call redact with gunzipped file.
    print("gunzip called")
    redact()

def redact():
    #will redact documents and log
    # FOR LOGGING: log name of file redacted, total lines, and lines redacted
    print("redact called")

def openFile(filePath):
    try:
        f = open(filePath, 'r')
        contents = f.readlines()
        count = 0
        #print(contents)
        for line in contents:

            socialMatch = re.search("Fred", line)
            #socialReplace = re.sub(EX, 'xxx-xxx-xxxx', line)
            #print(line)
            if socialMatch:
                count = count + 1
                #print(socialMatch.group())
        print(count)
    except:
        print("error reading file")

def main():
    param = sys.argv
    try:
        if param[1]:
            print("Argument supplied: {}".format(param[1]))
            # copy file
            copyFile(param[1])
    except:
        print("Incorrect parameters")

main()
