#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Dependencies
import os
import csv


# In[9]:


# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`
csvpath = os.path.join("Resources", "election_data.csv")


# In[10]:


total_votes = 0
candidate_list = [] # List of all candidate votes by candidate name
counter = 0
unique_cand_list = []
candidate_votes = []
combined_cand_info = []
cand_perc = []
winner_votes = 0
winner_found = False
winner = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    
    # The total number of votes cast
    for row in csvreader:
        total_votes += 1
        
    # Reset to begining of csv file
    csvfile.seek(0)
    csvheader = next(csvfile)
    
    # A complete list of candidates who received votes
    candidate_list = [(cols[2]) for cols in csv.reader(csvfile, delimiter=",")]
  
    # The total number of votes each candidate won
    from collections import Counter
    counter = Counter(candidate_list)
    candidate_votes = list(counter.values()) # [2218231, 704200, 492940, 105630]
    unique_cand_list = list(counter.keys()) # ['Khan', 'Correy', 'Li', "O'Tooley"]

    winner_votes = max(candidate_votes)
    
    # The percentage of votes each candidate won
    for i in range(0, len(unique_cand_list)):
        percentage = (candidate_votes[i] / total_votes) * 100 
        percentage = int(round(percentage))
        cand_perc.append(percentage)
   
    # The winner of the election based on popular vote
    combined_cand_info = zip(unique_cand_list, candidate_votes, cand_perc)
    combined_cand_info = list(combined_cand_info)
    # [('Khan', 2218231, 63), ('Correy', 704200, 20), ('Li', 492940, 14), ("O'Tooley", 105630, 3)]

    for row in combined_cand_info:
        if row[1] == winner_votes:
            winner = row[0]
            winner_found = True
            break


# In[11]:


print("""Election Results
----------------------------
Total Votes: {}
----------------------------""".format(total_votes))
      
for i in range(0, len(unique_cand_list)):
    print("""{}: {}% ({})""".format(unique_cand_list[i], cand_perc[i], candidate_votes[i]))

print("""----------------------------
Winner: {}
----------------------------""".format(winner))


# In[12]:


output_path = os.path.join("new.csv")

with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Votes: ' + str(total_votes)])
    csvwriter.writerow(['----------------------------'])
    for i in range(0, len(unique_cand_list)):
        csvwriter.writerow([str(unique_cand_list[i]) + ': ' + str(cand_perc[i]) + '% (' + str(candidate_votes[i]) + ')'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Winner: ' + str(winner)])
    csvwriter.writerow(['----------------------------'])


# In[ ]:




