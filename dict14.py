# 14. Accept a string from the user and create a dictionary containing each character and its frequency.

text = input("Enter a string: ")

char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1

print("Character Frequency Dictionary:")
print(char_freq)
