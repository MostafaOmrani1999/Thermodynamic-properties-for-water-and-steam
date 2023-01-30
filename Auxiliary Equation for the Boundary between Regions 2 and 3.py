import sys
import numpy as np
import math 
import matplotlib.pyplot as plt

#Reference Constants
R = 0.461526
T_c = 647.096
p_c = 22.064
rho_c = 322

T = float(input(" Enter the value of temperature:"))

n= [0.34805185628969*1000, -0.11671859879975*10, 0.10192970039326*0.01]

p = n[0] + n[1] * (T) + n[2] * (T) * (T)

print(" ")
print("The value of pressure is:")
print(" ")
print(p)