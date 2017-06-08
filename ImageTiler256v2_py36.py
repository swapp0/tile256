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
def folderReset(levelDir):
    if os.path.isdir(levelDir):
        shutil.rmtree(levelDir)

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

def makeTiles(sourceImage, tileSize, rowTiles, colTiles, levelDir):
    left = 0
    upper = 0
    right = tileSize
    lower = tileSize

    cropImage = None
    
    # tileNumber = 1 # for testing purpose
    
    for y in range(colTiles):
        for x in range(rowTiles):
            cropImage = sourceImage.crop((left, upper, right, lower))
            print("%2d %2d %4d %4d %4d %4d - %4d %4d" % 
                  (x, y, left, upper, right, lower, cropImage.width, cropImage.height))
            cropImage.save(os.path.join(levelDir, "%d_%d.jpg" % (left, upper)))
                    # levelDir+"\\%d_%d_%d.jpg" % (tileNumber, left, upper)) # for testing purpose
            
            # tileNumber = tileNumber + 1  # for testing purpose
            
            left = left + tileSize
            # account for the last tile of the row where the
            # remaining pixel do not fill the right side of the tile
            if(right + tileSize >= sourceImage.width):
                right = sourceImage.width
            else:
                right = right + tileSize

        left = 0
        upper = upper + tileSize
        right = tileSize
        # account for the last row tile of the column where the
        # remaining pixels of each subtile do not fill the bottom side
        if(lower + tileSize >= sourceImage.height):
            lower = sourceImage.height                    
        else:
            lower = lower + tileSize
    return

# Execution
if __name__ == "__main__":
    leveDir = "\\L"
    
    rowTiles = 1
    colTiles = 1
    TILE_SIZE = 256
    
    sourceImage = None

    try:
        # sourceImage = Image.open(sys.argv[1])
        sourceImage = Image.open("cat.jpg") # for testing purpose
        levelDir = os.path.join(os.path.dirname(os.path.realpath("cat.jpg")), "L")
        showImageInfo(sourceImage)
        folderReset(levelDir)
        n, m, L = calcLevel(sourceImage)
        makeTiles(sourceImage, TILE_SIZE, ceil(n/TILE_SIZE), ceil(m/TILE_SIZE), levelDir)

    except FileNotFoundError:
        print("There is no such file")

    print("END PROGRAM")
