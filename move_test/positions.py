import rtde_control
import rtde_io
import time

rtde_io_ = rtde_io.RTDEIOInterface("10.224.2.69")
rtde_c = rtde_control.RTDEControlInterface("10.224.2.69")


base = [-4.295280639325277, -1.2305423480323334, 2.051667038594381, -5.551773925820822, 1.538703441619873, -2.5057719389544886]

a = [-5.34224516550173, -0.2929087442210694, 0.2897399107562464, 1.5457216936298828, 1.564157485961914, -1.9786604086505335]

b = [-5.3434569279300135, -0.19018550336871343, 0.2919195334063929, 1.4932376581379394, 1.5670888423919678, -1.9786370436297815]

# moviments sequency

rtde_c.moveJ(base)
time.sleep(1)
rtde_c.moveJ(a)
time.sleep(1)
rtde_c.moveJ(b)

# close the gripper
rtde_io_.setToolDigitalOut(1, True)
time.sleep(1)

# return to base

rtde_c.moveJ(a)

rtde_c.moveJ(base)