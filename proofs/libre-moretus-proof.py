# set a size for the canvas *792 x 612 pixels
size(612, 792)

# using the functions width, height and pageCount
print "width:", width()
print "height:", height()
print "pageCount:", pageCount()
print installedFonts()

# gird variables
origin = (34, 44)
width = 544
height = 704
center = width/2
num_x_units = 17
num_y_units = 22

def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(0.5)
    stroke(0.9, 0.1, 0.1, 0.5)  
    fill(None)
    
    step_x = 0 
    unit_x = width / num_x_units
    for x in range(num_x_units + 1):
        line((step_x, 0), (step_x, height))
        step_x += unit_x
        
    step_y = 0 
    unit_y = height / num_y_units
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
###################################################################

######################################################### -- page 1
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

fontSize(12)
font("Helvetica Neue Bold")
fill(0)
stroke(None)

text("Libre Moretus: https://github.com/eliheuer/libre-moretus", (-1, 704-16))
text("144pt", (-1, 704-64))

txt_line_one="""Libre Moretus abeijl nort PHIL"""
font("LibreMoretus-Bold")
fontSize(144)
lineHeight(99)
textBox(txt_line_one, (-5, -55, 560, 630)) #align="center"

lineHeight(None)
###############################################################

######################################################### -- page 2
newPage()
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

fontSize(12)
font("Helvetica Neue Bold")
fill(0)
stroke(None)

text("Libre Moretus: https://github.com/eliheuer/libre-moretus", (-1, 704-16))
text("72pt", (-1, 704-64))

txt_line_one="""Libre Moretus  nnoonnoonn  oonnoonnoo nnoonnoonn  oonnoonnoo nnaannaann  ooaaooaaoo  nneenneenn eeooeeooee"""
font("LibreMoretus-Bold")
fontSize(72)
lineHeight(50)
textBox(txt_line_one, (-1, 0, 560, 591)) #align="center"

lineHeight(None)
###############################################################

saveImage("libre-moretus-proof.pdf")
