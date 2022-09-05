import fileToString
import random

address = "speech.txt"
words = fileToString.get_words(address)

next_options = dict()
all_words = set()
first_words = set()
last_words = set()

start_of_line = True

for i in range(len(words)):
    word = words[i]
    if start_of_line:
        first_words.add(word)
        start_of_line = False
    if word[-1] in ['.', '?', '!']:
        last_words.add(word)
        start_of_line = True

    if word not in all_words:
        all_words.add(word)
    if i + 1 < len(words):
        next_word = words[i + 1]
        if word in next_options:
            next_options[word].append(next_word)
        else:
            next_options[word] = [next_word]
all_words = list(all_words)
first_words = list(first_words)


def get_next_word(cur_word):
    word_list = []
    occurrences = dict()
    total = 0
    for item in next_options[cur_word]:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
        total += 1
    for (key, value) in occurrences.items():
        word_list.append((value, key))
    word_list.sort()
    p = 0
    probability = []
    for item in word_list:
        cnt = item[0]
        item_probability = cnt / total
        probability.append((p, p + item_probability))
        p += item_probability
    rand_num = random.uniform(0, 1)
    for i in range(len(probability)):
        if rand_num >= probability[i][0] and rand_num <= probability[i][1]:
            return word_list[i][1]
    return word_list[-1][1]


def get_random_sentence():
    current_word = random.choice(first_words)
    result = ""

    while current_word not in last_words:
        result += " " + current_word
        current_word = get_next_word(current_word)
    result += " " + current_word
    return result


print(get_random_sentence())
