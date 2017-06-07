
import sys

def perm(toPerm):
    for i in range(len(toPermargLength)):
        print(i)

def main():
    args = sys.argv
    try:
        if args[1]:
            perm(args[1])
    except:
        print("No argument given")

main()
