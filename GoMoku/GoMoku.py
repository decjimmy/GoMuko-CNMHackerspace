import arcade
arcade.open_window(600,600, "Drawining example")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()
#drawing code goes here
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.finish_render()

arcade.run()