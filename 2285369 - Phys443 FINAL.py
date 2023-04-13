#!/usr/bin/env python
# coding: utf-8

# In[1]:


### QUESTION 1  ###

print(" QUESTION 1\n\n\n ")

import math
import matplotlib.pyplot as plt

# the dataset

h = [0.05,0.44,1.23,2.40]     # height
t = [0.1,0.3,0.5,0.7]         # time

N = 4                         # data length

# g = 2 * h / t**2

gexp = [ 2 * h[i] / t[i]**2 for i in range(len(h))]    # experimental g values

### SECTION A, ESTIMATING BEST VALUE OF g ###

# Apporach Method:
# Since the displacement is linearly proportional with gravitational acceleration
# I will be using linear least square fit. Also as each variance is 0.01**2 in height 
# measurement.

# b = y - a * x  where y = g ,and  x = h



sumY = sum(gexp)                                                              #   discrete sum of g                                         

sumX = sum(h)                                                                 #   discrete sum of h 

sumXY = sum([gexp[i] * h[i] for i in range(len(h))   ])                       #   discrete sum of g*h                                            

sumX2 = sum([i**2 for i in h])                                                #   discrete sum of h^2                                                      


a = ((N * sumXY) - (sumX * sumY)) / ((N * sumX2) - (sumX)**2)  # page 30      #   calculation of constant for fit

###

meanY = sumY/len(gexp)                                                        #   mean value of g (experimental)

meanX = sumX/len(h)                                                           #   mean value of h (experimental)

  
# calculating b according to lecture 06, pg.30

b = meanY - a * meanX

# VARIANCE IN THE SLOPE AND INTERCEPT

varX = 0.01**2   # variance in h is stated to be (0.01)^2 in the question
errX = 0.01      # error in h

varY = (N * varX) / (N * sumX2 - sumX**2)      # variance in the intercept
errY = math.sqrt(varY)                         # error in the intercept

varY2 = varX * sumX2 / (N * sumX2 - sumX**2)   # variance in the slope
errY2 = math.sqrt(varY2)                       # error in the slope

print(" Best value of g is {} +-{}".format(round(meanY,3),round(errY,3)))


gFIT = [b + a * i for i in h]       # fit value for gravitational acceleration g


### PLOTTING SECTION ###

# scatters are the experimental values of g, line is the fit.

plt.errorbar(h, gFIT,xerr = errY, yerr = errY2, fmt='-',label = "Fit Value")
plt.errorbar(h,gexp, xerr = errX, fmt = "o", label = "Experimental Value" )
#plt.scatter(h,gexp,label = "Experimental Value")
plt.xlabel("Height")
plt.ylabel("Acceleration")
plt.legend()
plt.grid(linestyle = '--')
plt.show()


### SECTION B, FINDING CHI SQUARE ###

#gth = 9.80665      # theoritical g value

chi2 = sum([ (gexp[i]-gFIT[i])**2 / gFIT[i]   for i in range(len(gexp))])  # chi square calculation according to the lecture 05 and page 10

GOODNES = chi2 / (N-1)

print("Even though the mean error calculated by experiment and the error on the intercept are different by 2 decimals, the value of chi2 per degree of freedom is {}, which is lower than 1 and near to 0. Hence, there is a good agreement.\n\n\n".format(round(GOODNES,4)))



print(" QUESTION 2 \n\n\n")

import random
import matplotlib.pyplot as plt
import math
import numpy as np

e = math.exp(1)                                        # Euler's number for simplicity
c1 = 2 / (1 - e**-2)                                   # Defining the constant in front of pdf for simplicity
r = [i * 10**-3 for i in range(0,1000)]                # range of numbers between 0&1
y = [e**(-2*i) for i in r]      
pdfy = [-math.log(1-(2 * i / c1 )  ) / 2 for i in r]      # pdf



listy = []                                             #
for i in range(10000):                                 #
    listy.append(random.choice(pdfy))                  # Creating a number list of numbers from pdf (y)
    
#z = y[::-1]                                           # Equivalent of not transformed pdf

### CALCULATIONS FOR PDF B ###
a = [i * 10**-3 for i in range(0,1000)]                # Values of x between 0 & 1
b = [i**2 for i in a]                                  # Values of function 0<x<1
pdfb = [i**(1/3) for i in a]                           # Values of pdf for 0<x<1

listb = []                                             # Generation of list of randomly chosen values from the pdf
for i in range(10000):
    listb.append(random.choice(pdfb))

    
SUM = []

for i in range(len(b)):
    SUM.append(b[i] + y[i])
    
    
    
### PLOTTING THE PLOT ###

plt.plot(r,y, label = "P(a)")                         # Pdf plot
plt.plot(r,b, label = "P(b)")                         # plot of the pdf
plt.xlabel("x axis")                                  # labeling the axes
plt.ylabel("The Corresponding Value")                 #
plt.legend()
plt.title("PDF A and B")
plt.grid()
plt.show()

