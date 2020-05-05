#!/usr/bin/python3
from sense_hat import SenseHat
import math
import pi3d
import time
from time import sleep

sense = SenseHat()

display = pi3d.Display.create()
cam = pi3d.Camera.instance()

shader = pi3d.Shader("mat_light")

model = pi3d.Model(
    file_string="apollo-soyuz.obj",
    name="model", x=0, y=-1, z=40, sx=1, sy=1, sz=1)

model.set_shader(shader)

cam.position((0, 20, 0))
cam.point_at((0, -1, 40))
keyb = pi3d.Keyboard()

compass = gyro = accel = True
sense.set_imu_config(compass, gyro, accel)

yaw_offset = 72

X=0
Y=-1
Z=40

ux=0
vx=0
vy=uy=uz=vz=0
sense = SenseHat()

a = sense.accel_raw
axdel = 10*a["x"]
aydel = 10*a["y"]
azdel = 10*a["z"]

while display.loop_running():
    a = sense.accel_raw
    ax = 10*a["x"] - axdel
    ay = 10*a["y"] - aydel
    az = 10*a["z"] - azdel
	

    then = time.time()% 60
    sleep(0.00001)
    now = time.time()% 60
    diff = now - then
    seconds = diff % 60

    a = sense.accel_raw
    ax1 = 10*a["x"] - axdel
    ay1 = 10*a["y"] - aydel
    az1 = 10*a["z"] - azdel
	
    vx = vx + (ax1*now-ax*then)
    vy = vy + (ay1*now-ay*then) 	
    vz = vz + (az1*now-az*then)	
 	

    X = X + vx*diff
    Y = Y + vy*diff
    Z = Z + vz*diff		 
    model.translateX(X)
    #model.translateY(Y)
    #model.translateZ(vz*diff)			



    o = sense.get_orientation_radians()
    
    #print(sense.accelerometer)
    
    if o is None:
        pass

    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]

    yaw_total = yaw + math.radians(yaw_offset)

    sin_y = math.sin(yaw_total)
    cos_y = math.cos(yaw_total)

    sin_p = math.sin(pitch)
    cos_p = math.cos(pitch)

    sin_r = math.sin(roll)
    cos_r = math.cos(roll)

    abs_roll = math.degrees(math.asin(sin_p * cos_y + cos_p * sin_r * sin_y))
    abs_pitch = math.degrees(math.asin(sin_p * sin_y - cos_p * sin_r * cos_y))

    model.rotateToZ(abs_roll)
    model.rotateToX(abs_pitch)
    model.rotateToY(math.degrees(yaw_total))
    model.draw()

    keypress = keyb.read()

    if keypress == 27:
        keyb.close()
        display.destroy()
        break
    elif keypress == ord('m'):
        compass = not compass
        sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('g'):
        gyro = not gyro
        sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('a'):
        accel = not accel
        sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('='):
        yaw_offset += 1
    elif keypress == ord('-'):
        yaw_offset -= 1
