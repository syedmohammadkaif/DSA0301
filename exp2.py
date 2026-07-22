from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["caresses", "ponies", "caress", "cats",
         "running", "studies", "happiness", "relational"]

print("Word\t\tStem")
print("-" * 30)

for word in words:
    print(f"{word:15} {ps.stem(word)}")
