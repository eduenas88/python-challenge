import os
import csv

dates= []
profit_losses= []

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

    min = 0
    max = 0

    counter = 0


    for row in csv_reader:
        dates.append(row[0])
        profit_losses.append(int(row[1]))

        month_count+=1
        money+=int(row[1]) 

        if abs(profit_losses[counter]-(profit_losses[counter-1])) > min and profit_losses[counter]<profit_losses[counter-1]:
            min=abs(profit_losses[counter-1]-int(row[1]))
            min_month=row[0]

        if (profit_losses[counter])-(profit_losses[counter-1]) > max and profit_losses[counter]>profit_losses[counter-1] :
            max=profit_losses[counter]-profit_losses[counter-1]
            max_month=row[0]
        counter+=1
        
        
        




           

    print("Financial Analysis")
    print(f"--------------------")
    print(f"Total Months: {month_count}")
    print(f"Total : ${money}")
    #print(f"Average Change : {money/month_count}")
    print(f"Greatest Increase in Profit : {max_month} {max}")
    print(f"Greatest Decrease in Profit : {min_month} ${min*-1}")

 