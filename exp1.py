import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

word = input("Enter an English word: ")

stem = stemmer.stem(word)

print("Original Word:", word)
print("Stemmed Word:", stem)
