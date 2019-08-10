#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
import csv


# In[2]:


csvpath = os.path.join("Resources", "budget_data.csv")


# In[3]:


total_months = 0
total = 0
change = []
avg_change = 0
outlines = []
max_change = 0
min_change = 0
max_found = False
min_found = False
max_month = 0
min_month = 0

# Calculate the total number of months by summing the number of rows
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    
    for row in csvreader:
        total_months = total_months + 1
    
    # Reset to begining of csv file
    csvfile.seek(0)
    csvheader = next(csvfile)
    
    # Calculate the total profit/losses over the entire period by creating a list of float values and summing the values
    profit_loss = [int(cols[1]) for cols in csv.reader(csvfile, delimiter=",")]
    total = sum(profit_loss)
        
    # Calculate the average change by iterating over the profit_loss list and making a new list with the calculated values
    change = [profit_loss[i] - profit_loss[i-1] for i in range(1, len(profit_loss))]
    
    avg_change = sum(change)/len(change)
    
    # Calculate greatest increase in profits by taking a max of the avg_change list
    max_change = max(change)
    
    # Calculate greatest decrease in profits by taking a min of the avg_change list
    min_change = min(change)
    
    # Add 0 value at the begining of the list to make change the same length as the other lists
    change = [0] + change

    # Reset to begining of csv file
    csvfile.seek(0)
    csvheader = next(csvfile)
    
    out_lines = [row + [profit_loss[i]] + [change[i]] for i, row in enumerate(csvreader)]  
    
    for row in out_lines:
        if row[3] == max_change:
            max_month = row[0]
            max_found = True
            break
        
    for row in out_lines:
        if row[3] == min_change:
            min_month = row[0]
            min_found = True
            break


# In[4]:


print("""Financial Analysis
----------------------------
Total Months: {}
Total: ${}
Average Change: ${}
Greatest Increase in Profits: {} (${})
Greatest Decrease in Profits: {} (${})"""
.format(total_months, total, round(avg_change,2), max_month, max_change, min_month, min_change))


# In[5]:


output_path = os.path.join("new.csv")

with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months: ' + str(total_months)])
    csvwriter.writerow(['Total: $' + str(total)])
    csvwriter.writerow(['Average Change: $' + str(round(avg_change,2))])
    csvwriter.writerow(['Greatest Increase in Profits: ' + max_month + ' ($' + str(max_change) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits: ' + min_month + ' ($' + str(min_change) + ')'])


# In[ ]:




