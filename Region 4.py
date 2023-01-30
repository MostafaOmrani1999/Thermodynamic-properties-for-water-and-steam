import numpy as np

#Reference Constants
R = 0.461526
T_c = 647.096
p_c = 22.064
rho_c = 322

T_s = float(input(" Enter the value of temperature:"))

#Saturation line

r_s = T_s + (-0.23855557567849) / (T_s - 0.65017534844798 * 1000)
A = (r_s) * (r_s) + 0.11670521452767 * 10000 * r_s -0.72421316703206 * 1000000 
B = - 0.17073846940092 * 100 * r_s * r_s + 0.12020824702470 * 100000 * r_s -0.32325550322333 * 10000000
C = 0.14915108613530 * 100 * r_s * r_s - 0.48232657361591 * 10000 * r_s + 0.40511340542057 * 1000000

#Pressure
p_s = np.power((2 * C) / (-B + np.sqrt(B * B - 4 * A * C)), 4)

print(" ")
print("The value of saturation pressure at this temperature is:")
print(" ")
print(p_s)