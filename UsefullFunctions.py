from PIL import Image
import random
import numpy as np

### Secret Key File Creation ###
def CreateSecretKeyFile():
    try:
        SecretKey = []
        fileReader = [line.rstrip('\n') for line in open("secretKey")]
        for lines in fileReader:
            keys = str(lines).split(' ')
            keys = [int(key) for key in keys]
            SecretKey.append(keys)
        return np.array(SecretKey)
    except IOError:
        print("File not created, creatig file.")
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
        #secretKey = list(chunks(randStack,16))
        print("Secret Length :", len(secretKey) * len(secretKey[0]))

        np.savetxt("secretKey", secretKey, fmt="%d")
        return secretKey


### Playfair Secret Image Change
def WhatWeDo(indexA, indexB, secretKey):
    if indexA[0] == indexB[0]:  # Aynı Line
        return (secretKey[indexA[0],(indexA[1]+1)%16], secretKey[indexB[0],(indexB[1]+1)%16])
    if indexA[1] == indexB[1]:  # Aynı Column
        return (secretKey[(indexA[0]+1)%16,indexA[1]],secretKey[(indexB[0]+1)%16,indexB[1]])
    else:                       # Köşegen
        return (secretKey[indexA[0],indexB[1]],secretKey[indexB[0],indexA[1]])


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