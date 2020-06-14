#!/usr/bin/env python
# coding: utf-8

# In[11]:


#no 3
def Split(mix):
    ev_li = []
    od_li = []
    for i in mix:
        if (i % 2 == 0):
            ev_li.append(i)
        else:
            od_li.append(i)
        print("Even lists:", ev_li)
        print("odd list:", od_li)


# In[12]:


mix = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Split(mix)


# In[6]:


#no 2 
import re
print('(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', '021531409')))


# In[22]:


#no 1
def Hastag(string):
    x = len(string)
    
    for x in range (len(string)):
        if x<140 and x>=1:
            print('#' + string.title())
    else:
        print(' ')
Hastag('Good luck moron')


# In[23]:


def create_phone_number(numbers):
    for i in range (0,2)
        if i (0,2)
            print ()
    else -


# In[25]:



def Hastag(string):
    x = len(string)
    
    for x in range (len(string)):
        if x<140 and x>=1:
            print('#' + string.title())
    else:
        print(' ')

def remove(string):
    return string.replace(" "."")

string = input()
print(hastag(string))


# In[ ]:




