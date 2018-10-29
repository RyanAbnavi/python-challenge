# PyPoll
# Vote-Counting
# First we'll import the os module
# This will allow us to create file paths across operating systems
print(" ")
print ("Election Results")
print ("-"*20)
print(" ")

import os

# Module for reading CSV files
import csv

# Inserting File path
filepath = os.path.join("..",'PyPoll', 'election_data.csv')

# Improved Reading using CSV module

with open(filepath, newline='') as election_data_file:

    # CSV reader specifies delimiter and variable that holds contents
    election_data_file_reader = csv.reader(election_data_file, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    election_data_file_header = next(election_data_file_reader)

    # Creating list of months and list of profit/loss included in the dataset:
    voter_list = []
    county_list = []
    candidate_list = []
    for row in election_data_file_reader:
        voter_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])


# The total number of votes cast
Total_votes = len(voter_list)
print (f"Total votes: {Total_votes}")
print ("-"*20)
print(" ")

# A complete list of candidates who received votes

# print(Unique_candidate_list)

# The percentage of votes each candidate won
def votecount(allvotes):
    # candidate list
    # vote list
    candidates = []
    for i in allvotes:
        if i in candidates:
            continue
        else:
            candidates.append(i)
    vote_count = []
    for i in candidates:
        count = allvotes.count(i)
        vote_count.append(count)
        percent = round(count*100/Total_votes,3)
        print(f'{i}: {percent}% ({count})')
        
    print ("-"*20)

    candidates_votes_tuple = zip(vote_count,candidates)
    candidates_votes_list = list(candidates_votes_tuple)
    candidates_votes_dic = dict(candidates_votes_list)
    winner = candidates_votes_dic[max(vote_count)]
    print(f'Winner: {winner}')
    print ("-"*20)
    print(" ")

votecount(candidate_list)




txtpath = '../PyPoll/output.txt'

with open(txtpath, 'w') as text:
    text.write("Election Results\n")
    text.write("-"*40)
    text.write("\n")
    text.write('Total Votes: %d\r\n' %Total_votes)
    candidates = []
    for i in candidate_list:
        if i in candidates:
            continue
        else:
            candidates.append(i)
    vote_count = []
    for i in candidates:
        count = candidate_list.count(i)
        vote_count.append(count)
        percent = round(count*100/Total_votes,3)
        text.write(i+ ':%' + '%d' %percent + ' (%d'%count+")\n")
    candidates_votes_tuple = zip(vote_count,candidates)
    candidates_votes_list = list(candidates_votes_tuple)
    candidates_votes_dic = dict(candidates_votes_list)
    winner = candidates_votes_dic[max(vote_count)]
    text.write('Winner:'+str(winner))
    text.write("-"*40)
    text.write("\n")
    
    

