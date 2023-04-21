#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Problem no 1
#write a program to find the area of a trapezium, take the input from the user for the required paramenters.

#solution


a = int(input("Enter base value no 1:"))# a represents the first base of trapezium
b = int(input("Enter base value no 2:")) # b represents the second base of trapezium
height = int(input("Enter height:"))
Area = (a+b)/2 * height
print(Area)



        


# In[16]:


# Problem no 2
#write a program to find the cube of 36. 

#solution
a = 36
print(a*a*a)


# In[17]:


# Problem no 3
# Apply all the types of Arithmetic Operators on the following Variables:
#     a = 40
#     b = 5


a = 40
b = 5
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
print(a//b)


# In[11]:


# Problem no 4

#Write a program to identify if the number given by the user is a 1 digit number, 2 digit number and so on upto 5. 

a = int(input("Please enter the number"))
if a<=9:
    print("Single digit")
    
elif a>=10 and a<=99:
        print("Two digit")
    
    
elif a>=100 and a<=999:
    print("Three digit")
    

elif a>=1000 and a<=9999:
    print("Four digit")
    
    
elif a>=10000 and a<=99999:
    print("Five digit")
    
    
    
    
    
    
    
    
    


# In[17]:


# Problem no 5
#Write a program to create a basic calculator in python.

a = int(input("Please enter no 1:"))
b = int(input("Please enter no 2:"))
print("Type 1 for add")
print("Type 2 for subtract")
print("Type 3 for multiply")
print("Type 4 for divide")

c = int(input("Please enter the number:"))
if c==1:
    print(a+b)
    
elif c==2:
    print(a-b)
    
    
elif c==3:
    print(a*b)
    

elif c==4:
    print(a/b)
    
    
else:
    print("Please check your input")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




