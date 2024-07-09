import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDrive

class AckermannPublisher(Node):
    def __init__(self):
        super().__init__('ackermann_publisher')
        self.publisher_ = self.create_publisher(AckermannDrive, 'ackermann_cmd', 1)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = AckermannDrive()
        msg.speed = 1.0  # arbitrary speed value
        msg.steering_angle = 0.5  # arbitrary steering angle value
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: speed=%f, steering_angle=%f' % (msg.speed, msg.steering_angle))

def main(args=None):
    rclpy.init(args=args)
    ackermann_publisher = AckermannPublisher()
    rclpy.spin(ackermann_publisher)
    ackermann_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

