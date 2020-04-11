from pdf2image import convert_from_path
from PIL import Image
import getpass
from pdf2image import pdfinfo_from_path
import os
import time

host = getpass.getuser()
VarDump = [0,0] # list that temporarily saves newest size and location settings

if not os.path.exists(r"C:\Users\{}\Desktop\pdfInsert".format(host)):
    os.mkdir(r"C:\Users\{}\Desktop\pdfInsert".format(host)) # creates a folder on the desktop that will hold your pdf and image

print(input("\nPut your .pdf and .png file into the 'pdfInsert' folder on your desktop! Press ENTER to continue."))
pastePath = r"C:\Users\{}\Desktop\pdfInsert\{}".format(host, [n for n in os.listdir(r"C:\Users\{}\Desktop\pdfInsert".format(host)) if n.endswith(".png") or n.endswith(".jpg") or n.endswith(".jpeg")][0])
# image path using a list comprehension that searches for the image file
pdfPath = r"C:\Users\{}\Desktop\pdfInsert\{}".format(host, [n for n in os.listdir(r"C:\Users\{}\Desktop\pdfInsert".format(host)) if n.endswith(".pdf")][0])
# pdf path using a list comprehension that searches for the .pdf file

Mode = input("Keep aspect ratio? y/n: ") # 'yes' utilizes the thumbnail() function and 'no' the resize() function
page = int(input("PDF page number (f.ex '1' for first page): "))
pageCount = int(pdfinfo_from_path(pdfPath)["Pages"])
pngList = convert_from_path(pdfPath, first_page=1, last_page=pageCount) # creates a list with all the pdf pages as png's
pngList[page-1].save(r"C:\Users\{}\Desktop\pdfInsert\temporary.png".format(host)) # 'page-1' because we count from 0, not from 1

while True:
    pasteLocation = input("\nX/Y coordinates (eg. '800,50'): ")
    pasteSize = input("Width/Height in pixels (eg. ' 500,600'): ")

    if pasteSize == "" and pasteLocation == "": # if your settings dont change for one loop, it automatically saves the pdf file and exits the program
        pngList[page - 1] = png
        pngList[0].save(r"C:\Users\{}\Desktop\pdfInsert.pdf".format(host), "PDF", resolution=100.0, save_all=True, append_images=pngList[1:])
        os.remove(r"C:\Users\{}\Desktop\pdfInsert\temporary.png".format(host)) #removes temporary .png files that were used to paste the image
        print("\nThe .pdf file has been saved in the pdfInsert folder.")
        time.sleep(6)
        exit()

    if pasteLocation != "": # lets the user use the previous setting again by simply pressing ENTER. This saves time
        VarDump[0] = pasteLocation
    else:
        pasteLocation = VarDump[0]
    if pasteSize != "":
        VarDump[1] = pasteSize
    else:
        pasteSize=VarDump[1]

    Paste = Image.open(pastePath)
    if Mode == "y":
        Paste.thumbnail(eval(pasteSize))
    else:
        Paste = Paste.resize(eval(pasteSize))

    png = Image.open(r"C:\Users\{}\Desktop\pdfInsert\temporary.png".format(host))
    png.paste(Paste, (eval(pasteLocation)))
    png.show()
