import os
import struct
import time
import sys


def launch_test():
    print 'L1_1_1'
    print '---------------------------'
    sys.path.insert(0, 'L1_1_1')
    import L1_1_1
    parent_dir = 'L1_1_1/'
    L1_1_1.script(parent_dir)
    
    print 'L1_1_2'
    print '---------------------------'
    sys.path.insert(0, 'L1_1_2')
    import L1_1_2
    parent_dir = 'L1_1_2/'
    L1_1_2.script(parent_dir)
    
    print 'L1_2_1'
    print '---------------------------'
    sys.path.insert(0, 'L1_2_1')
    import L1_2_1
    parent_dir = 'L1_2_1/'
    L1_2_1.script(parent_dir)
    
    print 'L1_2_2'
    print '---------------------------'
    sys.path.insert(0, 'L1_2_2')
    import L1_2_2
    parent_dir = 'L1_2_2/'
    L1_2_2.script(parent_dir)
    
    print 'L1_3_1'
    print '---------------------------'
    sys.path.insert(0, 'L1_3_1')
    import L1_3_1
    parent_dir = 'L1_3_1/'
    L1_3_1.script(parent_dir)
    
    print 'L1_3_2'
    print '---------------------------'
    sys.path.insert(0, 'L1_3_2')
    import L1_3_2
    parent_dir = 'L1_3_2/'
    L1_3_2.script(parent_dir)
    
    