# ------------------------
# Image Manipulation #
# ------------------------
from PIL import Image

im = Image.open(r"C:\Users\AUC\Documents\PyProjects\Practical\1.jpg")

im.show()

mybox = ((700, 300, 1500, 1000))
newimg = im.crop(mybox)
newimg.show()
# newimg.save(r"C:\Users\AUC\Documents\PyProjects\Practical\1231.jpg")