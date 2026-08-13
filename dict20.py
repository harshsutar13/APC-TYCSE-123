# 20. Create a dictionary and display its elements in ascending order of keys.

dict1 = {
    "pune": 90,
    "mumbai": 100,
    "kolhapur": 85,
    "delhi": 95
}

print("Original Dictionary:", dict1)

sorted_dict = dict(sorted(dict1.items()))
print("\nSorted by keys (ascending):")
for key, value in sorted_dict.items():
    print(f"{key} : {value}")
