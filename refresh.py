import os, sys
import shutil

f = open("list")

dst = "patch"
src = "../gecko-dev"
for line in f:
    pos = line.rfind("/")
    end = -1
    file_name = line[pos + 1:end]
    print file_name
    print (src + line[:end], dst + '/' + file_name)
    shutil.copy(src + line[:end], dst + '/' + file_name)
