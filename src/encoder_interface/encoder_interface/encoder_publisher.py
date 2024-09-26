#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial
import time

class EncoderPublisher(Node):
    def __init__(self):
        super().__init__('encoder_publisher')
        self.publisher = self.create_publisher(JointState, 'joint_states', 10)
        self.serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=2) #change port as required
        self.get_logger().info('Encoder publisher has been started')
        
    def publish_joint_states(self):
        while not self.serial_port.in_waiting:
            time.sleep(0.01)
            
        line = self.serial_port.readline().decode('utf-8')
        angles = line.strip().split(',')
        joint_state = JointState()
        joint_state.name = ['joint1', 'joint2']
        joint_state.position = [float(angle) for angle in angles]
        joint_state.header.stamp = self.get_clock().now().to_msg()
        
        self.publisher.publish(joint_state)
        self.get_logger().info(f"Published joint states: {joint_state.position}")

def main(args=None):
    rclpy.init(args=args)
    encoder_publisher = EncoderPublisher()
    try:
        while rclpy.ok():
            encoder_publisher.publish_joint_states()
    except KeyboardInterrupt:
        pass
    finally:
        encoder_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()