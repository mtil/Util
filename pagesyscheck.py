import os
import subprocess



def fileSize():
    fileSize = os.path.getsize('c:/pagefile.sys')
    bitDiv = 1024

    fileSizeStripped = (round(fileSize))

    if fileSizeStripped > 3:

        convertToMB(fileSizeStripped)
    else:
        print('nope')

def checkLength():


def convertToMB(fileSize):
    stringSize = str(fileSize)
    print(stringSize)
    length = len(stringSize)
    print(length)
    while length > 3:
        stringSize = int(stringSize) / 1024
        print(round(stringSize))

fileSize()