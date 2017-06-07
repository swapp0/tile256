# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:46:37 2017

@author: Allen

read source image from command line argument
 - check file existant
 - extra width, height to n,m
 - determine the number of tiles if a tile is 256x256
 -- save number of tiles to numberOfTiles

create tiles
 - set pixel locator index locator = (0,0)
 - crop and extract subimage
 -- if desire subimage is less then 256x256, 
 --- create a new empty tile image and paste image to the upper left corner
 -- save image to tile level sub folder with filename L/x_y.jpg
 
    


"""

