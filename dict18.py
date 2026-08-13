# 18. Given two dictionaries, identify the values that are common to both dictionaries.

dict1 = {"a": 10, "b": 20, "c": 30, "d": 40}
dict2 = {"x": 20, "y": 40, "z": 50}

print("Dict 1:", dict1)
print("Dict 2:", dict2)

common_values = set(dict1.values()) & set(dict2.values())
print("Common Values:", list(common_values))
