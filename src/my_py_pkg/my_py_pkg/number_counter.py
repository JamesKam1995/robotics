import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class numberCounter(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("number_counter") # MODIFY NAME
        self.robot_name_ = "number_counter_V1"

        #subscriber
        self.subcriber = self.create_subscription(
            Int64, "number", self.callback_number, 10)
        self.get_logger().info("Smartphone has been started.")
        self.counter = 0

        #publisher
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.timer_ = self.create_timer(0.5, self.publish_number_count)
        self.get_logger().info("number_publisher has been started")

    def callback_number(self, msg):
        self.counter += msg.data
        self.get_logger().info(f'Recevied Message : {msg.data}, updated counter : {self.counter}')

    def publish_number_count(self):
        msg = Int64() 
        msg.data = self.counter
        self.publisher_.publish(msg)  
        self.get_logger().info(f'Hi, this is {self.robot_name_} publishing {self.counter}')

def main(args=None):
    rclpy.init(args=args)
    node = numberCounter() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()