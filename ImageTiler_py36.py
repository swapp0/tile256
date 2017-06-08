# -*- coding: utf-8 -*-
"""
@author: Allen
"""

import os
import sys
import shutil
from math import log2, ceil
from PIL import Image

# Methods
def folderReset(sourceDir, numberOfLevel):
    levelDir = ""
    
    for l in range(numberOfLevel):
        levelDir = sourceDir + l
        if os.path.isdir(levelDir):
            shutil.rmtree(levelDir)
        else:
            os.mkdir(levelDir)
    
def showImageInfo(sourceImage):
    print("Source Image Info")
    print(" Filename: ", sourceImage.filename, "\n"
          " Format: ", sourceImage.format, "\n"
          " Size: ", sourceImage.size, "\n"
          " Mode: ", sourceImage.mode)

def calcLevel(sourceImage):
    n = sourceImage.width
    m = sourceImage.height
    L = ceil(log2(max(n, m)))
    numOfTile = ceil(n/256) * ceil(m/256)

    print("Level of Zoom: %d" % L)
    print("Number of tiles needed: %d (%dx%d)"
          % (numOfTile, ceil(n/256), ceil(m/256)))
    
    return n, m, L

# Execution
if __name__ == "__main__":
    sourceDir = "\\L"
    
    rowTiles = 1
    colTiles = 1
    TILE_SIZE = 256
    
    sourceImage = None

    try:
        # sourceImage = Image.open(sys.argv[1])
        sourceImage = Image.open("cat.jpg") # for testing purpose
        sourceDir = os.path.dirname(os.path.realpath("cat.jpg"))
        showImageInfo(sourceImage)
        n, m, L = calcLevel(sourceImage)
        folderReset(sourceDir, L)
        # makeTiles(sourceImage, TILE_SIZE, ceil(n/TILE_SIZE), ceil(m/TILE_SIZE), levelDir)

    except FileNotFoundError:
        print("There is no such file")

    print("END PROGRAM")
