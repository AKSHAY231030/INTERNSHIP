#!/usr/bin/env python
# coding: utf-8

# 11.Write a python program to find the factorial of a number

# In[1]:


def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial(number)}")


# 12.	Write a python program to find whether a number is prime or composite

# In[2]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
result = "prime" if is_prime(number) else "composite"
print(f"{number} is a {result} number.")


# 13.	Write a python program to check whether a given string is palindrome or not. 

# In[3]:


user_input = input("Enter a string: ")

if user_input.lower() == user_input.lower()[::-1]:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")


# 14.	Write a Python program to get the third side of right-angled triangle from two given sides

# In[4]:


side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))

third_side = (side1**2 + side2**2)**0.5

print(f"The length of the third side is: {third_side}")


# 15.	Write a python program to print the frequency of each of the characters present in a given string.

# In[5]:


user_input = input("Enter a string: ")

frequency_dict = {char: user_input.count(char) for char in set(user_input) if char.isalnum()}

for char, count in frequency_dict.items():
    print(f"'{char}' appears {count} times.")


# In[ ]:





# In[ ]:




