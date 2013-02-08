#!/usr/bin/python


# contentPush
# Author: Brent Ryczak 
#
# This short python file takes the entire contents of one folder 
# and simply copies them into another. My purpose of this code is
# to work in a workspace on my website, and once I am ready to
# push the updated site online, I'll run this code to move the 
# contents. 

import shutil
import os
import sys

newdir = []
class contentPush:

    def pushFiles(self, dir, dest):
        global newdir
        localdir = []
        for file in os.listdir(dir):
            path = os.path.join(dir, file)
            if os.path.isfile(path):
                print("Copied file: " + path)
                newdir.append(path)
            elif os.path.isdir(path):
                newdir.append(path)
                localdir.append(path)
        for f in localdir:
            self.pushFiles(f, "")
        print("\n\n")

    def listContents(self):
        for each in newdir:
            print(each)

    def writeFiles(self, src, dest):
        copybuffer = []
        for each in newdir:
            print(dest + each[len(src):])
            if os.path.isdir(each):
                print(os.path.isdir(dest + each[len(src):]))
                if not os.path.exists(dest + each[len(src):]): 
                    os.makedirs(dest + each[len(src):])
        for each in newdir:
            if os.path.isfile(each):
                shutil.copy(each, dest + each[len(src):])

            
cp = contentPush()
from os.path import expanduser
home = expanduser("~")
print(home)
if os.path.exists(home + "/Documents/contentPushData"):
    print "/n/nenter 'yes' to use previous locations:"
    #data = sys.stdin.readline()[:-1]
    f = open (home + "/Documents/contentPushData/log.log", "r")
    src = f.readline()
    dest = f.readline()
    print "Source: " + src
    print "Destination: " + dest
    print("\'yes\' or \'no\'")
    answer = sys.stdin.readline()
    print "answer"
    #cp.pushFiles(sys.argv[1], sys.argv[2])
    #cp.writeFiles(sys.argv[1], sys.argv[2])
else:
    os.makedirs(home + "/Documents/contentPushData")
    f = open(home + "/Documents/contentPushData/log.log", "rw")
    f.write(' ')
    f.close()
if len(sys.argv) < 3:
    print("Usage: python contentPush.py <source folder abs. path> <destination folder abs. path>")
    print("--OR--")
    print(": ")
else:
    cp.pushFiles(sys.argv[1], sys.argv[2])
    cp.writeFiles(sys.argv[1], sys.argv[2])
