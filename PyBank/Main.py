import pandas as pd
import csv
#load the data
df = pd.read_csv("C:/Users/temmw/python_challenge/PyBank/Resources/budget_data.csv")
# Calculate total months
total_months = df['Date'].count()
    
# Sum of profit/losses
total_amount = df['Profit/Losses'].sum()
    
# Compute changes
df['Change'] = df['Profit/Losses'].diff()
average_change = df['Change'].mean()
    
greatest_increase = df['Change'].max()
greatest_increase_date = df.loc[df['Change'] == greatest_increase, 'Date'].iloc[0]
    
greatest_decrease = df['Change'].min()
greatest_decrease_date = df.loc[df['Change'] == greatest_decrease, 'Date'].iloc[0]

#Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

with open('C:/Users/temmw/Downloads/PyBankanalysis.ipynb', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Financial Analysis"])
        writer.writerow(["----------------------------"])
        writer.writerow([f"Total Months: {total_months}"])
        writer.writerow([f"Total: ${total_amount}"])
        writer.writerow([f"Average Change: ${average_change:.2f}"])
        writer.writerow([f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"])
        writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"])