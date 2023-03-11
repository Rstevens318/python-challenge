
#Import Modules
import os
import csv

#Define path to csv file
poll_data = os.path.join("..","Pypoll", "Resources", "election_data.csv")

#Open csv file
with open(poll_data) as poll_file:
    csvreader = csv.DictReader(poll_file, delimiter= ',')
    
    rowcount = 0
    voteCount = [] 
    votes = []  

   
    for row in csvreader:

        rowcount+= 1

        voteCount.append(row['Candidate'])

charles  = voteCount.count('Charles Casper Stockham')
diana = voteCount.count('Diana DeGette') 
raymon = voteCount.count('Raymon Anthony Doane')  

votes.append(charles)
votes.append(diana)
votes.append(raymon)

charlesPerc = (charles/rowcount) * 100
dianaPerc = (diana/rowcount) * 100
raymonPerc = (raymon/rowcount) * 100

highVotes = max(votes)

if highVotes == charles:
    winner = 'Charles Casper Stockham'

elif highVotes == diana:
    winner = 'Diana DeGette'

elif highVotes == raymon:
    winner = 'Raymon Anthony Doane'

    

print(rowcount)      
print(f'{charles} and {"%.2f" % charlesPerc}')
print(f'{diana} and {"%.2f" % dianaPerc}')
print(f'{raymon} and {"%.2f" % raymonPerc}')
print(winner)
 

    



