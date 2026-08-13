# 31. Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.

words = ["python", "java", "code", "dictionary", "list", "c", "html"]
print("List of words:", words)

length_dict = {}
for word in words:
    l = len(word)
    if l not in length_dict:
        length_dict[l] = []
    length_dict[l].append(word)

print("\nGrouped by Word Length:")
print(length_dict)
