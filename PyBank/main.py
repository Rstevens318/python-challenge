
#Import Modules
import os
import csv

#Define path to csv file
budget_data = os.path.join("..","PyBank", "Resources", "budget_data.csv")

#Open csv file
with open(budget_data, encoding= 'utf-8') as budget_file:

#Define reader and skip headers
    csvreader = csv.reader(budget_file, delimiter=',')
    csvheader = next(csvreader)
   
#Set Variables
    rowcount = 0
    total = 0
    averageChange = 0
    lastValue = 0
    lastValueChange = []
    monthOfChange = []

#Start Counter 
    for row in csvreader:
#Count Total Rows
        rowcount+= 1
#Count Sum of Profits/Losses
        total+= int(row[1])
#Get Average change in Profits/Losses over the period and take an average
        


print('Total Months:', rowcount)
print('Total:', '$',total)
print(monthOfChange)