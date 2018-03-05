"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zhiyu Wang HERE.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()


mike=rg.SimpleTurtle('turtle')
mike.pen=rg.Pen('light green',3)
mike.speed=200
size=300
for k in range(6):

    mike.draw_square(size)

    mike.pen_up()
    mike.right(60)
    mike.pen_down()

Shay= rg.SimpleTurtle('turtle')
Shay.pen = rg.Pen('red', 15)
Shay.speed = 200
size = 150
for k in range(8):

    Shay.draw_circle(size)

    Shay.pen_up()
    Shay.pen_down()

    Shay.forward(100)
    Shay.right(45)
    Shay.forward(100)
    Shay.right(45)
    Shay.forward(100)
    Shay.right(45)
    Shay.forward(100)
    Shay.right(45)
    Shay.forward(100)
    Shay.right(45)
    Shay.forward(100)
    Shay.right(45)
    Shay.forward(100)
    Shay.right(45)
    Shay.forward(100)

window.close_on_mouse_click()