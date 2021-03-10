import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

total_months = 0
monthly_profits = []
month = []
sum_of_profits = 0
greatest_increase = 0
greatest_decrease = 0
sum_change_in_profits = 0


with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        total_months += 1
        monthly_profits.append(int(row[1]))
        sum_of_profits += int(row[1])
        month.append(row[0])

change_in_profits = []

for i in range(1,len(monthly_profits)):

    x = monthly_profits[i] - monthly_profits[i - 1]
    change_in_profits.append(int(x))

for i in range(0,len(change_in_profits)):

    sum_change_in_profits += change_in_profits[i]
    average_profit_change = round((sum_change_in_profits / (len(change_in_profits))),2)

for pl in monthly_profits:

    if greatest_decrease == 0:

        greatest_increase == pl
        greatest_decrease == pl

    if pl > greatest_increase:

        greatest_increase = pl

    elif pl < greatest_decrease:

        greatest_decrease = pl

greatest_increase_index = monthly_profits.index(greatest_increase)
greatest_decrease_index = monthly_profits.index(greatest_decrease)

greatest_increase_date = month[greatest_increase_index]
greatest_decrease_date = month[greatest_decrease_index]

print(f"Financial Analysis\n")
print(f"----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${sum_of_profits}\n")
print(f"Average Change: ${average_profit_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}) \n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease}) \n")

output_path = os.path.join('Financial_Analysis.txt')

with open(output_path, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${sum_of_profits}\n")
    file.write(f"Average Change: ${average_profit_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}) \n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease}) \n")

