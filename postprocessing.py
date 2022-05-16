import os
from util import updateTime
import util
import glob
from mapnetwork import NETWORK_SHARE
import time
import subprocess

LAST_WORKLOAD = ''
LAST_DIR = ''

def finishedWorkload():
    print('Finished workload, transfering results to server.')
    currentRun = 'c:/results/currentrun'
    os.mkdir('c:/results/GuC/_' + util.CURRENT_DATE + '_' + updateTime()) #add folder with date and time
    os.rename(currentRun, 'c:/results/GuC/_' + util.CURRENT_DATE + '_' + updateTime()) #moves last run data to new folder
    lastDir = max(glob.glob(os.path.join('c:/results/Guc/', '*/')), key=os.path.getmtime).rstrip('\\') #finds last folder made
    LAST_DIR = lastDir  #moving to global
    LAST_WORKLOAD = NETWORK_SHARE + lastDir #moving to global
    xferToShare(lastDir) #prep for network move

def xferToShare(dirToMove):
    print('Moving files to network.')
    os.rename(dirToMove, NETWORK_SHARE)
    time.sleep(60) #pasuses script for xfer, probably needed for dat to txt conversion, timing
    convertDatToTXT()

def convertDatToTXT():
    print('Converting UKLog.dat to text file.')
    subprocess.call(r'GuCLogConverter.exe -d' + LAST_WORKLOAD + 'UKLog.dat' '-t' + LAST_DIR + '-c raw')  # exe needs file location
