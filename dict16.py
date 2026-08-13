# 16. Create two dictionaries and merge them into a single dictionary.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

print("Dict 1:", dict1)
print("Dict 2:", dict2)

merged_dict = dict1 | dict2
print("Merged Dictionary:")
print(merged_dict)
