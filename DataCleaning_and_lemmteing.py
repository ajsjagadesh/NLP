import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

pg = "In this essay on computer, we are going to discuss some useful things about computers. The modern-day computer has become an important part of our daily life. Also, their usage has increased much fold during the last decade. Nowadays, they use the computer in every office whether private or government. Mankind is using computers for over many decades now. Also, they are used in many fields like agriculture, designing, machinery making, defense and many more. Above all, they have revolutionized the whole world "

print(pg)
print()

sent = nltk.sent_tokenize(pg)
#print(sent)

lemm =WordNetLemmatizer()

corpus = []

for i in range(len(sent)):
    words = re.sub('[^a-zA-Z]',' ',sent[i])
    words = words.lower()
    words = nltk.word_tokenize(words)
    words = [lemm.lemmatize(w) for w in words if w not in set(stopwords.words('english'))]
    words = ' '.join(words)
    corpus.append(words)

print()
print(corpus)
