from std_srvs.srv import Empty 
import rclpy
from rclpy.node import Node


class StartMotor(Node):

    def __init__(self):
        super().__init__('start_motor')
        self.cli = self.create_client(Empty, '/start_motor')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Empty.Request()
        


    def send_request(self):

        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        if self.future.result() is not None:
            self.get_logger().info('Service call succeeded')
        else:
            self.get_logger().error('Service call failed')


def main(args=None):
    rclpy.init(args=args)
    start_node = StartMotor()
    start_node.send_request()
    rclpy.shutdown()


if __name__ == '__main__':
    main()