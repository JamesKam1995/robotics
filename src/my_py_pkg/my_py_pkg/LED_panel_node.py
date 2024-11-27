import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import LedState
from my_robot_interfaces.srv import SetLed

class LEDPanelNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("led_panel_node") # MODIFY NAME
        self.panel_state_ = [0, 0, 0]

        #publisher
        self.panel_state_publisher_ = self.create_publisher(LedState, "led_panel_state", 10)
        self.timer_ = self.create_timer(3.0, self.publish_led_panel_state)

        #server
        self.server_ = self.create_service(
           SetLed , "set_led", self.callback_set_led)
    
    def publish_led_panel_state(self):
        msg = LedState()
        msg.led_state = self.panel_state_
        self.panel_state_publisher_.publish(msg)

    def callback_set_led(self, request, response):
        led_number = request.led_number
        led_state = request.led_state

        if led_number > len(self.panel_state_) or led_number <= 0:
            response.success = False
            return response
        
        if led_state not in [0, 1]:
            response.success = False
            return response
        
        self.panel_state_[led_number - 1] = led_state
        response.success = True
        return response

def main(args=None):
    rclpy.init(args=args)
    node = LEDPanelNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
