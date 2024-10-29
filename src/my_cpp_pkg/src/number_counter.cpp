#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

class numberCounterNode : public rclcpp::Node // MODIFY NAME
{
public:
    numberCounterNode() : Node("number_counter") // MODIFY NAME
    {
        subscriber_ this->create_subcription<example_interfaces::msg::Int64>(
            "number", 10,
            std::bind(&numberCounterNode::callbackNumberCounter, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "Smartphone has been started.");
    }


private:
    void callbackNumberCounter(const example_interfaces::msg::Int64::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "%i", msg->data.c_int());
    }
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<numberCounterNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}