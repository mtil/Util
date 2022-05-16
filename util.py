import datetime

CURRENT_DATE = datetime.datetime.now().strftime("%Y_%m_%d")

# Gives updated time every time called instead of CURRENT_TIME = str(datetime.datetime.now().time()) which just saves
# the time the first time it is called.
def updateTime():
    newtime = str(datetime.datetime.now().time().strftime('%H.%M.%S'))
    print('updateTime call: ' + newtime)
    return newtime


def cleanUpOldFiles():
    if os.path.isfile('c:/UKLog.dat') is True:
        print('UKLog.dat already exists. Renaming to preserve data.')
        os.rename('c:/UKLog.dat', CURRENT_DATE + '_' + updateTime() + '.' + 'c:/results/UKLog.dat')
    else:
        print('No existing files, continuing.')