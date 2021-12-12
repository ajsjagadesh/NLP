import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
#nltk.download("wordnet")
pg = "In this essay on computer, we are going to discuss some useful things about computers. The modern-day computer has become an important part of our daily life. Also, their usage has increased much fold during the last decade. Nowadays, they use the computer in every office whether private or government. Mankind is using computers for over many decades now. Also, they are used in many fields like agriculture, designing, machinery making, defense and many more. Above all, they have revolutionized the whole world "

print(pg)
print()
words = nltk.word_tokenize(pg)
print(words)
print()
fdist = FreqDist()
i = 0
for i in words:
    fdist[i] = fdist[i] + 1

print(fdist)
print(fdist.most_common(70))

#print(words)