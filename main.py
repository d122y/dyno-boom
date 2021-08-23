import os
from boom import Explode

def main():
    inPath = "./in/"
    outPath = "./out/"

    if not os.path.exists(inPath):
        print("Directory {0} doesn't exist".format(inPath))
        exit(1)

    if not os.path.exists(outPath):
        os.makedirs(outPath)

    for f in os.listdir(inPath):
        concreteOutPath = "{0}{1}".format(outPath, f)
        if not os.path.exists(concreteOutPath):
            os.makedirs(concreteOutPath)

        concreteInPath = "{0}{1}".format(inPath, f)
        Explode(concreteInPath, concreteOutPath)

if __name__ == "__main__":
    main()