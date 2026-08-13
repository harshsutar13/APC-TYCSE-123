# 9. Create a dictionary of programming languages and their creators. Display each key and value using a loop.

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

print("Language -> Creator:")
for lang, creator in languages.items():
    print(f"{lang} : {creator}")
