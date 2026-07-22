from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "university",
    "universe",
    "organization",
    "organ",
    "relational",
    "relation",
    "running",
    "runner"
]

print("{:<15}{:<15}".format("Word", "Stem"))
print("-"*30)

for word in words:
    print("{:<15}{}".format(word, ps.stem(word)))
