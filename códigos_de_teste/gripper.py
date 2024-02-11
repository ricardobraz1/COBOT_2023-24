import rtde_io
import rtde_receive
import time

rtde_io_ = rtde_io.RTDEIOInterface("10.224.2.69")
rtde_receive_ = rtde_receive.RTDEReceiveInterface("10.224.2.69")


# 0 open the gripper
# 1 close the gripper


#rtde_io_.setStandardDigitalOut(0, False)
rtde_io_.setToolDigitalOut(0, False)

#rtde_io_.setStandardDigitalOut(1, True)
rtde_io_.setToolDigitalOut(1, True)