from simple_launch import SimpleLauncher

sl = SimpleLauncher()
sl.declare_arg('robot', 'turret')


def launch_setup():

    robot = sl.arg('robot')

    sl.robot_state_publisher('stage_troisieme', robot + '.urdf')
    sl.node('stage_troisieme', 'arm_bridge.py')

    sl.rviz(sl.find('stage_troisieme', 'sim.rviz'))

    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)
