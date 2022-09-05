from matplotlib import pyplot as plt
from wordcloud import *


def get_words(address):
    f = open(address, "r", encoding="utf-8")

    result = ""
    for line in f.readlines():
        result += line
    return result


text = get_words(address="speech.txt")

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
