
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
#Get Average change in Profits/Losses over the period (Month) and take an average
        currentValue = int(row[1])

        if rowcount == 1:

            lastValue = currentValue

        else:
        
            valueChanges = currentValue - lastValue

            monthOfChange.append(row[0])

            monthlyValueChange.append(valueChanges)

            lastValue = currentValue

    averageValue = sum(monthlyValueChange)/len(monthOfChange)

    greatestIncrease = max(monthlyValueChange)
    greatestDecrease = min(monthlyValueChange)
    greatestMonthIncrease = monthlyValueChange.index(greatestIncrease)
    greatestMonthDecrease = monthlyValueChange.index(greatestDecrease)
    highestMonth = monthOfChange[greatestMonthIncrease]
    lowestMonth = monthOfChange[greatestMonthDecrease]


print('Total Months:', rowcount)
print('Total:', '$',total)
print('%.2f' % averageValue)
print(greatestIncrease)
print(greatestDecrease)
print(highestMonth)
print(lowestMonth)
