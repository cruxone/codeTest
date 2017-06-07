import sys
import os

def openFile(filePath):
    try:
        f = open(filePath, 'r')
        contents = f.readlines()
        for line in contents:
            print(line)
    except:
        print("error reading file")

def main():
    param = sys.argv
    try:
        if param[1]:
            print("Argument supplied: {}".format(param[1]))
            openFile("logData.txt")
    except:
        print("Incorrect parameters")

main()
