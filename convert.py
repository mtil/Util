import subprocess
from postprocessing import LAST_WORKLOAD
from postprocessing import LAST_DIR



def convertDatToTXT():

    print('Converting UKLog.dat to text file.')
    subprocess.call(r'GuCLogConverter.exe -d' + LAST_WORKLOAD + 'UKLog.dat' '-t' + LAST_DIR + '-c raw') #exe needs file location

