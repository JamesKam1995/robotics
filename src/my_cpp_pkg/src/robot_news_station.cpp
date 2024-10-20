#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStationNode : public rclcpp::Node // MODIFY NAME
{
public:
    RobotNewsStationNode() : Node("robot_news_station") // MODIFY NAME
    {
        publisher_ = this -> create_publisher <example_interfaces::msg::String>("robot_news", 10);
        timer_ = this -> create_wall_timer(std::chrono::milliseconds(500),
        )
    }

private:
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MyCustomNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}