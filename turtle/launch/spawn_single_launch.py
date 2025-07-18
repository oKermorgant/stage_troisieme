from simple_launch import SimpleLauncher
from simple_launch.events import When, OnProcessExit

def generate_launch_description():

    sl = SimpleLauncher(use_sim_time = False)
    sl.declare_arg('x', 0.)
    sl.declare_arg('y', 0.)
    sl.declare_arg('theta', 0.)
    sl.declare_arg('name', 'turtle')
    sl.declare_arg('target', '')

    # spawn the turtle anyway with name and pose
    # done through a service call in turtlesim
    sl.service('/spawn', request=sl.arg_map('x','y','theta','name'))
    pen = sl.call_service('set_pen', {'off': 1})

    # with sl.group(when = When(pen, OnProcessExit)):
    #     sl.node('stage_troisieme', 'track', parameters = sl.arg_map('target'))

    return sl.launch_description()
