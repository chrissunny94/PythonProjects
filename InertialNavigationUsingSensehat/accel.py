from sense_hat import SenseHat

import time
from time import sleep
X=0.0000
Y=0.0000
Z=0.0000
ux=0
vx=0
vy=uy=uz=vz=0
sense = SenseHat()

a = sense.accel_raw
axdel = a["x"]
aydel = a["y"]
azdel = a["z"]
#axdel =0
#aydel =0
#azdel =0

while(True):
	a = sense.accel_raw
	#print(a)
    	ax=float(10*((a["x"])-axdel))
    	ay=float(10*((a["y"])-aydel))
    	az=float(10*((a["z"])-azdel))
	

    	then = time.time()% 60
    	sleep(0.05)
    	now = time.time()% 60
    	diff = now - then
    	seconds = diff % 60

    	ax1 = float(10*(a["x"] - axdel))
    	ay1 = float(10*(a["y"] - aydel))
    	az1 = float(10*(a["z"] - azdel))
	
    	vx = vx + (ax1*now-ax*then)
    	vy = vy + (ay1*now-ay*then) 	
    	vz = vz + (az1*now-az*then)	
 	

    	#X = X + vx*diff + (1/2*((ax1+ax)/2))*diff*diff
    	#Y = Y + vy*diff + (1/2*((ay1+ay)/2))*diff*diff
    	#Z = Z + vz*diff + (1/2*((az1+az)/2))*diff*diff
	
	X = X  + ((1/2)*((ax1+ax)/2))*then*then
    	Y = Y  + ((1/2)*((ay1+ay)/2))*then*then
    	Z = Z  + ((1/2)*((az1+az)/2))*then*then
	

	#print(ax ,ay ,az)
	print(10*a["x"],10*a["y"],10*a["z"])
	#print(X,Y,Z)
		
