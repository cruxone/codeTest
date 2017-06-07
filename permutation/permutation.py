
import sys

def permutate(toPerm):
    #check if length of string is viable for iteration, if so return list
    if len(toPerm) <= 1:
        return [toPerm]
    # grab first letter of string
    firstChar = toPerm[0]
    print(firstChar)
    # grab all letters after first string
    permutations = permutate(toPerm[1:])
    print(permutations)

def main():
    args = sys.argv
    print(permutate('LSE'))
    # try:
    #     if args[1]:
    #         print("yus")
    #         perm(args[1])
    #
    # except:
    #     print("No argument given")

main()
