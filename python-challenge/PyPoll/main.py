# PyPoll
# Vote-Counting
# First we'll import the os module
# This will allow us to create file paths across operating systems

import os

# Module for reading CSV files
import csv

# header for the results
print(" ")
print ("Election Results")
print ("-"*20)
print(" ")

# Inserting File path
filepath = os.path.join("..",'PyPoll', 'election_data.csv')

# Improved Reading using CSV module

with open(filepath, newline='') as election_data_file:

    # CSV reader specifies delimiter and variable that holds contents
    election_data_file_reader = csv.reader(election_data_file, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    election_data_file_header = next(election_data_file_reader)

    # Creating list of Voter, County and Votes included in the dataset:
    voterID_list = []
    county_list = []
    vote_list = []
    for row in election_data_file_reader:
        voterID_list.append(row[0])
        county_list.append(row[1])
        vote_list.append(row[2])


# The total number of votes cast
Total_votes = len(vote_list)
print (f"Total votes: {Total_votes}")
print ("-"*20)
print(" ")

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# Difine a function which calculate the number of votes and the percent of vote for each candidate 
def votecount(allvotes):
    # allvotes: list of votes
    # candidates: names of candidates
    candidates = []
    for i in allvotes:
        if i in candidates:
            continue
        else:
            candidates.append(i)
    #vote_count: number of votes for each candidate
    vote_count = []
    for i in candidates:
        count = allvotes.count(i)
        vote_count.append(count)
        # percent: percentage of votes each candidate earn
        percent = round(count*100/Total_votes,3)
        print(f'{i}: {percent}% ({count})')
        
    print ("-"*20)

    # finding the winner using a dictionary which shows number of votes for each candidate
    candidates_votes_tuple = zip(vote_count,candidates)
    candidates_votes_list = list(candidates_votes_tuple)
    candidates_votes_dic = dict(candidates_votes_list)
    # And the winner is:
    winner = candidates_votes_dic[max(vote_count)]
    print(f'Winner: {winner}')
    print ("-"*20)
    print(" ")

#callling the function
votecount(vote_list)



#text file address which shows the results
txtpath = '../PyPoll/output.txt'

with open(txtpath, 'w') as text:
    text.write("Election Results\n")
    text.write("-"*40)
    text.write("\n")
    text.write('Total Votes: %d\r\n' %Total_votes)
    candidates = []
    for i in vote_list:
        if i in candidates:
            continue
        else:
            candidates.append(i)
    vote_count = []
    for i in candidates:
        count = vote_list.count(i)
        vote_count.append(count)
        percent = round(count*100/Total_votes,3)
        text.write(i+ ':%' + '%d' %percent + ' (%d'%count+")\n")
    candidates_votes_tuple = zip(vote_count,candidates)
    candidates_votes_list = list(candidates_votes_tuple)
    candidates_votes_dic = dict(candidates_votes_list)
    winner = candidates_votes_dic[max(vote_count)]
    text.write("-"*40+"\n")
    text.write('Winner:'+str(winner)+"\n")
    text.write("-"*40)
    
    

