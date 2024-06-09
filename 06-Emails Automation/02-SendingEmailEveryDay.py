#!/usr/bin/env python
# coding: utf-8

# # Sending Email Every Day
# For this purpuse, each company has an ETL system (e.g. Databricks, airflow apache, ...). In this course, we will use PythonAnywhere
# 

# In[2]:


import os
import yagmail
import time
from datetime import datetime as dt


# In[3]:


pw = os.getenv('EMAIL_PASSWORD')


# In[4]:


sender = "minhloan.ftu@gmail.com"
receiver = "loandoan.hsrw@gmail.com"

subject = "This is the subject"

contents = """ 
Here is the content of the email!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('EMAIL_PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email sent!")


# **To convert .ipynb to .py, use command below in Terminal:**
# *jupyter nbconvert --to python 02-SendingEmailEveryDay.ipynb*

# # Send email monthly

# In[8]:


sender = "minhloan.ftu@gmail.com"
receiver = "loandoan.hsrw@gmail.com"

subject = "This is the subject"

contents = """ 
Here is the content of the email!
"""
now = dt.now()
if now.day == 22:
    yag = yagmail.SMTP(user=sender, password=os.getenv('EMAIL_PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent!")


# In[ ]:




