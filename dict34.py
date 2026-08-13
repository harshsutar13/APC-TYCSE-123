# 34. Take a string, use a dictionary to find the first character that occurs more than once.

text = input("Enter a string: ")

seen = {}
first_repeated = None

for ch in text:
    if ch in seen:
        first_repeated = ch
        break
    seen[ch] = True

if first_repeated:
    print(f"First character occurring more than once: '{first_repeated}'")
else:
    print("No character occurs more than once.")
