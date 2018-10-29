# First we'll import the os module
# This will allow us to create file paths across operating systems
print(" ")
print ("Financial Analysis")
print ("-"*20)
print(" ")

import os

# Module for reading CSV files
import csv

# Inserting File path
filepath = os.path.join("..",'PyBank', 'budget_data.csv')

# Improved Reading using CSV module

with open(filepath, newline='') as budget_data_file:

    # CSV reader specifies delimiter and variable that holds contents
    budget_data_file_reader = csv.reader(budget_data_file, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    budget_data_file_header = next(budget_data_file_reader)

    # Creating list of months and list of profit/loss included in the dataset:
    months_list = []
    Profit_loss_list = []
    for row in budget_data_file_reader:
        months_list.append(row[0])
        Profit_loss_list.append(int(row[1]))

# print(f"list of months: {months_list} and {Profit_loss_list}")

# The total number of months included in the dataset
Total_months = len(months_list)
print (f"Total Months: {Total_months}")

# The total net amount of "Profit/Losses" over the entire period
Total_profit_loss = sum(Profit_loss_list)
print (f"Total: ${Total_profit_loss}")

# The average change in "Profit/Losses" between months over the entire period
Average_change = round((Profit_loss_list[-1]-Profit_loss_list[0])/(len(Profit_loss_list)-1),2)
print (f"Average Change: ${Average_change}")

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
profit_loss_change = []
for i in range(len(Profit_loss_list)-1):
    change  = int(Profit_loss_list[i+1])- int(Profit_loss_list[i])
    profit_loss_change.append(change)

greatest_increase = max(profit_loss_change)
greatest_decrease = min(profit_loss_change)
greatest_increase_date = months_list[profit_loss_change.index(greatest_increase)+1]
greatest_decrease_date = months_list[profit_loss_change.index(greatest_decrease)+1]

print (f'Greatest Increase in Profit: {greatest_increase_date} ({greatest_increase})')
print (f'Greatest Decrease in Profit: {greatest_decrease_date} ({greatest_decrease})')

txtpath = '../PyBank/output.txt'

with open(txtpath, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("-"*40)
    text.write("\n")
    text.write('Total Months: %d\n' %Total_months)
    text.write('Total: $%d\n' %Total_profit_loss)
    text.write('Average Change: $%d\n' %Average_change)
    text.write('Greatest Increase in Profit: '+ greatest_increase_date +' ($%d' %greatest_increase+")\n")
    text.write('Greatest Decrease in Profit: '+ greatest_decrease_date +' ($%d' %greatest_decrease+")\n")
