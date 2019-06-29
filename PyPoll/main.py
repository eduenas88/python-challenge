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
    output_path = "PyPoll_Analysis.txt"

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

with open(output_path, "w", newline='') as textfile:
    print("Election Results", file=textfile)
    print(f"--------------------", file=textfile)
    print(f'Total Votes: {votes}', file=textfile)
    print(f"--------------------", file=textfile)
    print(f"Khan : {khan/votes*100:.3f}% ({khan})", file=textfile)
    print(f"Correy : {correy/votes*100:.3f}% ({correy})", file=textfile)
    print(f"Li : {li/votes*100:,.3f}% ({li})", file=textfile)
    print(f"O'Tooley : {o_tooley/votes*100:.3f}% ({o_tooley})", file=textfile)    
    print(f"--------------------", file=textfile)   

    if khan > li and khan > correy and khan > o_tooley:
        print("Winner: Khan", file=textfile)
    elif li > khan and li > correy and li > o_tooley:
        print("Winner: Li", file=textfile)
    elif correy > khan and correy > li and correy > o_tooley: 
        print("Winner: Correy", file=textfile)
    else:  
        print("Winner: O'Tooley", file=textfile)

    print(f"--------------------", file=textfile) 

with open(output_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)