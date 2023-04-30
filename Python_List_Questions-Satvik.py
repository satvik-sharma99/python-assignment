#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Problem no 1
#Python program to interchange first and last elements in a list
a =[10,7,8,23,45,56]
temp = a[0]
length =len(a)
a[0] = a[length - 1]
a[length - 1] = temp
print(a)



# In[36]:


# Problem no 3
#write a program to find length of list without using len()

l =[2,7,9,8,"jaipur"]
count = 0
for x in l:
    count += 1
    print("The length of list is" , count)
    


# In[11]:


# Problem no 4
#Write a python program to check if element exists in list

a =[6,10,11,"jaipur",23.5]
if "jaipur" in a:
    print("The element is found")
else:
    print("The element is not found")


# In[14]:


# Problem no 5
# Write a python program to reverse a list
l1 =[3,7,54,"kota",32]
l1.reverse()
print(l1)


# In[15]:


# Problem no 6
#Write a python program to Count occurrences of an element in a list
l =[2,3,3,4,89,3,5,3]
print(l.count(3))


# In[18]:


# Problem no 7
# Python Program to find sum and average of List in Python
s =[10,45,23,60,90,46]
a = s[0] + s[1] + s[2] +s[3] + s[4] +s[5]
print(a)

#average
h = (a)/6
print(h)


# In[41]:


# Problem no 8
#Write a program to find Sum of  two number digits in List
c = [24,45,8,10,11,2,45]
for i in c:
    if(i>10 and i<100):
        print(i)


# In[43]:


# Problem no 9 and 10
#Python program to find smallest number in a list without using min()
l = [27,45,97,11,10,6,15]
l.sort()
print("The smallest number is:", l[0])
#Python program to find largest number in a list without using max()
print("The largest number is:" ,l[-1])


# In[ ]:





# In[16]:


# Problem no 11
#Python program to print even numbers in a list

l = [2,6,77,3,51,9,84,42]
for i in l:
    if(i%2==0):
        print("The even numbers are" , i)


# In[5]:


# Problem no 12
# Python program to print odd numbers in a list

l = [2,6,77,3,51,9,84,42]
for i in l:
    if(i%2!=0):
        print("The odd numbers are" , i)
        


# In[8]:


# Problem no 13
# Python program to print positive numbers in a list
a = [-1 ,4, 8 , -6 , 10 ,-9]
for i in a:
    if(i>0):
        print("Positive Numbers are", i)

        
        


# In[5]:


# Problem no 14
#Python program to count positive and negative numbers in a list
d = [10,-7,-5,5,4,-8,-9,12]
for i in d:
        if(i>0):
            print("These are positive numbers:" , i)



# In[ ]:





# In[ ]:




