import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class EmergencyStop(Node):
    def __init__(self):
        super().__init__('emergency_stop')
        self.subscriber_ = self.create_subscription(LaserScan, "/scan", self.twist_callback, 10)

        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.twist_msg = Twist()
        

    def twist_callback(self, msg):
        len_front = msg.ranges[0]               # degree(0 ~ 359) == ranges[0 ~ 1079]
        
        if len_front < 0.3:
            self.twist_msg.linear.x = 0.0
            self.twist_msg.angular.z = 0.0
            self.get_logger().warn(" ==Emergency Stop== {:.2f}".format(len_front))
        
        else:
            self.twist_msg.linear.x = 0.3
            self.twist_msg.angular.z = 0.3
            self.get_logger().info(" ====   Safe   ==== {:.2f}".format(len_front))

        self.publisher_.publish(self.twist_msg)






def main(args=None):
    rclpy.init(args=args)
    stop_node = EmergencyStop()
    rclpy.spin(stop_node)
    stop_node.destroy_node()
    rclpy.shutdown()




if __name__ == '__main__':
    main()