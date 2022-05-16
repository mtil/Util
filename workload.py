import os
import subprocess
import time
import postprocessing

def GuCsocWatch():
    socwatchDefaultTime = 20
    socOutput = 'c:/results/currentrun/'

    subprocess.call(r'%systemdrive%/users/%username%/Desktop/socwatch/socwatch.exe -t' + socwatchDefaultTime + '-f cpu -f sstate -o' + socOutput, shell=True)
    time.sleep(1.5) #starts collecting socwatch datat before guc - guc takes ~10 seconds
    subprocess.call(r'%systemdrive%/users/%username%/Desktop/GucPerfLog/StartLogging.bat', shell=True)

    postprocessing.finishedWorkload()