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

    while True:
        c = screen.getch()
        if c == curses.KEY_LEFT:
            screen.addstr(5,10, 'left key pressed')
            car.camera.left(3)
            screen.refresh()
        elif c == curses.KEY_RIGHT:
            screen.addstr(5,50, 'right key pressed')
            car.camera.right(3)
            screen.refresh()
        elif c == curses.KEY_UP:
            screen.addstr(2,30,'UP key pressed')
            car.camera.up(3)
            screen.refresh()
        elif c == curses.KEY_DOWN:
            screen.addstr(2,30,'DOWN key pressed')
            car.camera.down(3)
            screen.refresh()
        elif c == ord('w'):   
            screen.addstr(2,30,'W key pressed')
            car.back_wheels.forward(3)
            screen.refresh()
        elif c == ord('s'):   
            screen.addstr(2,30,'S key pressed')
            car.back_wheels.reverse(3)
            screen.refresh()
        elif c == ord('d'):   
            screen.addstr(2,30,'D key pressed')
            car.front_wheels.turn_right(3)
            screen.refresh() 
        elif c == ord('a'):   
            screen.addstr(2,30,'A key pressed')
            car.front_wheels.turn_left(3)
            screen.refresh() 
            

    curses.nobreak()
    screen.keypad(False) # Enable keypad Mode
    curses.echo()
    curses.endwin()

       
wrapper(main)    