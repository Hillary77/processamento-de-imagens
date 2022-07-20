from PIL import Image, ImageOps, ImageDraw, ImageFilter
from random import randint
import numpy as np


#Imagem01

with Image.open("01.jpg") as img:
    img = img.convert("RGB")

width, height = img.size

img = img.convert("L")
pixels = img.load()


brilho = 40


for x in range(width):
    for y in range(height):
        pixels[x,y] = pixels[x,y] + brilho

img.show()

#Imagem02

with Image.open("02.jpg") as img:
      img = img.convert("RGB")


img = img.filter(ImageFilter.GaussianBlur(7))

img.show()

#Imagem03
    
with Image.open("03.png") as img:
    img = img.convert("RGB")
    
img = img.filter(ImageFilter.MinFilter(5))
    
img.show()

