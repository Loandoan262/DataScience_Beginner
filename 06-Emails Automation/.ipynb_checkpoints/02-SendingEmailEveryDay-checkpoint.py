#!/usr/bin/env python
# coding: utf-8

# # Sending Email Every Day
# For this purpuse, each company has an ETL system (e.g. Databricks, airflow apache, ...). In this course, we will use PythonAnywhere
# 

# In[15]:


import os
import yagmail
import time
from datetime import datetime as dt


# In[16]:


pw = os.getenv('EMAIL_PASSWORD')


# In[17]:


sender = "minhloan.ftu@gmail.com"
receiver = "loandoan.hsrw@gmail.com"

subject = "This is the subject"

contents = """ 
Here is the content of the email!
"""
while True:
    now = dt.now()
    if now.hour == 21:
        yag = yagmail.SMTP(user=sender, password=os.getenv('EMAIL_PASSWORD'))
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email sent!")
        time.sleep(3600)


# !jupyter nbconvert --to python 02-Sending Email Every Day.ipynb
