#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Q1. Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.
Use the below-given list as an argument for your function.
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
Note: you must extract numeric keys and values of the dictionary also.
'''


# In[7]:


def product_of_numbers(lst):
    flat_lst = []
    for item in lst:
        if isinstance(item, (int, float)):
            flat_lst.append(item)
        elif isinstance(item, (list, tuple, set)):
            flat_lst += [num for num in item if isinstance(num, (int, float))]
        elif isinstance(item, dict):
            flat_lst += [num for num in item.values() if isinstance(num, (int, float))]
    product = 1
    for num in flat_lst:
        product *= num
    return product
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
print(product_of_numbers(list1)) 


# In[4]:





# In[5]:


'''
isinstance() is a built-in Python function that is used to check if an object belongs to a particular class or data type. It takes two arguments: the first is the object that you want to check, and the second is the class or data type that you want to check against.
For example, isinstance(item, int) checks if item is an instance of the int class, and returns True if it is, and False if it is not.

x = 5
if isinstance(x, int):
    print("x is an integer.")
else:
    print("x is not an integer.")

'''


# In[ ]:




