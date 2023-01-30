import numpy as np
import math 

T = float(input(" Enter the value of temperature:"))
p = float(input("Enter the value of pressure:"))

p_star = 1
T_star = 540
R = 0.461526

pix = p / p_star
tau = T_star / T

J0 = [0, 1, -5, -4, -3, -2, -1, 2, 3]
n0 = [-9.6927686500217, 10.086655968018, -0.005608791128302, 0.071452738081455, -0.40710498223928, 1.4240819171444, -4.383951131945, -0.28408632460772, 0.021268463753307]

Ir = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24]
Jr = [0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58]
nr = [-1.7731742473213E-03, -0.017834862292358, -0.045996013696365, -0.057581259083432, -0.05032527872793, -3.3032641670203E-05, -1.8948987516315E-04, -3.9392777243355E-03, -0.043797295650573, -2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, -3.227767723857E-05, -1.5033924542148E-03, -0.040668253562649, -7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, -1.6714766451061E-11, -2.1171472321355E-03, -23.895741934104, -5.905956432427E-18, -1.2621808899101E-06, -0.038946842435739, 1.1256211360459E-11, -8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, -1.0234747095929E-13, -1.0018179379511E-09, -8.0882908646985E-11, 0.10693031879409, -0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, -4.2002467698208E-06, -5.9056029685639E-26, 3.7826947613457E-06, -1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, -9.436970724121E-07];

a0 = 0
for i in range(0, 9):
    a0 = a0 + n0[i] * pow(tau, J0[i])
    
gamma0 = np.log(pix) + a0

gammar = 0
for i in range(0, 43):
    gammar = gammar + nr[i] * pow(pix, Ir[i]) * pow(tau - 0.5, Jr[i])
    
gamma0_pix = 1/pix

gamma0_tau = 0 
for i in range(0, 9):
    gamma0_tau = gamma0_tau + n0[i] * J0[i] * pow(tau, J0[i] - 1)
    
gammar_pix = 0 
for i in range(0, 43):
    gammar_pix = gammar_pix + nr[i] * Ir[i] *pow(pix, Ir[i] - 1) * pow(tau - 0.5, Jr[i])
    
gammar_tau = 0
for i in range(0, 43):
    gammar_tau = gammar_tau + nr[i] * pow(pix, Ir[i]) * Jr[i] * pow(tau - 0.5, Jr[i] - 1)
    
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
   

    
    

   
    