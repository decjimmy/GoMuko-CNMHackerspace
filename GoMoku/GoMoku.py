import arcade
# Import the "arcade" library
import arcade

def draw_tree(x,y):
    arcade.draw_rectangle_filled(x, y, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(x, y + 30, 30, arcade.csscolor.DARK_GREEN)

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
draw_tree(100, 320)
draw_tree(220, 320)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()