import numpy as np
import math 

T = float(input(" Enter the value of temperature:"))
p = float(input("Enter the value of pressure:"))

p_star = 1
T_star = 1000
R = 0.461526

pix = p / p_star
tau = T_star / T 

J0 = [0, 1, -3, -2, -1, 2]
n0 = [-13.179983674201, 6.8540841634434, -0.024805148933466, 0.36901534980333, -3.1161318213925, -0.32961626538917]

Ir = [1, 1, 1, 2, 3]
Jr = [0, 1, 3, 9, 3]
nr = [-1.2563183589592E-04, 2.1774678714571E-03, -0.004594282089991, -3.9724828359569E-06, 1.2919228289784E-07]

a0 = 0
for i in range(0, 6):
    a0 = a0 + n0[i] * pow(tau, J0[i])
    
gamma0 = np.log(pix) + a0

gammar = 0
for i in range(0, 5):
    gammar = gammar + nr[i] * pow(pix, Ir[i]) * pow(tau, Jr[i])
    
gamma0_pix = 1/pix

gamma0_tau = 0 
for i in range(0, 6):
    gamma0_tau = gamma0_tau + n0[i] * J0[i] * pow(tau, J0[i] - 1)
    
gammar_pix = 0 
for i in range(0, 5):
    gammar_pix = gammar_pix + nr[i] * Ir[i] *pow(pix, Ir[i] - 1) * pow(tau, Jr[i])
    
gammar_tau = 0
for i in range(0, 5):
    gammar_tau = gammar_tau + nr[i] * pow(pix, Ir[i]) * Jr[i] * pow(tau, Jr[i] - 1)
    
#Gibbs energy
g = R * pow(10, 3) * T * (gammar + gamma0)

#Specific volume
v = R * 1000 * T / (p * 1000000) * pix * (gamma0_pix + gammar_pix)

#Internal energy
u = R * pow(10, 3) * T * (tau * (gamma0_tau + gammar_tau) - pix* (gamma0_pix + gammar_pix))

#Entropy
s = R * (tau * (gamma0_tau + gammar_tau) - gammar - gamma0)

#Enthalpy
h = R * pow(10, 3) * T * (tau * (gamma0_tau + gammar_tau))   
    
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
      
    