import nltk
from nltk.stem import PorterStemmer
#from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
#nltk.download("wordnet")
pg = "In this essay on computer, we are going to discuss some useful things about computers. The modern-day computer has become an important part of our daily life. Also, their usage has increased much fold during the last decade. Nowadays, they use the computer in every office whether private or government. Mankind is using computers for over many decades now. Also, they are used in many fields like agriculture, designing, machinery making, defense and many more. Above all, they have revolutionized the whole world "

print(pg)
print()
sent = nltk.sent_tokenize(pg)
print("befor stemming")
print(sent)
print()
stemmer = PorterStemmer()

for i in range(len(sent)):
    words = nltk.word_tokenize(sent[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sent[i] = ' '.join(words)

print()
print("after stemming")
print(sent)