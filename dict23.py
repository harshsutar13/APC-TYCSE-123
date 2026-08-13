# 23. Given a list of numbers, create a dictionary containing each unique number and its frequency.

numbers = [1, 2, 2, 3, 4, 3, 2, 1, 5, 4, 1, 2]
print("List of numbers:", numbers)

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1

print("Frequency of unique numbers:")
print(freq)
