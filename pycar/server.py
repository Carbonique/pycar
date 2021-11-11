import socket
import sys
from car import Car

if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from  argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
    exit(1)

car = Car()

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

while True:
    print("####### Server is listening #######")
    data, address = s.recvfrom(4096)
    print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")

    if data.decode('utf-8') == "car_left":
        car.front_wheels.turn_left(3)

    if data.decode('utf-8') == "car_right":
        car.front_wheels.turn_right(3)
    
    if data.decode('utf-8') == "camera_right":
        car.camera.right(3)
    
    if data.decode('utf-8') == "camera_left":
        car.camera.left(3)

    if data.decode('utf-8') == "camera_up":
        car.camera.down(3)
    
    if data.decode('utf-8') == "camera_down":
        car.camera.up(3)    

    if data.decode('utf-8') == "forward/brake":
        car.back_wheels.change_speed_by(3)

    if data.decode('utf-8') == "reverse/brake":
        car.back_wheels.change_speed_by(-3)



