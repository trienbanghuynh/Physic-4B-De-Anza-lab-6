import numpy as np
import matplotlib.pyplot as plt

E = 12   # insert a value for the potential of a battery
C = 1   # insert a  value for the capacitance 
R = 1   # insert a value for resistance
t0 = 0  # note that t=0 is t0
q0 = 0  # At t=0, the capacitor has zero charge 
tf = 10 # we will assume final time is 10 seconds
n = 101 # here gives us 100 points from 0 to 10 seconds

# define our delta t function 
def delta(t1,t2,n):
    return (t2 - t1) / (n - 1)

t = np.linspace(t0,tf,n) # set a value for t0,t1,...,tn
q = np.zeros([n]) # set every q-value to zero in an array format

q[0] = q0 # initialize the first point value of output

# perform Euler's method using a for loop
for i in range (0,n):
    q[i] = delta(t0,tf,n) * (-1/(R*C) * q[i-1] + E/R)+ q[i-1]

# print out our values 
for i in range(n):
    print(t[i],q[i])

# initialize input values for exact solution
q_exact = np.zeros([n])

# define a for loop to compute exact solution
for i in range (0,n):
    q_exact[i] = C*E*(1 - np.exp(-t[i] / (R  * C)))
    
# plotting the solution
plt.plot(t,q)

# plot exact solution
plt.plot(t,q_exact)

plt.text(6,6,"R=%.02f" % R)
plt.text(6,5,"C=%.02f" % C)
plt.text(6,4,"E=%.02f" % E)
plt.xlabel("Time (s)")
plt.ylabel("Charge (C)")
plt.title("Approximation of Charge in RC Circuit")
plt.show()

plt.show()
