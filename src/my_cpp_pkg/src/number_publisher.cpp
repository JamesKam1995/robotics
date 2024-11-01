#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

class NumberPublisher : public rclcpp::Node // MODIFY NAME
{
public:
    NumberPublisher() : Node("number_publisher") // MODIFY NAME
    {
        publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds(500),
                                         std::bind(&NumberPublisher::PublishNumber, this));
        RCLCPP_INFO(this->get_logger(), "number publisher has been started.");
    }

private:
    void PublishNumber()
    {
        auto msg = example_interfaces::msg::Int64();
        msg.data = 1;
        publisher_->publish(msg);
    }
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisher>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}