import numpy as np
import math 

#Reference Constants
R = 0.461526
T_c = 647.096
p_c = 22.064
rho_c = 322

T = float(input(" Enter the value of temperature:"))
rho = float(input("Enter the value of density:"))

p_star = p_c
T_star = T_c
rho_star = rho_c
R = 0.461526

tau = T_star / T
delta = rho / rho_star

I = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11];
J = [0, 0, 1, 2, 7, 10, 12, 23, 2, 6, 15, 17, 0, 2, 6, 7, 22, 26, 0, 2, 4, 16, 26, 0, 2, 4, 26, 1, 3, 26, 0, 2, 26, 2, 26, 2, 26, 0, 1, 26];
n = [1.0658070028513, -15.732845290239, 20.944396974307, -7.6867707878716, 2.6185947787954, -2.808078114862, 1.2053369696517, -8.4566812812502E-03, -1.2654315477714, -1.1524407806681, 0.88521043984318, -0.64207765181607, 0.38493460186671, -0.85214708824206, 4.8972281541877, -3.0502617256965, 0.039420536879154, 0.12558408424308, -0.2799932969871, 1.389979956946, -2.018991502357, -8.2147637173963E-03, -0.47596035734923, 0.0439840744735, -0.44476435428739, 0.90572070719733, 0.70522450087967, 0.10770512626332, -0.32913623258954, -0.50871062041158, -0.022175400873096, 0.094260751665092, 0.16436278447961, -0.013503372241348, -0.014834345352472, 5.7922953628084E-04, 3.2308904703711E-03, 8.0964802996215E-05, -1.6557679795037E-04, -4.4923899061815E-05];

a0 = n[0] * np.log(delta)

b0 = 0
for i in range(1, 40):
    b0 = b0 + n[i] * pow(delta, I[i]) * pow(tau, J[i])
    
phi = a0 + b0

c0 = n[0] / delta    
d0 = 0
for i in range(1, 40):
    d0 = d0 + n[i] * I[i] * pow(delta, I[i] - 1) * pow(tau, J[i])
    
phi_delta = d0 + c0

phi_tau = 0 
for i in range(1, 40):
    phi_tau = phi_tau + n[i] * pow(delta, I[i]) * J[i] * pow(tau, J[i] - 1)

#Helmholtz energy    
f = R * pow(10, 3) * T * ( a0 + b0)

# Pressure
p = rho * 0.001 * R * T * delta * phi_delta

#Internal energy
u = R * T  * tau * phi_tau

#Entropy
s = R * ( tau * phi_tau - phi)

#Enthalpy
h = R * T * (tau * phi_tau + delta * phi_delta)

print("Pressure is:")
print("")
print(p)
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
   


    