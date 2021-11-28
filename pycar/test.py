from pyPS4Controller.controller import Controller
from pyPS4Controller.event_mapping.DefaultMapping import DefaultMapping


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_right(self, value):
        if value == 32767:
            print('test')
        print("on_L3_right: {}".format(value))


class MyEventDefinition(DefaultMapping):

    def __init__(self, **kwargs):
        DefaultMapping.__init__(self, **kwargs)

    # each overloaded function, has access to:
    # - self.button_id
    # - self.button_type
    # - self.value
    # - self.overflow
    # use those variables to determine which button is being pressed
    def L3_x_at_rest(self):
        print(self.overflow)


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.debug = True  # you will see raw data stream for any button press, even if that button is not mapped
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
