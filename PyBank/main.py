import csv

path = "Resources/budget_data.csv"
with open(path, 'r') as budgetData:
    budget = csv.reader(budgetData, delimiter=',')
    next(budget)

    totalProfits = 0
    lastValue = 0
    changesList = {}

    for row in budget:
        totalProfits += int(row[1])
        valueChange = int(row[1]) - lastValue
        lastValue = int(row[1])
        changesList[row[0]] = valueChange

    totalMonths = len(changesList)
    average = round((sum([x for x in changesList.values()])/totalMonths), 2)
    greatestIncrease = max(changesList, key=changesList.get)
    greatestDecrease = min(changesList, key=changesList.get)

    output = f"Financial Analysis\n----------------------------\nTotal Months: {totalMonths}\n" \
             f"Total: ${totalProfits}\nAverage Change: ${average}\n" \
             f"Greatest Increase in Profits: {greatestIncrease} (${changesList[greatestIncrease]})\n" \
             f"Greatest Decrease in Profits: {greatestDecrease} (${changesList[greatestDecrease]})"
    print(output)

with open("analysis/output.txt", "w+") as data:
    data.write(output)