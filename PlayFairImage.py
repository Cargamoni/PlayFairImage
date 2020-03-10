from PIL import Image
import numpy as np

### Home Made Functions ###
import UsefullFunctions as UsFunc
import ImageOperations as ImgOps
import SecretShareServer as Server
import SecretShareClient as Client

'''
1 - Welcome Message 
2 - Make a SecretKey
3 - Create a Cipher Image
4 - Send Cipher Image
5 - Get Cipher Image
'''


### Welcome Message ###

print('Welcome to the Playfair Image Transferring Program PlayFairImage.')

### Home Made Variables ###
Verticality = False
SquareWidth = 0

### Resimi Açma###
PlainImage = UsFunc.FindThePlainImage()
print("Original Image Size : ", PlainImage.size[0], "x", PlainImage.size[1])  # Get the width and hight of the image for iterating over


### Making Square, If Vertical Make it Horizontal ###
if PlainImage.size[0] >= PlainImage.size[1]:
    SquareWidth = PlainImage.size[0]
    Verticality = False
else:
    SquareWidth = PlainImage.size[1]
    PlainImage = PlainImage.transpose(Image.ROTATE_90)
    Verticality = True
PlainImagePixels = list(PlainImage.getdata())
ImgOps.CreateSquareImage(SquareWidth, PlainImagePixels, Verticality)


### Cipher Image ###
SecretImage = UsFunc.FindTheSecretImage()
SecretPixelColors = list(SecretImage.getdata())
SecretPixelColors = list(UsFunc.Chunks(SecretPixelColors, 2))

CipherPixelColors = []
SecretKey = UsFunc.CreateSecretKeyFile()
print(SecretKey)

UsFunc.PrintProgressBar(0, len(SecretPixelColors), prefix='Progress:', suffix='Complete', length=50)
for i, Secrets in enumerate(SecretPixelColors):
    SecretRa = Secrets[0][0]
    SecretGa = Secrets[0][1]
    SecretBa = Secrets[0][2]

    SecretRb = Secrets[1][0]
    SecretGb = Secrets[1][1]
    SecretBb = Secrets[1][2]

    SecretRaIndex = list(zip(*np.where(SecretKey == SecretRa)))[0]
    SecretRbIndex = list(zip(*np.where(SecretKey == SecretRb)))[0]

    SecretGaIndex = list(zip(*np.where(SecretKey == SecretGa)))[0]
    SecretGbIndex = list(zip(*np.where(SecretKey == SecretGb)))[0]

    SecretBaIndex = list(zip(*np.where(SecretKey == SecretBa)))[0]
    SecretBbIndex = list(zip(*np.where(SecretKey == SecretBb)))[0]

    Red = UsFunc.WhatWeDo(SecretRaIndex, SecretRbIndex, SecretKey)
    Green = UsFunc.WhatWeDo(SecretGaIndex, SecretGbIndex, SecretKey)
    Blue = UsFunc.WhatWeDo(SecretBaIndex, SecretBbIndex, SecretKey)

    CipherPixelColors.append((Red[0], Green[0], Blue[0]))
    CipherPixelColors.append((Red[1], Green[1], Blue[1]))
    UsFunc.PrintProgressBar(i + 1, len(SecretPixelColors), prefix='Progress:', suffix='Complete', length=50)

ImgOps.CreateCipherImage(SquareWidth, CipherPixelColors)