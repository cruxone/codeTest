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
    print("gunzip called")
    regex = r"\d{3}-\d{2}-\d{4}"
    counter = 0
    redactCount = 0
    openFile = gzip.open(log, 'rb')
    contents = openFile.readlines()
    openFile.close()
    openFile = gzip.open(log, 'w')
    for line in contents:
        socialMatch = re.search(regex, line)
        if not socialMatch:
            openFile.write(line)
        else:
            counter = counter + 1
    print("sensitive data found: {} times.".format(counter))
    #openFile.close()

    # with gzip.open(log, 'rb') as f:
    #     for line in f.readlines():
    #         counter = counter + 1
    #         socialMatch = re.search("Fred", line)
    #         #socialReplace = re.sub(EX, 'xxx-xxx-xxxx', line)
    #         if socialMatch:
    #             redactCount = redactCount + 1
    #             print("Fred found")
    #     print(redactCount)
    #     print(counter)
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
