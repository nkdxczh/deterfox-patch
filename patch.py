import os, sys
import shutil

f = open("list")

src = "patch"
dst = "../gecko-dev"
for line in f:
    pos = line.rfind("/")
    end = -1
    #src = "patch"
    #dst = "gecko-dev"
    file_name = line[pos + 1:end]
    print file_name
    print (file_name, dst + line[:end])
    shutil.copy(src + '/' + file_name, dst + line[:end])
