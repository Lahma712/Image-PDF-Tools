import os
import getpass
from pdf2image import convert_from_path
host = getpass.getuser()
Path = r"C:\Users\{}\Desktop\PDFtoImage".format(host)

if not os.path.exists(r"C:\Users\{}\Desktop\PDFtoImage".format(host)):
    os.mkdir(Path.format(host)) # creates a folder on the desktop that will hold your pdf
print(input("Put your PDF in the PDFtoImage folder on your desktop! Press ENTER to continue."))

pages = list([n for n in input("Page range (f.ex '1-3'): ").split('-')]) #list that holds the first and last page number
pngList = convert_from_path(Path + "\{}".format(os.listdir(Path.format(host))[0]), first_page= int(pages[0]), last_page= int(pages[1])) #list of converted png files

for image in pngList:
    image.save(Path+"\\Page{}.png".format(pages[0]))
    pages[0] = int(pages[0])+1
print("The .png files have been saved in the PDFtoImage folder.")
