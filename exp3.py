import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')

ps = PorterStemmer()

with open("sample.txt", "r") as file:
    text = file.read()

words = word_tokenize(text)

stemmed = [ps.stem(word) for word in words]

print("Original Words")
print(words)

print("\nStemmed Words")
print(stemmed)
