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
def folderReset():
    if os.path.isdir(levelDir):
        shutil.rmtree(levelDir)

    os.mkdir(levelDir)
    
def showImageInfo():
    print("Source Image Info")
    print(" Filename: ", sourceImage.filename, "\n"
          " Format: ", sourceImage.format, "\n"
          " Size: ", sourceImage.size, "\n"
          " Mode: ", sourceImage.mode)

    calcLevel()

def calcLevel():
    global n
    n = sourceImage.width
    global m
    m = sourceImage.height
    global L
    L = ceil(log2(max(n, m)))
    numOfTile = ceil(n/256) * ceil(m/256)

    print("Level of Zoom: %d" % L)
    print("Number of tiles needed: %d (%dx%d)"
          % (numOfTile, ceil(n/256), ceil(m/256)))

def makeTile(left, upper, right, lower):
    return


# Execution
if __name__ == "__main__":
    left = 0
    upper = 0
    right = 256
    lower = 256
    
    tileNum = 1
    rowTiles = 1
    colTiles = 1
    
    cropImage = None

    folderReset()

    try:
        # sourceImage = Image.open(sys.argv[1])
        sourceImage = Image.open("cat.jpg")
        showImageInfo()
        rowTiles = ceil(n/256)
        colTiles = ceil(m/256)

        for y in range(colTiles):
            for x in range(rowTiles):
                cropImage = sourceImage.crop((left, upper, right, lower))
                print("%3d %2d %2d %4d %4d %4d %4d - %4d %4d" % (tileNum, x, y, left, upper, right, lower, cropImage.width, cropImage.height))
                cropImage.save(
                        levelDir+"\\%d_%d_%d.jpg" % (tileNum, left, upper),
                        #levelDir+"\\%d_%d.jpg" % (left, upper),
                        format=sourceImage.format)
                tileNum = tileNum + 1
                
                left = left + 256
                # account for the last tile of the row where the
                # remaining pixel do not fill the right side of the tile
                if(right + 256 >= sourceImage.width):
                    right = sourceImage.width
                else:
                    right = right + 256
    
            left = 0
            upper = upper + 256
            right = 256
            # account for the last row tile of the column where the
            # remaining pixels of each subtile do not fill the bottom side
            if(lower + 256 >= sourceImage.height):
                lower = sourceImage.height                    
            else:
                lower = lower + 256

    except FileNotFoundError:
        print("There is no such file")
        raise

    print("END PROGRAM")
