
import sys

def permutate(toPerm):
    #check if length of string is viable for iteration, if so return list
    if len(toPerm) == 1:
        return toPerm
    # grab first letter of string
    firstChar = toPerm[0]
    # grab all letters after first string
    permutations = permutate(toPerm[1:])
    # list to contain unique permutations
    possible = []
    #print(permutations)
    for perm in permutations:
        #print(perm)
        for i in range(len(perm)+1):
            newPerm = perm[:i] + firstChar + perm[i:]
            if newPerm not in possible:
                possible.append(newPerm)
    return possible


def main():
    args = sys.argv
    try:
        if args[1]:
            print(permutate(args[1]))
    except:
        print("Please supply an argument")
main()
