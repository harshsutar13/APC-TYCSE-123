runs = (45, 72, 30, 100, 56, 80, 25, 67, 90, 40)

total = 0
highest = runs[0]
lowest = runs[0]

for run in runs:
    total = total + run

    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

average = total / len(runs)

print("Total Runs =", total)
print("Highest Score =", highest)
print("Lowest Score =", lowest)
print("Average Score =", average)
