from pyPS4Controller.controller import Controller
import socket
import sys

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    def on_R2_press(self, value):
        self.send_udp("forward/brake")

    def on_L2_press(self, value):
        self.send_udp("reverse/brake")

    def on_R3_up(self, value):
        self.send_udp("camera_up")

    def on_R3_down(self, value):
        self.send_udp("camera_down")

    def on_R3_x_at_rest(self, value):
        print(value)

    def on_R3_left(self, value):
        self.send_udp("camera_left")

    def on_R3_right(self, value):
        self.send_udp("camera_right")

    def on_L3_left(self, value):
        self.send_udp("car_left")

    def on_L3_right(self, value):
        self.send_udp("car_right")

    def on_options_press(self):
        self.send_udp("car_stop")

    def send_udp(self, payload):
        self.s.sendto(payload.encode('utf-8'), ("192.168.30.15", 5000))
        print("\n\n Client Sent : ", payload, "\n\n")

#if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
#    ip = sys.argv[1]
#    port = int(sys.argv[2])
#else:
#    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
#    exit(1)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()

s.close()
