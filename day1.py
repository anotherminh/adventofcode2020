expenseReport = open('day1-input.txt', 'r')
expenses = list(map(lambda x: int(x), expenseReport.readlines()))
expensesLookup = set(expenses)

targetSum = 2020

def findTwoSum():
    for expense in expenses:
        target = 2020 - expense
        if target in expensesLookup:
            return [target, expense]
    return 'Found nothing'

print(findTwoSum())

def findThreeSum():
    allSums = {}
    for i in range(len(expenses)):
        k = i + 1
        while k < len(expenses):
            total = expenses[i] + expenses[k]
            allSums[2020 - total] = [expenses[i], expenses[k]]
            k += 1

    for expense in expenses:
        if expense in allSums:
            return allSums[expense] + [expense] + [allSums[expense][0] * allSums[expense][1] * expense]
    return 'Found nothing'

print(findThreeSum())

