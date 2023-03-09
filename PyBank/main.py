
#Import Modules
import os
import csv

#Define path to csv file
budget_data = os.path.join("..","PyBank", "Resources", "budget_data.csv")

#Set Variables
rowcount = 0
total = 0
currentValue = 0
lastValue = 0
valueChanges = 0
monthlyValueChange = []
monthOfChange = []

#Open csv file
with open(budget_data, encoding= 'utf-8') as budget_file:

#Define reader and skip headers
    csvreader = csv.reader(budget_file, delimiter=',')
    csvheader = next(csvreader)

#Start Counter 
    for row in csvreader:
#Count Total Rows
        rowcount += 1
#Count Sum of Profits/Losses
        total += int(row[1])
#Assign current value before looping through rows
        currentValue = int(row[1])
#Start loop
        if rowcount == 1:
#Set last Value at start of loop
            lastValue = currentValue
#Set value change per month and update lists
        else:
        
            valueChanges = currentValue - lastValue

            monthOfChange.append(row[0])

            monthlyValueChange.append(valueChanges)

            lastValue = currentValue
#Get Average of profit/losses
    averageValue = sum(monthlyValueChange)/len(monthOfChange)
#Get Min and Max of monthly profit/loss
    greatestIncrease = max(monthlyValueChange)
    greatestDecrease = min(monthlyValueChange)
#Set the Min and Max in the list
    greatestMonthIncrease = monthlyValueChange.index(greatestIncrease)
    greatestMonthDecrease = monthlyValueChange.index(greatestDecrease)
#Get the month associated with the min and max from the list
    highestMonth = monthOfChange[greatestMonthIncrease]
    lowestMonth = monthOfChange[greatestMonthDecrease]

#Print to terminal to double check work
print('Total Months:', rowcount)
print('Total:', '$',total)
print('%.2f' % averageValue)
print(greatestIncrease)
print(greatestDecrease)
print(highestMonth)
print(lowestMonth)


#Export data to .txt file