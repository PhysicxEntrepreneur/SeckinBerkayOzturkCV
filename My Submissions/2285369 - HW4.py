#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import random


x = np.arange(0.1,1,0.01)      #generating exp. dist. function
y= -(np.log(x))                 #

for n in [1,2,5,10,15,20,50]:      #iterating along the values
    
    xNumb = 0
    avgList = []
    RepList = []
    while xNumb <1000:              #making 1000 random choice 
                                    #round(5.76543, 2)
        Z = random.choices(y,k=n)   #making choices "n" times
        avg = sum(Z)/len(Z)         #average values
        avgList.append(round(avg,2))         #adding rounded average values 
        xNumb += 1
    sortedList = sorted(avgList)    #sorting the average list
    NotRepeated = []
    for i in sortedList:            #creating a no duplicate list to 
        if i not in NotRepeated:    #avoid overlaps in the graph
            NotRepeated.append(i)
            
    #creating a  dictionary that includes the average and the frequency
    my_dict = {i:sortedList.count(i) for i in NotRepeated} 
    
    #PLOTTING THE FUNCTION
    plt.bar(list(my_dict.keys()),list(my_dict.values()))
    plt.title('n ={} '.format(n))
    plt.xlabel('Mean')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()
    
    #There is a problem with my graphs but I wasn't able to figure it out.
    #There are no negative values in the average data, but it is represented
    #as if it is in the graph
    #There is another displaying problem which makes it look like there 
    #is a cutoff on the y axis, and the graph lacks to give correct values
    


# In[ ]:




