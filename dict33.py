# 33. Take a string, use a dictionary to find the first character that occurs only once.

text = input("Enter a string: ")

char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1

first_unique = None
for ch in text:
    if char_freq[ch] == 1:
        first_unique = ch
        break

if first_unique:
    print(f"First character occurring only once: '{first_unique}'")
else:
    print("No non-repeating character found.")
