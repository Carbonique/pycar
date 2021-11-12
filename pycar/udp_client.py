import socket
import sys
import curses
from curses import wrapper

if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)

def send_udp(socket, payload):
    socket.sendto(payload.encode('utf-8'), (ip, port))
    print("\n\n Client Sent : ", payload, "\n\n")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.addstr("PRESS THE ARROW KEYS TO MOVE THE car")

print("Do Ctrl+c to exit the program !!")
while True:
    # Create socket for server
    c = screen.getch()
    if c == curses.KEY_LEFT:
        screen.addstr(0,0, 'left key pressed')
        send_udp(s, "camera_left")
        screen.refresh()
    elif c == curses.KEY_RIGHT:
        screen.addstr(0,0,'right key pressed')
        send_udp(s, "camera_right")
        screen.refresh()
    elif c == curses.KEY_UP:
        screen.addstr(0,0,'UP key pressed')
        send_udp(s, "camera_up")
        screen.refresh()
    elif c == curses.KEY_DOWN:
        screen.addstr(0,0,'DOWN key pressed')
        send_udp(s, "camera_down")
        screen.refresh()
    elif c == ord('w'):   
        screen.addstr(0,0,'Forward/brake key pressed')
        send_udp(s, "forward/brake")
        screen.refresh()
    elif c == ord('s'):   
        screen.addstr(0,0,'Reverse/brake key pressed')
        send_udp(s, "reverse/brake")
        screen.refresh()
    elif c == ord('d'):   
        screen.addstr(0,0,'D key pressed')
        send_udp(s, "car_right")
        screen.refresh() 
    elif c == ord('a'):   
        screen.addstr(0,0,'A key pressed')
        send_udp(s, "car_left")
        screen.refresh() 
    elif c == ord(' '):   
        screen.addstr(0,0,'Space bar pressed')
        send_udp(s, "car_stop")
        screen.refresh() 
# close the socket
s.close()

