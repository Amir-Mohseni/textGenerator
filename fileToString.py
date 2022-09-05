def get_words(address):
    f = open(address, "r", encoding="utf-8")

    words = []
    for line in f.readlines():
        all_words = line.split()
        for word in all_words:
            words.append(word)
    return words
