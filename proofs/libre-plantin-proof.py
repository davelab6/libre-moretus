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

# grid
#translate(*origin) # grid off
grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0)
stroke(None)

text("Libre Plantin: https://github.com/eliheuer/libre-plantin", (-1, 704-16))
text("144pt", (-1, 704-64))

txt_line_one="""Libre Plantin abehijl mnort LHPO"""

font("LibrePlantin-Bold")
fontSize(144)
tracking(0)
lineHeight(99)
textBox(txt_line_one, (-5, -55, 560, 630)) #align="center"
#textBox(txt_line_two, (-2, -32, 520, 300))
#textBox(txt_line_three, (-2, -32, 520, 628-(80*2)))
#textBox(txt_line_four, (-2, -32, 520, 628-(80*3)))

lineHeight(None)
###############################################################

######################################################### -- page 2
newPage()

# grid
#translate(*origin) # grid off
grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)

text("Libre Plantin: https://github.com/eliheuer/libre-plantin", (-1, 704-16))
text("144pt", (-1, 704-64))

txt_line_one="""Libre Plantin"""
 
textBox("Hello World " * 100, (0, 0, 300, 300))

font("LibrePlantin-Bold")
fontSize(144)
tracking(-4)
lineHeight(80)
#textBox(txt_line_one, (-2, -32, 520, 492))
#textBox(txt_line_two, (-2, -32, 520, 628-80))
#textBox(txt_line_three, (-2, -32, 520, 628-(80*2)))
#textBox(txt_line_four, (-2, -32, 520, 628-(80*3)))

lineHeight(None)
###############################################################

saveImage("libre-plantin-proof.pdf")
