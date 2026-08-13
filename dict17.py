# 17. Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"b": 20, "d": 40, "e": 50}

print("Dict 1:", dict1)
print("Dict 2:", dict2)

common_keys = dict1.keys() & dict2.keys()
print("Common Keys:", list(common_keys))
