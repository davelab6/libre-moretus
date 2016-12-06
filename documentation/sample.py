# from drawBot import * # uncomment if using setupAsModule.py
import math # for cos, sin and pi functions

# Print installed fonts to the terminal
print installedFonts()

# static variables
canvasWidth = 452  # size of the image in pixels
canvasHeight = 90

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# draws a new page
def new_page(): 
    newPage(canvasWidth, canvasHeight) # new page from canvas variable 
    fill(1) # color of background
    rect(0, 0, canvasWidth, canvasHeight) # draw the backgroun
new_page()
    
# type 
fontSize(72)
font("LibrePlantin-Bold")
tracking(0)
fill(0)
stroke(None)
text("Libre Plantin", (-2, 30))
fill(1, 0, 0)
                   
saveImage("sample.png")