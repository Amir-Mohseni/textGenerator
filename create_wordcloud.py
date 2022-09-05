from matplotlib import pyplot as plt
from wordcloud import *


def get_words(address):
    f = open(address, "r", encoding="utf-8")

    result = ""
    for line in f.readlines():
        result += line
    return result


text = get_words(address="speech.txt")

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
