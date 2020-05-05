#!/usr/bin/python3

import math
import pi3d



display = pi3d.Display.create()
cam = pi3d.Camera.instance()

shader = pi3d.Shader("mat_light")

model = pi3d.Model(
    file_string="apollo-soyuz.obj",
    name="model", x=0, y=-1, z=50, sx=.1, sy=.1, sz=.1)

model.set_shader(shader)

cam.position((0, 20, 0))
cam.point_at((0, -1, 40))
keyb = pi3d.Keyboard()

yaw_offset = 72


while display.loop_running():
    
    
    
    
    model.draw()
    
    keypress = keyb.read()

    if keypress == 27:
        keyb.close()
        display.destroy()
        break
    elif keypress == ord('m'):
        model.rotateToZ(2)
        model.translateX(-1)
    elif keypress == ord('g'):
        model.rotateToX(2)
    elif keypress == ord('a'):
        model.rotateToY(2)
        model.translateX(1)
    elif keypress == ord('='):
        yaw_offset += 1
    elif keypress == ord('-'):
        yaw_offset -= 1
