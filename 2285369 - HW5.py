#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import statistics as st
import math


price = [895,799,831,596,666,825,1263,793,1199,876,1126,1208,785,743,748]
m2 = [200,148,205,125,180,143,275,165,243,202,220,219,123,140,167]

t = 2.145    #t value for %95 confidence level & df = 14
t2 = 4.140   #t value for %99.9 confidence level & df = 14

ratio = [price[i]/m2[i] for i in range(15)]  #list of price/size

mPr = sum(price)/len(price)            #mean of price
SDeviation = st.stdev(price)           #standard dev for price
StDevmPr = SDeviation/math.sqrt(15)    #standard deviation of mean for price
SDevRat = st.stdev(ratio)              #st dev for ratio
mRat = sum(ratio)/len(ratio)           #mean of ratio
StDevmRat = SDevRat/math.sqrt(15)      #standard deviation of mean for ratio

#######        ***ESTIMATION CALCULATIONS***         #######

avgPr = [mPr-t2*StDevmPr,mPr+t2*StDevmPr]       #average estimation for Price
avgRat = [mRat-t2*StDevmRat,mRat+t2*StDevmRat]  #average estimation for Ratio
avgPr2 = [mPr-t*StDevmPr,mPr+t*StDevmPr]         #mean for 95% confidence interval


#### ***OUTPUT*** ###

plt.hist(price)
plt.xlabel('Price Range (TL)')
plt.ylabel('Number of Houses')
plt.grid()

print("""
Average Estimation for Price : {}
Average Estimation for Price/House size Ratio : {}
Mean for %90 confidence interval : {}
""".format(avgPr,avgRat,avgPr2))


# In[ ]:




