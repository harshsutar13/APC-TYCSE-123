temperatures = (32, 35, 31, 30, 36, 34, 33)

total = 0

maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    total = total + temp

    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = total / len(temperatures)

print("Maximum Temperature =", maximum)
print("Minimum Temperature =", minimum)
print("Average Temperature =", average)
