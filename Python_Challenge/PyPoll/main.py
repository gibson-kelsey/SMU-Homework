import csv

csvpath = r"Resources\election_data.csv"
print(csvpath)

#inital Total Votes
total_Votes = 0

candidateDict = {}

#read in the file 
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
   

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_Votes = total_Votes + 1

        #row[0] = Voter ID
        #row[1] = County
        #row[2] = Candidate

        #if candidate is in the dictionary
        # then add 1 to the value

        #if the candidate is not in the dictionary
        # creat a new item, initalize value 1 

        candidate = row[2]
        if row[2] in candidateDict.keys():
            candidateDict[candidate] += 1
        else:
            candidateDict[candidate] = 1


#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
winner = max(candidateDict, key=candidateDict.get)
print(winner)

candidate_Strings = [f"{key}: {round((candidateDict[key] / total_Votes)*100,3)}% ({candidateDict[key]})" for key in candidateDict.keys()]
candidate_Strings = "\n".join(candidate_Strings)

summaryString= f"""Election Results
-------------------------
Total Votes: {total_Votes}
-------------------------
{candidate_Strings}
-------------------------
Winner: {winner}
-------------------------
"""
with open("poll_results.txt", "w") as file1:
    file1.write(summaryString)