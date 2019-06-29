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
    min = 0
    max = 0
    i = 0
    total = 0

    for row in csv_reader:
        dates.append(row[0])
        profit_losses.append(int(row[1]))

        month_count+=1
        money+=int(row[1]) 

        if i >= 1:
            total+= profit_losses[i]-(profit_losses[i-1])

        if profit_losses[i]-(profit_losses[i-1]) < min:
            min=profit_losses[i]-(profit_losses[i-1])
            min_month=row[0]

        if (profit_losses[i])-(profit_losses[i-1]) > max:
            max=profit_losses[i]-profit_losses[i-1]
            max_month=row[0]
        i+=1

    print("Financial Analysis")
    print(f"--------------------")
    print(f"Total Months: {month_count}")
    print(f"Total : ${money}")
    print(f"Average Change : (${total/(len(profit_losses)-1):,.2f})")
    print(f"Greatest Increase in Profit : {max_month} (${max})")
    print(f"Greatest Decrease in Profit : {min_month} (${min})")

 