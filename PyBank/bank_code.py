#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


infile = os.path.join("budget_data.csv")
infile


# In[3]:


with open(infile,"r") as csv_file:
    count_months = sum(1 for line in csv_file) - 1
print(f"Number of months = {count_months}")


# In[4]:


net_profit = 0

with open(infile,"r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader)
    for row in reader:
        net_profit = net_profit + float(row[1])
print(f"Net profit = ${net_profit:,.2f}")


# In[5]:


avg_profit = net_profit/count_months
print(f"Average profit = ${avg_profit:,.2f}")


# In[6]:


max_profit = 0
maxp_month = ""
max_loss = 0
maxl_month = ""

with open(infile,"r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader)
    for row in reader:
        if float(row[1]) > max_profit:
            max_profit = float(row[1])
            maxp_month = row[0]
        if float(row[1]) < max_loss:
            max_loss = float(row[1])
            maxl_month = row[0]
print(f"Max profit = ${max_profit:,.2f} in {maxp_month}")
print(f"Max loss = ${max_loss:,.2f} in {maxl_month}")


# In[7]:


output_path = os.path.join("bank_output.txt")

with open(output_path, 'w', newline='') as textfile:
    textfile.write(f"Number of months = {count_months}\n")
    textfile.write(f"Net profit = ${net_profit:,.2f}\n")
    textfile.write(f"Average profit = ${avg_profit:,.2f}\n")    
    textfile.write(f"Max profit = ${max_profit:,.2f} in {maxp_month}\n")
    textfile.write(f"Max loss = ${max_loss:,.2f} in {maxl_month}\n")

