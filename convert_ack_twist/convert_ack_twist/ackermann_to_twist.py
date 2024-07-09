import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDrive
from geometry_msgs.msg import Twist

class AckermannToTwist(Node):
    def __init__(self):
        super().__init__('ackermann_to_twist')
        self.get_logger().info('Subscribing to ackermann_cmd...')
        self.subscription = self.create_subscription(
            AckermannDrive,
            'ackermann_cmd',
            self.ackermann_callback,
            1)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

    def ackermann_callback(self, msg):
        self.get_logger().info('Entered callback...')
        twist_msg = Twist()
        twist_msg.linear.x = msg.speed
        twist_msg.angular.z = msg.steering_angle
        self.publisher.publish(twist_msg)
        self.get_logger().info('Publishing: linear x =%f, angular z =%f' % (twist_msg.linear.x, twist_msg.angular.z))


def main(args=None):
    rclpy.init(args=args)
    node = AckermannToTwist()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
