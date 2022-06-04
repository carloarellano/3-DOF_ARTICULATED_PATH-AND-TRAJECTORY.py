#PATH AND TRAJECTORY60

from os import *
import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

# link lenths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))


# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)


# Create Links
Arti_Elbow = DHRobot([
    RevoluteDH(a1,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a2,0,0,qlim=[(-20/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a3,0,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    ], name='Articulated')

print(Arti_Elbow)

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi

#ARE ANG NABABAGO
# q Paths
#JOINT VARAIBLE = ([T1, T2, T3, 0])
q0 = np.array([0,0,0])
q1 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = ")))
                ])

q2 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = ")))
                ])

q3 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = "))
                )])

q4 = np.array([deg_to_rad(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = "))
                )])
#new q path
#q_init = np.array([0,0,0])
#q_pick = np.array([deg_to_rad(float(input("T1 = "))),
#                deg_to_rad(float(input("T2 = "))),
#                deg_to_rad(float(input("T3 = ")))
#                ])

# Trajectory commands (VELOCITY)
traj1 = rtb.jtraj(q0,q1,50)
traj2 = rtb.jtraj(q1,q2,50)
traj3 = rtb.jtraj(q2,q3,50)
traj4 = rtb.jtraj(q3,q4,50)
# new trajectory commands

#traj1 = rtb.jtraj(q_init,q_pick,10) #time vector or steps
#print(traj1)
#print(traj1.q)

#plot scale
x1 = - 0.1
x2 = 0.1
y1 = - 0.1
y2 = 0.1
z1 = - 0.1
z2 = 0.1

# for joint variable vs. time(s) table
#rtb.qplot(traj1.q)
#rtb.qplot(traj2.q)
#rtb.qplot(traj3.q)

#PLOT COMMAND
Arti_Elbow.plot(traj1.q, limits=[x1,x2,y1,y2,z1,z2]) 
Arti_Elbow.plot(traj2.q, limits=[x1,x2,y1,y2,z1,z2])
Arti_Elbow.plot(traj3.q, limits=[x1,x2,y1,y2,z1,z2])
Arti_Elbow.plot(traj4.q, limits=[x1,x2,y1,y2,z1,z2], block=True)
#SCARA_V3.teach(jointlabels=1)