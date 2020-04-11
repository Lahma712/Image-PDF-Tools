from PIL import Image
import os
import getpass
host = getpass.getuser()

def bleach(img): # function that iterates over pixels and turns nearly white pixels completely white
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x,y][0] > 190 and pix[x,y][1] > 190 and pix[x,y][2] > 190 :
                pix[x,y] = (255, 255, 255, 255)
    img.save(r"C:\Users\{}\Desktop\ImageBleach\{}".format(host, str(n[:-4]+"-bleached.png")))


if not os.path.exists(r"C:\Users\{}\Desktop\ImageBleach".format(host)):
    os.mkdir(r"C:\Users\{}\Desktop\ImageBleach".format(host)) # creates folder on desktop that holds images
print(input("Place your images into the 'imageBleach' folder on your desktop. Press ENTER to continue."))

for n in os.listdir(r"C:\Users\{}\Desktop\ImageBleach".format(host)): # for loop that applies bleach() to all images in the folder
    path = r"C:\Users\{}\Desktop\ImageBleach\{}".format(host, n)
    img = Image.open(path)
    img = img.convert("RGBA")
    pix = img.load()
    bleach(img)

print("The images have been saved in the ImageBleach folder.")
