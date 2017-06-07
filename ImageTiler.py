from math import log2, ceil
import os, sys
from PIL import Image
#from PIL import Image, ImageTk

# Variables
n = 0
m = 0
L = 1
image_fName = ""
image = None



# Methods

def reset():
    "CODE"

def calcLevel():
    n = image.width
    m = image.height
    L = ceil(log2(max(n,m)))

    for i in range(L):
        os.mkdir("Level" + str(i))



# Execution
#print( sys.argv[1] )
try:
#    image_fName = os.getcwd() + sys.argv[1]
    image = Image.open("cat.jpg")
    calcLevel()
    
except FileNotFoundError:
    print("There is no such file")

print("END PROGRAM")
