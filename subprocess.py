#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:57:01 2020

@author: arun
"""
import numpy as np
import random
# importing image object from PIL 
from PIL import Image, ImageDraw 
  
axis = 3

matrix = np.empty((axis,axis))

alphabets = []
val_index = []
alpha = 'A'
for i in range(0, 26): 
    alphabets.append(alpha) 
    alpha = chr(ord(alpha) + 1)

def randomnumbers():
    r = 0
    r = random.randrange(1,axis*axis+1)
    return r

for i in range(0, axis):
    for j in range(0,axis):
        while True:
            val = randomnumbers()
            if val not in val_index:
                val_index.append(val)
                matrix[i,j] = val
                break
print(matrix)


w, h = 1000, 1000
shape = [(40, 40), (w, h)] 
shape1 = [(40, 1000), (1000, 1060)] 
  
# creating new Image object 
box = Image.new("RGB", (w, h)) 
  
# create rectangle image 
img1 = ImageDraw.Draw(box)   


img1.rectangle(shape, fill ="#fff", outline ="red")
img1.rectangle(shape1, fill ="#fff", outline ="red")               

box.show() 

  

        
    