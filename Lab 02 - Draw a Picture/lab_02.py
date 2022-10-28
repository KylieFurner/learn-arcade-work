# in this lab I will use arcade to draw a picture
# the picture is supposed to be mountains a lake and some grass

# import the arcade library
import arcade

# open a window to draw in
arcade.open_window(800, 600, "Drawing Example")

# set a background color
# a link to a list of arcade colors https://api.arcade.academy/en/latest/arcade.color.html
# a link to 
arcade.set_background_color(arcade.color.COCOA_BROWN)

# Get ready to draw
arcade.start_render()

# draw the lake
# Rectangle (left, right, top, bottom)
arcade.draw_lrtb_rectangle_filled(0, 800, 300, 0, arcade.color.COAL)

# draw the mountains
# Triangle (x,y , x,y , x,y)
arcade.draw_triangle_filled(100, 300, 200, 550, 400, 300, arcade.color.COFFEE)
arcade.draw_triangle_filled(300, 300, 450, 570, 600, 300, arcade.color.COFFEE)
arcade.draw_triangle_filled(500, 300, 700, 550, 800, 300, arcade.color.COFFEE)
arcade.draw_triangle_filled(325, 500, 100, 300, 600, 300, arcade.color.COOL_GREY)
arcade.draw_triangle_filled(0, 500, 0, 300, 300, 300, arcade.color.COOL_BLACK)
arcade.draw_triangle_filled(800, 500, 800, 300, 500, 300, arcade.color.COOL_BLACK)

# draw an arc for grass (x,y of the center width, height)
arcade.draw_arc_filled(0, 0, 1000, 400, arcade.csscolor.DARK_GREEN, 0, 100)


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

