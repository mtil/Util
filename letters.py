from os.path import exists

def networkDriveLetterTumbler():
    usedLetters = []
    unusedLetters = []
    for drive in range(ord('A'), ord('Z')):
        if exists(chr(drive) + ':') is True:
            usedLetters.append(chr(drive))
        if exists(chr(drive) + ':') is False:
            unusedLetters.append(chr(drive))

    return unusedLetters[0]

networkDriveLetterTumbler()