import numpy as np
import math 

T = float(input(" Enter the value of temperature:"))
p = float(input("Enter the value of pressure:"))

# T beyween 273.15 and 623.15 K
# p between 611.213e-6 and 100 Mpa
p_star = 16.53
T_star = 1386
R = 0.461526
 
#Defininf constants
I = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32]
J = [-2, -1, 0, 1, 2, 3, 4, 5, -9, -7, -1, 0, 1, 3, -3, 0, 1, 3, 17, -4, 0, 6, -5, -2, 10, -8, -11, -6, -29, -31, -38, -39, -40, -41]
n= [0.14632971213167, -0.84548187169114, -0.37563603672040 * 10, 0.33855169168385 * 10, -0.95791963387872, 0.15772038513228, -0.16616417199501 * 0.1, 0.81214629983568 * pow(10, -3), 0.28319080123804 * pow(10, -3), -0.60706301565874 * pow(10, -3), -0.18990068218419 * 0.1, -0.32529748770505 * 0.1, - 0.21841717175414 * 0.1, -0.52838357969930 * pow(10, -4), -0.47184321073267 * pow(10, -3), -0.30001780793026 * pow(10, -3), 0.47661393906987 * pow(10, -4), -0.44141845330846 * pow(10, -5), -0.72694996297594 * pow(10, -15), -0.31679644845054 * pow(10, -4), -0.28270797985312 * pow(10, -5), -0.85205128120103 * pow(10, -9), - 0.22425281908000 * pow(10, -5), -0.65171222895601 * pow(10, -6), -0.14341729937924 * pow(10, -12), -0.40516996860117 * pow(10, -6), -0.12734301741641 * pow(10, -8), -0.17424871230634 * pow(10, -9), -0.68762131295531 * pow(10, -18), 0.14478307828521 * pow(10, -19), 0.26335781662795 * pow(10, -22), -0.11947622640071 * pow(10, -22), 0.18228094581404 * pow(10, -23), -0.93537087292458 * pow(10, -25)]

pi = p / p_star
tau = T_star / T 

#Gibbs energy
g = 0
for i in range(0, 34):
    g = g + R * pow(10, 3) * T * (n[i] * pow(7.1 - pi, I[i]) * pow(tau - 1.222, J[i]))
    
# Specific volume
v = 0  
for i in range(0, 34):
    v = v + R * 0.001* pow(10, 3) * (T / (p * pow(10, 6))) * pi * (-n[i] * I[i] * pow(7.1 - pi, I[i] -1) * pow(tau - 1.222, J[i]))
    
#Internal energy
u = 0
for i in range(0, 34):
    u = u + R * 1000 * T *(tau * n[i] * pow(7.1 - pi, I[i]) * J[i] * pow(tau - 1.222, J[i] -1) + pi * (n[i] * I[i] * pow(7.1 - pi, I[i] -1) * pow(tau - 1.222, J[i])))
    
#Entropy
s = 0
for i in range(0, 34):
    s = s + R  * (tau * n[i] * pow(7.1 - pi, I[i]) * J[i] * pow(tau - 1.222, J[i] -1) - n[i] * pow(7.1 - pi, I[i]) * pow(tau - 1.222, J[i]))

#Enthalpy
h = 0
for i in range(0, 34):
    h = h + R * 1000  * T * tau * n[i] * pow(7.1 - pi, I[i]) * J[i] * pow(tau - 1.222, J[i] -1)

print("Specific Volume is:")
print("")
print(v)
print("")
print("Specific Internal energy is:")
print("")
print(u)
print("")
print("Specific Entropy is:")
print("")
print(s)
print("")
print("Specific Enthalpy is:")
print("")
print(h)
print("")  
   