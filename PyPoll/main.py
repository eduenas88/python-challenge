import os
import csv

election_data_csv_path = os.path.join("PyPoll","election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first 
    csv_header = next(csvfile)
    
    #set my variables to zero 

    votes = 0 
    khan = 0
    li = 0
    correy = 0
    o_tooley=0

    for row in csv_reader: 
        votes+=1
        if row[2]=='Khan':
            khan+=1
        elif row[2]=='Li': 
            li+=1
        elif row[2]=='Correy':
            correy+=1
        else:
            o_tooley+=1
        pass


print("Election Results")
print(f"--------------------")
print(f'Total Votes: {votes}')
print(f"--------------------")
print(f"Khan : {khan/votes*100:,.3f}% ({khan})")
print(f"Correy : {correy/votes*100:,.3f}% ({correy})")
print(f"Li : {li/votes*100:,.3f}% ({li})")
print(f"O'Tooley : {o_tooley/votes*100:,.3f}% ({o_tooley})")    
print(f"--------------------")    
if khan > li and khan > correy and khan > o_tooley:
    print("Winner: Khan")
elif li > khan and li > correy and li > o_tooley:
    print("Winner: Li")
elif correy > khan and correy > li and correy > o_tooley: 
    print("Winner: Correy")
else:  
    print("Winner: O'Tooley")
print(f"--------------------") 