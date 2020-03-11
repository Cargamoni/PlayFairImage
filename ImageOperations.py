from PIL import Image
from PIL import ImageOps

#### Making Square Image ###
def CreateSquareImage(width, colors, isVertical):
    img = Image.new('RGB', (width, width), "black") # Paint it black
    pixels = img.load()  # Create the pixel map
    counter = 0
    for i in range(img.size[0]):  # For every pixel:
        for j in range(img.size[1]):
            # Set the colour accordingly
            pixels[i, j] = (colors[counter][0], colors[counter][1], colors[counter][2])
            if counter < len(colors) - 1:
                counter = counter + 1
            else:
                counter = 0
    if not isVertical:
        img = img.rotate(-90)

    print("Square Image Size : ", img.size[0], "x", img.size[1])
    img = ImageOps.mirror(img)
    #img.show()
    img.save('converted/secret.bmp', format='bmp')

### Cipher Image Creation ###
def CreateCipherImage(width, colors):
    img = Image.new('RGB', (width, width), "black")  # Create a new black image
    pixels = img.load()  # Create the pixel map
    counter = 0
    for i in range(img.size[0]):  # For every pixel:
        for j in range(img.size[1]):
            # pixels[i, j] = (i, j, 100)  # Set the colour accordingly
            pixels[i, j] = (colors[counter][0], colors[counter][1], colors[counter][2])
            if counter < len(colors) - 1:
                counter = counter + 1
            else:
                counter = 0

    img = ImageOps.mirror(img)
    img = img.rotate(90)
    img.show()
    img.save('converted/cipher.bmp', format='bmp')

### Cipher Image Creation ###
def CreateDecipherImage(width, colors):
    img = Image.new('RGB', (width, width), "black")  # Create a new black image
    pixels = img.load()  # Create the pixel map
    counter = 0
    for i in range(img.size[0]):  # For every pixel:
        for j in range(img.size[1]):
            pixels[i, j] = (colors[counter][0], colors[counter][1], colors[counter][2])
            if counter < len(colors) - 1:
                counter = counter + 1
            else:
                counter = 0

    img = ImageOps.mirror(img)
    img = img.rotate(90)
    img.show()
    img.save('converted/decipheredImage.bmp', format='bmp')

### Playfair Secret Image Change ###
def CipherPlainImage(indexA, indexB, secretKey):
    if indexA[0] == indexB[0]:  # Aynı Line
        return (secretKey[indexA[0],(indexA[1]+1)%16], secretKey[indexB[0],(indexB[1]+1)%16])
    if indexA[1] == indexB[1]:  # Aynı Column
        return (secretKey[(indexA[0]+1)%16,indexA[1]],secretKey[(indexB[0]+1)%16,indexB[1]])
    else:                       # Köşegen
        return (secretKey[indexA[0],indexB[1]],secretKey[indexB[0],indexA[1]])

### Playfair Decipher Image ###
def DecipherCipherImage(indexA, indexB, SecretKey):
    if indexA[0] == indexB[0]:  # Aynı Line
        return (SecretKey[indexA[0],(indexA[1]-1)%16], SecretKey[indexB[0],(indexB[1]-1)%16])
    if indexA[1] == indexB[1]:  # Aynı Column
        return (SecretKey[(indexA[0]-1)%16,indexA[1]],SecretKey[(indexB[0]-1)%16,indexB[1]])
    else:                       # Köşegen
        return (SecretKey[indexA[0],indexB[1]],SecretKey[indexB[0],indexA[1]])