weights = np.ones_like(listy)/float(len(listy)) * 3.7    # Normalizing the histogram to 1
plt.hist(listy, weights=weights, label = "P(a)")  # Plotting random number list histogram which is normalized to 1 
weights2 = np.ones_like(listb)/float(len(listb)) * 3.7   # Normalizing the histogram to 1
plt.hist(listb, weights=weights2, label = "P(b)", alpha = 0.4)  # plot of histogram 
plt.xlabel("Choosen Value")                             # labeling the axes
plt.ylabel("Number of Occurences")                      #
plt.title(" The Value vs Normalized Occurences for PDF")
plt.legend()
plt.grid()
plt.show()




##########################
####### section d ########
##########################



f = [i * 10**-2 for i in range(100)]          # values of f for iterating 

logL = []                                     # will be adding logL values into this list

for i in f[5:95]:                             # iterating through different values of f, to avoid math errors, the boundary is shrinked.
    
    liste = []                                # the list to add discrete Ptot values
    for j in range(19,len(b)-19,20):          # j index values to iterate Pa and Pb to avoid math errors, the boundary is shrinked.
        
        Ptotj = i * y[j] + (1-i) * b[j]       # discrete Ptot values
        liste.append( -math.log(Ptotj ))      # adding Ptot to liste list
                     
    Psum = 0                                  #
    
    for k in liste:                           # adding the logarithms together to get logL for different f
        Psum += k
    logL.append(Psum)
    



##########################
####### section e ########
##########################



z = logL.index(min(logL))                       # the index of minimum logL

fcut1 = f[z+5]                                  # the index of fcut corresponding the minimum logL
#however, as iterating is done in f[5:95], adding 5

delfcut = round(fcut1 - f[81+5],3)              # since (del)logL = 0.5 corresponds to index 81 of logL
# even though fcut is found out to be 0.75, it's wrong, and will be chosing 0.415

print("fcut = {}, delfcut = +- {}".format(fcut1,delfcut))

##########################
####### section f ########
##########################

#fcut = 0.415                          # determined fcut
fcut = fcut1

SUMcut = []

for i in range(len(b)):
    SUMcut.append( (1-fcut) * b[i] + fcut * y[i])
    
mody = [fcut * i for i in y]           # modified y in the function Ptot
modb = [(1-fcut) * i for i in b]       # modified b in the function Ptot


### PLOTTING PTOT USING FCUT ###


plt.plot(r,SUMcut, label = "f = 0.75")
plt.plot(r,mody, label = "P(a)")                 # Pdf plot
plt.plot(r,modb, label = "P(b)")                 # plot of the pdf
plt.xlabel("x axis")                             # labeling the axes
plt.ylabel("The Corresponding Value")            #
plt.legend()
plt.title("PDF with fcut")
plt.grid()
plt.show()




##########################
####### section g ########
##########################


#plotting f vs lnL

plt.plot(f[5:95],logL)
plt.xlabel("f values")
plt.ylabel("-log(L)")
plt.axvline(fcut1)
plt.grid()
plt.title("f vs logL")
plt.show()


##########################
####### section h ########
##########################


print("As seen from the figure above, values lower than 50 passes fcut")

N = 50

print("Total events passing fcut is {}".format(N))
plt.hist(logL,range = (45,50),bins = 8)
plt.ylabel("Events")
plt.xlabel("log(L) values below 50")
plt.grid()




print("\n\n\n")




print(" QUESTION 3 \n\n\n")

import math
import matplotlib.pyplot as plt

###########################
### FIRST CALCULATIONS  ###
###########################

x = [0.7, 0.551]
varX = [0.002**2, 0.005**2]      # error**2 = variance
errX = [0.002, 0.005]            # error on x

v = [10**-16, 0.89]
varV = [10**-32, 0.01**2]  
errV = [10**-16, 0.01]           # error on v (to avoid math errors, instead of 0, 10**-16 is prefered)

m = 0.230                        # mass
errM = 0.001                     # error on the mass

k = 1.03                         # constant
errK = 0.01                      # error on the constant

###########################
###      SECTION A      ###
###########################

E = [ round( (m * v[i]**2 / 2) + (k * x[i]**2 / 2 ),3) for i in range(2)]         # Energy without errors

print("Total energies are {}, and {} for the measurements i and ii, respectively".format(round(E[0],5),round(E[1],5)))

###########################
###      SECTION B      ###
###########################

# CALCULATIONS ARE DONE ACCORDING TO PG.78 ETC.


errKE = [(m * v[i]**2 / 2) * math.sqrt(   (2 * errV[i]  / v[i])**2     +     (errM / m)**2       ) for i in range(2)]  # error on kinetic energy

errPE = [(k * x[i]**2 / 2) * math.sqrt(   (2 * errX[i]  / x[i])**2     +     (errK / k)**2       ) for i in range(2)]  # error on potential energy


errE = [round(math.sqrt(errPE[i]**2 + errKE[i]**2),4)  for i in range(2)]

###########################
###      SECTION C      ###
###########################

print(" The total energies for the first and second measurements with errors are {} +- {}, and {} +- {} respectively".format(E[0],errE[0],E[1],errE[1]))
print(" The total energy seems to be conserved, as both energy measurements have intersections within the error limit. Small losses are possible.")









# In[ ]:




