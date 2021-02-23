import os, sys

args = sys.argv[1] if len(sys.argv) > 1 else None


def main():

    if args != None: 
        ls = os.listdir(args) 
        for i, l in enumerate(ls): # l is the item iterated, i is the iteration index
            if i != len(ls) - 1:
                print(l)
            else:
                print(l, end="")

    else: 
        ls = os.listdir(os.getcwd())
        for i, l in enumerate(ls):
            print(l)



if __name__ == "__main__":
    main()