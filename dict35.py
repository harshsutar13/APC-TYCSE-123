# 35. Accept a paragraph and create a dictionary where:
# • Key = word length 
# • Value = number of words having that length.

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
length_count = {}

for word in words:
    cleaned_word = word.strip(".,!?\"'()[]{}")
    if cleaned_word:
        l = len(cleaned_word)
        length_count[l] = length_count.get(l, 0) + 1

print("\nDictionary (Word Length -> Count):")
print(length_count)
