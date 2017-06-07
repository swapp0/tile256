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
def folderReset():
    if os.path.isdir(LEVEL_DIR):
        shutil.rmtree(LEVEL_DIR)

    os.mkdir(LEVEL_DIR)
    
def showImageInfo():
    print("Source Image Info")
    print(" Filename: ", sourceImage.filename, "\n"
          " Format: ", sourceImage.format, "\n"
          " Size: ", sourceImage.size, "\n"
          " Mode: ", sourceImage.mode)

def calcLevel():
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
    LEVEL_DIR = os.getcwd() + "\\L"
    
    rowTiles = 1
    colTiles = 1
    TILE_SIZE = 256
    
    left = 0
    upper = 0
    right = 256
    lower = 256
    
    sourceImage = None
    cropImage = None

    folderReset()

    try:
        sourceImage = Image.open(sys.argv[1])
        # sourceImage = Image.open("cat.jpg")
        showImageInfo()
        n, m, L = calcLevel()
        rowTiles = ceil(n/TILE_SIZE)
        colTiles = ceil(m/TILE_SIZE)

        for y in range(colTiles):
            for x in range(rowTiles):
                cropImage = sourceImage.crop((left, upper, right, lower))
                print("%2d %2d %4d %4d %4d %4d - %4d %4d" % 
                      (x, y, left, upper, right, lower, cropImage.width, cropImage.height))
                cropImage.save(
                        LEVEL_DIR+"\\%d_%d.jpg" % (left, upper),
                        format=sourceImage.format)
                
                left = left + TILE_SIZE
                # account for the last tile of the row where the
                # remaining pixel do not fill the right side of the tile
                if(right + TILE_SIZE >= sourceImage.width):
                    right = sourceImage.width
                else:
                    right = right + TILE_SIZE
    
            left = 0
            upper = upper + TILE_SIZE
            right = TILE_SIZE
            # account for the last row tile of the column where the
            # remaining pixels of each subtile do not fill the bottom side
            if(lower + TILE_SIZE >= sourceImage.height):
                lower = sourceImage.height                    
            else:
                lower = lower + TILE_SIZE

    except FileNotFoundError:
        print("There is no such file")
        raise

    print("END PROGRAM")
