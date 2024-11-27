import rclpy
from rclpy.node import Node
from functools import partial

from my_robot_interfaces import SetLed

class BatteryClientNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("battery_client_node") # MODIFY NAME
        self.battery_state = "full"
        self.last_time_battery_state_change =  self.get_current_time_seconds()
        self.battery_timer = self.create_timer(0.1, self.check_battery_state)
        self.get_logger().info("Battery client node has been started")

    def get_current_time_seconds(self):
        secs, nsecs = self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs / 1000000000.0

    def check_battery_state(self):
        time_now = self.get_current_time_seconds()
        if self.battery_state == "full":
            if time_now - self.last_time_battery_state_change > 4.0:
                self.battery_state = "empty"
                self.last_time_battery_state_change = time_now
                self.get_logger().info("Battery is empty! Charging...")
                self.call_set_led_server(3,1)

        else:
            if time_now - self.last_time_battery_state_change > 6.0:
                self.battery_state = "full"
                self.last_time_battery_state_change = time_now
                self.get_logger().info("Battery is full")
                self.call_set_led_server(3,0)

    def call_set_led_server(self, led_number, led_state):
        client = self.create_client(SetLed, "setled")
        while not client.wait_for_service(1.0):
            self.get_logger().info("Waiting for server set led")

        request = SetLed()
        request.led_number = led_number
        request.led_state = led_state

        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_set_led, led_number=led_number, led_state=led_state))
        
    def callback_call_set_led(self, future, led_number, led_state):
        try:
            response = future.result()
            self.get_logger().info(str(response.success))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = BatteryClientNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
