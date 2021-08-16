import os
from boom import Explode

inPath = "./in/"
outPath = "./out/"

if not os.path.exists(inPath):
    print("Directory {0} doesn't exist".format(inPath))
    exit(1)

if not os.path.exists(outPath):
    os.makedirs(outPath)

ext = ('.png')
for f in os.listdir(inPath):
    if f.endswith(ext):
        path = "{0}{1}".format(inPath, f)
        Explode(os.path.splitext(f)[0], path, outPath)  
    else:
        print("Ignoring unsupported extension {0}".format(f))
        continue