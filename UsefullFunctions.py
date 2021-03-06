from PIL import Image
import random
import numpy as np
from os import system, name

### Secret Key File Creating ###
def CreateSecretKeyFile():
    stack = []
    for x in range(256):
        stack.append(x)

    randStack = []
    while (len(stack) != 0):
        a = random.choice(stack)
        randStack.append(a)
        stack.remove(a)

    secretKey = np.array(randStack)
    secretKey = np.reshape(randStack, (16, 16))
    # secretKey = list(chunks(randStack,16))
    print("Secret Length :", len(secretKey) * len(secretKey[0]))

    np.savetxt("secretKey", secretKey, fmt="%d")
    return secretKey

### Secret Key File Loading ###
def LoadSecretKeyFile():
    try:
        SecretKey = []
        fileReader = [line.rstrip('\n') for line in open("secretKey")]
        for lines in fileReader:
            keys = str(lines).split(' ')
            keys = [int(key) for key in keys]
            SecretKey.append(keys)
        return np.array(SecretKey)
    except IOError:
        print("File not found, creatig file.")
        return CreateSecretKeyFile()

### Find The PlainImage ###
def FindThePlainImage():
    try:
        Path = input("Enter the file location with name : ")
        PlainImage = Image.open(Path, mode='r')
        return PlainImage
    except IOError:
        print("File not found, please try again.")
        FindThePlainImage()

### Find The SecretImage ###
def FindTheSecretImage():
    try:
        Path = "converted/secret.bmp"
        SecretImage = Image.open(Path, mode='r')
        return SecretImage
    except IOError:
        print("File not found, please create secret image.")

### Clear Terminal ###
def ClearScreen():
        # for windows
        if name == 'nt':
            _ = system('cls')
            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

# Print iterations progress
def PrintProgressBar (iteration, total, prefix ='', suffix ='', decimals = 1, length = 100, fill ='█', printEnd ="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

### Split Array to N pieces ###
def Chunks(l, n):                   # Create a function called "chunks" with two arguments, l and n:
    for i in range(0, len(l), n):   # For item i in a range that is a length of l,
        yield l[i:i+n]              # Create an index range for l of n items:

### Find Index In 2D Lists ###
def Find2dListIndex(List, Item):
    for i, Items in enumerate(List):
        if Item in Items:
            return (i, Items.index(Item))