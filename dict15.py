# 15. Accept a sentence and create a dictionary containing each word and the number of times it occurs.

sentence = input("Enter a sentence: ")

words = sentence.split()
word_freq = {}

for word in words:
    word = word.strip(".,!?").lower()
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequency Dictionary:")
print(word_freq)
