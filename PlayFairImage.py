from PIL import Image
import numpy as np
import time

### Home Made Functions ###
import UsefullFunctions as UsFunc
import ImageOperations as ImgOps
import SecretShareServer as Server
import SecretShareClient as Client

### Home Made Variables ###
Verticality = False
SquareWidth = 0
Status = True

'''
6 - Decipher Image
'''

while(Status):
    ### Welcome Message ###
    print('Welcome to the Playfair Image Transferring Program: PlayFairImage.')
    print('Please give a input for operations:')
    print('1 : Make a SecretKey')
    print('2 : Create a Cipher Image')
    print('3 : Send Cipher Image')
    print('4 : Get Cipher Image')
    print('5 : Clear Screen')
    print('6 : Quit')
    UserInput = input('Input : ')
    if not UserInput.isnumeric() or UserInput == '':
        print('Please give a valid input !')
        time.sleep(2)
        UsFunc.ClearScreen()
        continue
    else:
        ### 1 : Make a SecretKey ###
        if UserInput == '1':
            UsFunc.ClearScreen()
            print('This operation will create a new SecretKey, if you have already one it will warn you for overwrite operation.')
            print('SecretKey File is using for cipher and decipher your image. Alice have to send this file to Bob for decipher !')
            try:
                fileReader = open("secretKey",'r')
                if fileReader is not None:
                    print('Warning you already have secretKey file, this operation will overwrite through your file.')
                    feedback = input('\nDo you want to continue ? (Y/n : Default No) :> ')
                    if feedback == '' or feedback == 'n':
                        UsFunc.ClearScreen()
                        continue
                    elif feedback == 'Y':
                        print('\nCreating a new SecretKeyFile.\n')
                        SecretKey = UsFunc.CreateSecretKeyFile()
                        print(SecretKey)
                        print('\nNew SecretKey File Created !\n')
                        time.sleep(2)
                    else:
                        print('Wrong input !')
                        time.sleep(2)
            except IOError:
                print("\nSecretKey File not found, creatig a new SecretKey File.\n")
                SecretKey = UsFunc.CreateSecretKeyFile()
                print(SecretKey)
                print("\nNew SecretKey File Created !\n")
                time.sleep(2)

        ### 2 : Create a Cipher Image ###
        if UserInput == '2':
            UsFunc.ClearScreen()
            ### Resimi Açma###
            PlainImage = UsFunc.FindThePlainImage()
            print("Original Image Size : ", PlainImage.size[0], "x",
                  PlainImage.size[1])  # Get the width and hight of the image for iterating over

            ### Making Square, If Vertical Make it Horizontal ###
            if PlainImage.size[0] >= PlainImage.size[1]:
                SquareWidth = PlainImage.size[0]
                Verticality = False
            else:
                SquareWidth = PlainImage.size[1]
                PlainImage = PlainImage.transpose(Image.ROTATE_90)
                Verticality = True

            ### Getting Image's Pixel RGB Values ###
            PlainImagePixels = list(PlainImage.getdata())
            ImgOps.CreateSquareImage(SquareWidth, PlainImagePixels, Verticality)

            ### Cipher Image ###
            SecretImage = UsFunc.FindTheSecretImage()
            SecretPixelColors = list(SecretImage.getdata())
            SecretPixelColors = list(UsFunc.Chunks(SecretPixelColors, 2))

            CipherPixelColors = []
            SecretKey = UsFunc.LoadSecretKeyFile()
            print(SecretKey,'\n')

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

                Red = ImgOps.CipherPlainImage(SecretRaIndex, SecretRbIndex, SecretKey)
                Green = ImgOps.CipherPlainImage(SecretGaIndex, SecretGbIndex, SecretKey)
                Blue = ImgOps.CipherPlainImage(SecretBaIndex, SecretBbIndex, SecretKey)

                CipherPixelColors.append((Red[0], Green[0], Blue[0]))
                CipherPixelColors.append((Red[1], Green[1], Blue[1]))

                UsFunc.PrintProgressBar(i + 1, len(SecretPixelColors), prefix='Progress:', suffix='Complete', length=50)

            ImgOps.CreateCipherImage(SquareWidth, CipherPixelColors)
            print('\nCipher Image Created !\nHeading to Main Menu...\n')
            time.sleep(5)

        ### Send Cipher Image ###
        if UserInput == '3':
            UsFunc.ClearScreen()
            if __name__ == '__main__':
                NewServer = Server
                NewServer.Streaming.run(Server)
            print('\nSending Cipher Image is Complete, Closing Operation\n')
            time.sleep(5)
            continue

        ### Get Cipher Image ###
        if UserInput == '4':
            UsFunc.ClearScreen()
            if __name__ == '__main__':
                NewClient = Client
                NewClient.Receiving.run(Client)
            print('\nRecieving Cipher Image is Complete, Closing Operation\n')
            time.sleep(5)
            continue

        ### 5: Clear Screen ###
        if UserInput == '5':
            UsFunc.ClearScreen()
            continue

        ### 6: Quit ###
        if UserInput == '6':
            Status = False
            print('\nAll operations done, exiting program.')
