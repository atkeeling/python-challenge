#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


infile = os.path.join("election_data.csv")
infile


# In[3]:


with open(infile,"r") as csv_file:
    total_votes = sum(1 for line in csv_file) - 1
print(f"Total votes = {total_votes}")


# In[4]:


candidates = []

with open(infile,"r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader)
    for row in reader:
        if row[2] not in candidates:
            candidates.append(row[2])
candidates


# In[5]:


votes = []

with open(infile,"r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader)
    for row in reader:
        votes.append(row[2])


# In[6]:


khan = votes.count("Khan")
correy = votes.count("Correy")
li = votes.count("Li")
otooley = votes.count("O'Tooley")
maxvotes = max([khan,correy,li,otooley])
if maxvotes == khan:
    winner = "Khan"
if maxvotes == correy:
    winner = "Correy"
if maxvotes == li:
    winner = "Li"
if maxvotes == otooley:
    winner = "O'Tooley"
winner


# In[7]:


khan_pc = khan/total_votes 
correy_pc = correy/total_votes
li_pc = li/total_votes
otooley_pc = otooley/total_votes


# In[8]:


print(f"Total number of votes = {total_votes}")
print(f"Khan received {khan:,} votes which was {khan_pc*100:.0f}% of the total")
print(f"Correy received {correy:,} votes which was {correy_pc*100:.0f}% of the total")
print(f"Li received {li:,} votes which was {li_pc*100:.0f}% of the total")
print(f"O'Tooley received {otooley:,} votes which was {otooley_pc*100:.0f}% of the total")
print(f"The winner is {winner}.")


# In[9]:


output_path = os.path.join("poll_output.txt")

with open(output_path, 'w', newline='') as textfile:
    textfile.write(f"Total number of votes = {total_votes:,}\n"
                    f"Khan received {khan:,} votes which was {khan_pc*100:.0f}% of the total\n"
                    f"Correy received {correy:,} votes which was {correy_pc*100:.0f}% of the total\n"
                    f"Li received {li:,} votes which was {li_pc*100:.0f}% of the total\n"
                    f"O'Tooley received {otooley:,} votes which was {otooley_pc*100:.0f}% of the total\n"
                    f"The winner is {winner}.\n")


# In[ ]:




