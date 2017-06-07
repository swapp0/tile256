# -*- coding: utf-8 -*-
"""
@author: Allen
"""

import os
import sys
import shutil
from math import log2, ceil
from PIL import Image

# Variables
levelDir = os.getcwd() + "\\L"
n = 0
m = 0
L = 1
sourceImage = None
numberOfTiles = 0



# Methods
def showImageInfo():
    print("Source Image Info")
    print(" Filename: ", sourceImage.filename, "\n"
          " Format: ", sourceImage.format, "\n"
          " Size: ", sourceImage.size, "\n"
          " Mode: ", sourceImage.mode)

    calcLevel()
    
def calcLevel():
    n = sourceImage.width
    m = sourceImage.height
    L = ceil(log2(max(n,m)))
    numberOfTiles = ceil(n/256) * ceil(m/256)

    print("Level of Zoom: " + str(L))
    print("Number of tiles needed: " + str(numberOfTiles))


def makeTile(left, upper, right, lower):
    return
    

# Execution
if __name__ == "__main__":
    left = 0
    upper = 0
    right = 256
    lower = 256
    lastTileInRow = None
    tileNum = 1

    if os.path.isdir(levelDir):
        shutil.rmtree(levelDir)

    os.mkdir(levelDir)

    try:
        # sourceImage = Image.open(sys.argv[1])
        sourceImage = Image.open("cat.jpg")
        showImageInfo()

        while lower < sourceImage.height:
            while right < sourceImage.width:
                sourceImage.crop((left,
                                  upper,
                                  right,
                                  lower)).save(levelDir+"\\%d_%d_%d.jpg" % (tileNum, left, upper), format=sourceImage.format)
                tileNum = tileNum + 1
                
                left = left + 256
                right = right + 256

            # when you reached the last tile of the row and the pixels do not fill the entire tile
            if left < sourceImage.width:
                sourceImage.crop((left,
                                  upper,
                                  sourceImage.width,
                                  lower)).save(levelDir+"\\%d_%d_%d.jpg" % (tileNum, left, upper), format=sourceImage.format)
                tileNum = tileNum + 1

            left = 0
            upper = upper + 256
            right = 256
            lower = lower + 256

        # when you reached the last row of the image and each tile don't have
        # enough pixels to fill the entire space
        lower = sourceImage.height
        while right < sourceImage.width:
                sourceImage.crop((left,
                                  upper,
                                  right,
                                  lower)).save(levelDir+"\\%d_%d_%d.jpg" % (tileNum, left, upper), format=sourceImage.format)
                tileNum = tileNum + 1
                
                left = left + 256
                right = right + 256

            # when you reached the last tile of the row and the pixels do not fill the entire tile
                if left < sourceImage.width:
                    sourceImage.crop((left,
                                      upper,
                                      sourceImage.width,
                                      lower)).save(levelDir+"\\%d_%d_%d.jpg" % (tileNum, left, upper), format=sourceImage.format)
                    tileNum = tileNum + 1
        
        

    except FileNotFoundError:
        print("There is no such file")
        raise

    print("END PROGRAM")
