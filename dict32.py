# 32. Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15, 3, 6]
target = 9

print("Numbers list:", numbers)
print("Target sum:", target)

seen = {}
found = False

for num in numbers:
    complement = target - num
    if complement in seen:
        print(f"Pair found: {complement} + {num} = {target}")
        found = True
        break
    seen[num] = True

if not found:
    print("No two numbers sum to the target value.")
