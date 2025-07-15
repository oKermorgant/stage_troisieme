#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from math import cos, sin, atan, atan2, acos, sqrt, pi
from tf2_ros import Buffer, TransformListener


class Robot(Node):
    def __init__(self):

        super().__init__('move')

        self.js_sub = self.create_subscription(JointState, 'joint_states', self.js_read, 1)
        self.js = None

        self.t0 = None
        self.position = None
        self.timer = self.create_timer(0.01, self.move)

        self.cmd = JointState()
        self.cmd_pub = self.create_publisher(JointState, '/gui/position_manual', 1)

        self.buffer = Buffer()
        self.listener = TransformListener(self.buffer, node = self)

        self.tf_timer = self.create_timer(1, self.print)

    def sphere(self):
        now = rclpy.time.Time()
        if not self.buffer.can_transform('tool0', 'base_link', now):
            return [0,0,0][:len(self.js.name)]
        p = self.buffer.lookup_transform('tool0', 'base_link', now).transform.translation
        return [p.x,p.y,p.z][:len(self.js.name)]

    def print(self):
        if self.js is None:
            return
        p = ', '.join(f'{v: .2f}' for v in self.sphere())
        print(f'Sphere @ ({p})')

    def q(self):
        return list(self.js.position)

    def now(self):
        s,ns = self.get_clock().now().seconds_nanoseconds()
        if self.t0 is None:
            self.t0 = s + 1e-9*ns
        return s + 1e-9*ns - self.t0

    def js_read(self, msg):
        self.js = msg

    def move(self):
        if self.js is None:
            return
        self.cmd.name = self.js.name
        if len(self.js.name) == 2:
            self.move_rr()
        else:
            self.move_turret()
        if self.position is None:
            return
        self.cmd.position = [float(v) for v in self.position]
        self.cmd_pub.publish(self.cmd)

    def move_rr(self):

        t = self.now()
        d1 = 0.2
        d2 = 0.15

        # TODO have the robot reach a given (x,y,z) position
        self.position = [cos(t), sin(t)]


    def move_turret(self):
        t = self.now()

        d1 = 0.5
        d2 = 0.11

        

        # TODO have the robot reach a given (x,y,z) position

        self.position = [cos(t), sin(t), 0.04*cos(t)]


rclpy.init()
rclpy.spin(Robot())
rclpy.shutdown()

