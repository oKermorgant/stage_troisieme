from simple_launch import SimpleLauncher
from simple_launch.events import When, OnProcessExit


def generate_launch_description():
    
    sl = SimpleLauncher(use_sim_time = False)
    sl.declare_arg('slider', False)
    sl.declare_arg('b', 255)
    sl.declare_arg('g', 0)
    sl.declare_arg('r', 0)
    
    # run turtlesim with turtle1
    params = dict(('background_'+key,sl.arg(key)) for key in 'rgb')
    sl.node('turtlesim', 'turtlesim_node', parameters=params)
    
    # run the open-loop or manual control
    with sl.group(ns='turtle1'):
        
        sl.node('joy', 'joy_node')

        pen = sl.call_service('set_pen', {'off': 1})
        
        with sl.group(if_arg='slider'):
            # manual control
            sl.node('slider_publisher', 'slider_publisher',name='turtle1',
                    arguments=[sl.find('stage_troisieme', 'Turtle.yaml')])
        with sl.group(unless_arg='slider', when = When(pen, OnProcessExit)):
            sl.node('stage_troisieme', 'loop')

    return sl.launch_description()
