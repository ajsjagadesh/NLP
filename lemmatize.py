import nltk
#from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download("averaged_perceptron_tagger")
pg = "In this essay on computer, we are going to discuss some useful things about computers. The modern-day computer has become an important part of our daily life. Also, their usage has increased much fold during the last decade. Nowadays, they use the computer in every office whether private or government. Mankind is using computers for over many decades now. Also, they are used in many fields like agriculture, designing, machinery making, defense and many more. Above all, they have revolutionized the whole world "

print(pg)
print()
sent = nltk.sent_tokenize(pg)
print("befor lemmatize")
print(sent)
print()
#stemmer = PorterStemmer()
lemm =WordNetLemmatizer()

for i in range(len(sent)):
    words = nltk.word_tokenize(sent[i])
    #words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    words = [lemm.lemmatize(w) for w in words if w not in set(stopwords.words('english'))]
    sent[i] = ' '.join(words)

for i in range(len(sent)):
    words = nltk.word_tokenize(sent[i])
    words = nltk.pos_tag(words)
    print(words) 

print()
print("after lemmatize")
print(sent)