import os
import csv

# defining the main function for my calculations
def print_percentages(budget_data_csv_path):
    # For readability, it can help to assign your values to variables with descriptive names
    #date = str(budget_data[0])
    # total = int(budget_data[1])
    #averagechange = int(wrestler_data[2])
    #averageincrease = int(wrestler_data[3])
    pass
    
budget_data_csv_path = os.path.join("Pybank","budget_data.csv")

# Open and read csv
with open(budget_data_csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvfile)
    
    #Set variables to zero 
    month_count = 0
    money = 0
    average = 0

    from statistics import mean
    mean= (budget_data_csv_path[1])
    print(mean)

    for row in csv_reader:
        month_count+=1
            

        print(f"Financial Analysis")
        print(f"--------------------")
        print(f"Total Months: {month_count}")
        print(f"Total : {total}")
        print(f"Average Change : {total/month_count}")
        #print(f"Greatest Increase in Profit : {total/month_count}")
        #print(f"Greatest Decrease in Profit : {total/month_count}")
 