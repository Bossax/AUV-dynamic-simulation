
"""
AUV roll/pitch dynamics simulation

Sitthichat 22/1/2021
"""

import numpy as np 
import matplotlib.pyplot as plt
from control.matlab import *

"Roll stability"
X0 = [20,0] # 10 degree, 0 rad/s
Jp = 100     # roll moment of inertia
mass = 500 # kg
B = mass*9.81

time_vector = np.linspace(0,40,400)
#%% effect of metacentric height

Dp = 10
MH = np.linspace(0.1,0.3,3)

plt.figure(1)
for i in range(len(MH)):
    sys = tf(1,[Jp,Dp,B*MH[i]])
    # initial response for the system
    
    yout, T = initial(sys, T = time_vector,X0 = X0)
    plt.plot(T, yout, label='MH = %s m' % MH[i])
    plt.grid()
    plt.xlim((0,40))
  
    plt.title('Impulse response of roll motion')
    plt.xlabel('Time (s)')
    plt.ylabel('Roll (degree)')
    #print("Poles = %s, Zeros = %s"% (pole(sys), zero(sys)))
    
plt.legend()

#%% effect of drag

Dp = np.linspace(10,100,3)
MH = 0.2

plt.figure(2)
for i in range(len(Dp)):
    sys = tf(1,[Jp,Dp[i],B*MH])
    # initial response for the system
    
    yout, T = initial(sys, T = time_vector,X0 = X0)
    plt.plot(T, yout/3.141*180, label='Dp = %s F.s' % Dp[i])
    plt.grid()
    plt.xlim((0,40))
  
    plt.title('Impulse response of roll motion')
    plt.xlabel('Time (s)')
    plt.ylabel('Roll (degree)')
    #print("Poles = %s, Zeros = %s"% (pole(sys), zero(sys)))
    
plt.legend()
