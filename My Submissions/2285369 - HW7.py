#!/usr/bin/env python
# coding: utf-8

# In[2]:



import numpy as np

import matplotlib.pyplot as plt


#mt1 data
x = np.array([93, 61, 67, 54, 77, 90, 69, 53, 76, 
     71, 93, 82, 41, 51, 91, 48, 31, 52, 
     71, 71, 91, 76, 25, 
     90, 67, 52, 88, 90, 94, 95, 86, 71, 
     44, 80, 61, 31, 68, 76, 30, 26, 83, 
     80, 94, 31, 65, 80, 21, 86, 38, 78, 86, 63, 73, 35, 66, 79, 85, 91, 85, 65, 68, 81, 92, 35, 
     39, 44, 84, 79, 86, 50, 75, 43, 33, 
     86, 97, 100, 38, 67, 71, 76, 58, 36, 
     73, 81, 39, 55, 61, 43, 94, 87, 85, 64,
     59, 77, 60, 62, 65, 92, 47, 87])
#mt2 data
y = np.array([83, 47, 68, 30, 83, 82, 48, 54, 73, 63, 91, 61, 62, 46, 
     69, 49, 52, 72, 37, 56, 72, 54, 22, 68, 48, 36, 75, 84, 
     92, 60, 60, 41, 
     18, 46, 51, 42, 91, 68, 42, 43, 56, 4, 76, 51, 28, 73, 
     49, 63, 37, 78, 67, 50, 64, 4, 56, 65, 90, 87, 69, 58, 55, 74, 93, 42, 42,
     46, 67, 54, 61, 44, 58, 35, 7, 73, 87, 76, 23, 45, 84,
     35, 6, 61, 62, 48, 28, 39, 35, 32, 60, 96, 42, 65, 43, 78, 39, 73, 60, 47, 52, 93])


z = np.linspace(0,100,100)                       # Creating an array with 100 elements for graph purposes 


n = 100                # Total number of elements, basically len(x) or len(y)

sumx = sum(x)          # Sum of mt1 grades
sumy = sum(y)          # Sum of mt2 grades
sumx2 = sum(x**2)      # Sum of mt1^2 grades
sumy2 = sum(y**2)      # Sum of mt2^2 grades
sumxy = sum(x*y)       # Sum of mt1*mt2 grades


sxx = sumx2 - (sumx)**2 / n                      #

sxy = sumxy - sumx * sumy / n                    #

syy = sumy2 - (sumy)**2 / n                      # Total Sum of Squares

ssr = sxy**2 / sxx                               # Sum of squares for regression      

sse = syy-ssr                                    # Sum of squares error    


b = sxy / sxx          # Point estimator of b

a = round(sumy/n - b * sumx / n,2)               # Point esimator of a

b = round(b,2)         # Rounded value of b

t = a+b*z              # The equation y = a+bx  (given t and z to make unique values than former x and y)

colors = np.array(["red","magenta"])

plt.scatter(x,y)                                 # Scattering the plot of midterm grades
plt.plot(z,t)                                    # Line plot of the linear regression
plt.legend(["y = 12.74+0.65x", "mt1-mt2"])       # Adding legends
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Linear Regression Relation with respect to mt and mt2")
plt.savefig("2285369 HW7 plots.pdf")             # Downloading the figure as pdf
plt.show()                                       # Showing the plot

                 

regdf = 1                                        # Regression df = 1

errdf = len(x)-2                                 # Error df = n-2 

df = len(x)-1                                    # total df = n-1

msr = ssr/regdf                                  # Mean squares regression

mse = sse/errdf                                  # Mean squares error

F = msr/mse                                      # F test

r2 = ssr/syy                                     # R square (coefficient of determination)

var = mse                                        # Variation

dev = (var)**(1/2)                               # Deviation

print("the F and r^2 values are {}, {}, respectively".format(round(F,2),round(r2,2)))

#printing the table, fullscreen is advised
print("\nANOVA TABLE:\n\nSource        df         SS               MS            F\nRegression    {}        {}        {}       {}\nError        {}        {}        {}          \nTotal        {}        {}                 \n".format(1,round(ssr,2),round(msr,2),round(msr/mse,2),n-2,round(sse,2),round(mse,2),n-1,round(syy,2)))


# In[ ]:




