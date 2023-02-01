import djitellopy as tello

import time
drone = tello.Tello()
drone.connect()
battery = drone.get_battery()
print(battery)
drone.takeoff()
drone.send_rc_control(0,50,0,0) #lr, fb, ud, yv
time.sleep(0.5)

drone.send_rc_control(0,0,0,0) #lr, fb, ud, yv
time.sleep(0.5)

drone.send_rc_control(0,0,0,0) #lr, fb, ud, yv
time.sleep(0.5)

drone.send_rc_control(0,0,0,0) #lr, fb, ud, yv
time.sleep(0.5)

drone.land()
