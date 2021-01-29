# ------------------------
# Image Manipulation #
# ------------------------

from PIL import Image

im = Image.open(r"C:\Users\AUC\Desktop\image.jpg")
w, h = im.size

# print(im.size)

# How it Works 
# first we decide where the crop begin (Position)
# We Deced the width and height of the box
# >> box = 500,500
# >> dist + dim = 500#
newIm = im.crop(200, 400, w - 300, h - 100)
newIm.show()