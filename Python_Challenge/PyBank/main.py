import csv
import numpy as np

csvpath = r"Resources\02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv"
print(csvpath)

total_Months = 0
total_Profit = 0

isFirstRow = True
lastRowProfit = 0
changeDict = {}

#read in the file 
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)


        #row[0] = Date
        #row[1] = Profit/Losses

        total_Months +=1
        total_Profit += int(row[1])

        if isFirstRow:
            lastRowProfit =int(row[1])
            isFirstRow = False
        else: 
            change = int(row[1]) - lastRowProfit
            changeDict[row[0]] = change
            lastRowProfit = int(row[1])



averageChange =np.mean(list(changeDict.values()))

maxChangeMonth = max(changeDict, key= changeDict.get)
maxChangeValue = changeDict[maxChangeMonth]

minChangeMonth = min(changeDict, key=changeDict.get)
minChangeValue = changeDict[minChangeMonth]

summaryString= f"""Financial Analysis
-------------------------
Total Votes: {total_Months}
Total: ${total_Profit}
Average Change: ${round(averageChange,2)}
Greatest Increase in Profits: {maxChangeMonth} (${maxChangeValue})
Greatest Decrease in Profits: {minChangeMonth} (${minChangeValue})
"""
with open("bank_results.txt", "w") as file1:
    file1.write(summaryString)
  
   
