import os

# Checks to see if results folder is in root of C:
# Makes results
def resultsDirCheck():
    if os.path.exists('c:/results/GuC/'):
        print('GuC Result Path Exists!')
    else:
        os.mkdir('c:/results/')
        os.mkdir('c:/results/GuC') #Windows won't let you make a full path
        os.mkdir('c:/results/currentrun') #Temp directory for current run
