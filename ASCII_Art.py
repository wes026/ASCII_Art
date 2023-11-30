# importing numpy module 
import numpy as np

from PIL import Image
print(Image.__version__)

# opening the image 
im = Image.open("stary_night.jpeg")
#im.show()

# printing the width and height
print(im.size)

#returns tuples of each pixel value in im
pix = list(im.getdata())
# print(pix)


# returns pixel access object and pix_mapping[x][y] gives the pixel value at (x,y) coordinates
pix_mapping = im.load()




#turning the list of tuples into a 2d array 
arr = np.asarray(pix)
print(arr)
# nested loop to iterate through the array 

for x in range(1):
    for y in range(len(arr[x])-2):
        r = arr[x][y]
        g = arr[x][y+1]
        b = arr[x][y+2]
        brightness = (r+g+b)/3
        

# Convert RGB tuples of your pixels into single brightness numbers

char = list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")