# -*- coding: utf-8 -*-
"""
@author: Allen
"""

import os
import sys
import shutil
from math import log, ceil
from PIL import Image

# Methods


def folderReset(sourceDir, numberOfLevel):
    levelDir = ""

    print("Reseting folder...")

    for l in range(numberOfLevel):
        levelDir = os.path.join(sourceDir, str(l))
        if os.path.isdir(levelDir):
            shutil.rmtree(levelDir)
        os.mkdir(levelDir)

    print("Folder Reset complete.\n")


def showImageInfo(sourceImage):
    print("Source Image Info")
    try:
        print(" Filename: ", sourceImage.filename)
    except AttributeError:
        print(" Filename: -- ")
    print(" Format: ", sourceImage.format)
    print(" Size: ", sourceImage.size)
    print(" Mode: ", sourceImage.mode)


def calcLevel(sourceImage):
    n = sourceImage.size[0]
    m = sourceImage.size[1]
    L = ceil(log(max(n, m), 2))

    return L


def halfResolution(sourceImage):
    reducedImage = sourceImage.resize((int(ceil(sourceImage.size[0]/2)),
                                       int(ceil(sourceImage.size[1]/2))),
                                      Image.ANTIALIAS)

    print("Image Resolution halfed...")

    showImageInfo(reducedImage)
    
    return reducedImage


def makeTiles(sourceImage, tileSize, rowTiles, colTiles, levelDir):
    left = 0
    upper = 0
    right = tileSize
    lower = tileSize

    cropImage = None

    if sourceImage.size[0] <= tileSize:
        right = sourceImage.size[0]
    if sourceImage.size[1] <= tileSize:
        lower = sourceImage.size[1]

    print("Number of tiles needed: %d (%dx%d)"
          % (rowTiles*colTiles, rowTiles, colTiles))

    for y in range(colTiles):
        for x in range(rowTiles):
            cropImage = sourceImage.crop((left, upper, right, lower))
            cropImage.save(os.path.join(levelDir, "%d_%d.jpg" % (left, upper)))

            left = left + tileSize

            if(right + tileSize >= sourceImage.size[0]):
                right = sourceImage.size[0]
            else:
                right = right + tileSize

        left = 0
        upper = upper + tileSize
        right = tileSize

        if(lower + tileSize >= sourceImage.size[1]):
            lower = sourceImage.size[1]
        else:
            lower = lower + tileSize
    return

# Execution
if __name__ == "__main__":
    sourceDir = ""

    L = 0
    rowTiles = 1
    colTiles = 1
    TILE_SIZE = 256

    sourceImage = None

    try:
        sourceImage = Image.open(sys.argv[1])
        # sourceImage = Image.open("cat.jpg")  # for testing purpose
        sourceDir = os.path.dirname(os.path.realpath("cat.jpg"))
        L = int(calcLevel(sourceImage))

        print("Level of Zoom: %d\n" % L)

        folderReset(sourceDir, L)
        showImageInfo(sourceImage)
        for level in range(L):
            makeTiles(sourceImage,
                      TILE_SIZE,
                      int(ceil(float(sourceImage.size[0])/TILE_SIZE)),
                      int(ceil(float(sourceImage.size[1])/TILE_SIZE)),
                      os.path.join(sourceDir, str(level)))

            print("Level %d tiles completed\n" % level)

            if level < L-1:
                sourceImage = halfResolution(sourceImage)

    except Exception:
        print("There is no such file")

    print("END PROGRAM")
