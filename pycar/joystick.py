from car import Car

import curses
from curses import wrapper
from car import Car

car = Car()

def main(screen):
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    screen.addstr("PRESS THE ARROW KEYS TO MOVE THE car")
    pan = 90
    tilt = 110
    speed = 0
    steeringAngle = 90

    while True:
        c = screen.getch()
        if c == curses.KEY_LEFT:
            screen.addstr(5,10, 'left key pressed')
            pan = pan + 10
            car.camera.pan = pan
            screen.refresh()
        elif c == curses.KEY_RIGHT:
            screen.addstr(5,50, 'right key pressed')
            pan = pan - 10
            car.camera.pan = pan
            screen.refresh()
        elif c == curses.KEY_UP:
            screen.addstr(2,30,'UP key pressed')
            tilt = tilt - 10
            car.camera.tilt = tilt
            screen.refresh()
        elif c == curses.KEY_DOWN:
            screen.addstr(2,30,'DOWN key pressed')
            tilt = tilt + 10
            car.camera.tilt = tilt
            screen.refresh()
        elif c == ord('w'):   
            screen.addstr(2,30,'W key pressed')
            speed = speed + 10
            car.back_wheels.speed = speed
            screen.refresh()
        elif c == ord('s'):   
            screen.addstr(2,30,'S key pressed')
            speed = speed - 10
            car.back_wheels.speed = speed
            screen.refresh()
        elif c == ord('d'):   
            screen.addstr(2,30,'D key pressed')
            steeringAngle = steeringAngle + 10
            car.front_wheels.angle = steeringAngle
            screen.refresh() 
        elif c == ord('a'):   
            screen.addstr(2,30,'A key pressed')
            steeringAngle = steeringAngle - 10
            car.front_wheels.angle = steeringAngle
            car.back_wheels._left_motor.speed =  car.back_wheels._left_motor.speed +10
            car.back_wheels._right_motor.speed = car.back_wheels._right_motor.speed  -10
            screen.refresh() 
            

    curses.nobreak()
    screen.keypad(False) # Enable keypad Mode
    curses.echo()
    curses.endwin()

       
wrapper(main)    