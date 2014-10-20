##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
# house outline-70pt
drawpad.create_rectangle(40,100,160,200)
drawpad.create_line(40,100,100,20)
drawpad.create_line(100,20,160,100)
#windows & door-80pt
drawpad.create_rectangle(80,160,110,200)
drawpad.create_rectangle(50,110,70,130)
drawpad.create_rectangle(50,140,70,160)
drawpad.create_rectangle(120,110,140,130)
drawpad.create_rectangle(120,140,140,160)
#door handle & chimney-90pt
drawpad.create_oval(100,180,110,190)
drawpad.create_line(140,70.5,140,50)
drawpad.create_line(140,50,160,50)
drawpad.create_line(160,50,160,120)
root.mainloop()
