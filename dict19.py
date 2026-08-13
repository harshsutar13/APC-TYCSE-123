# 19. Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.

dict1 = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

print("Original Dictionary with duplicate values:")
print(dict1)

unique_dict = {}
seen_values = set()

for key, val in dict1.items():
    if val not in seen_values:
        unique_dict[key] = val
        seen_values.add(val)

print("Dictionary after removing duplicate values:")
print(unique_dict)
