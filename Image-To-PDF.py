from PIL import Image
import os
import getpass

host = getpass.getuser()

if not os.path.exists(r"C:\Users\{}\Desktop\ImageToPDF".format(host)):
    os.mkdir(r"C:\Users\{}\Desktop\ImageToPDF".format(host)) # creates a folder on the desktop that will hold your images
print(input("Put your images in the ImageToPDF folder on your desktop! Press ENTER to continue."))
imageList = [(Image.open(r"C:\Users\{}\Desktop\ImageToPDF\{}".format(host, n))).convert('RGB') for n in os.listdir(r"C:\Users\{}\Desktop\ImageToPDF".format(host))]
# list comprehension that creates a list that holds all the paths of all the images
imageList[0].save(r"C:\Users\{}\Desktop\ImageToPDF\Images.pdf".format(host), "PDF", resolution=100.0, save_all=True, append_images = imageList[1:]) # saves the image list into one pdf

print("The .pdf file has been saved in the ImageToPDF folder.")
