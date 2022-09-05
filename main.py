import fileToString
import random

address = "speech.txt"
words = fileToString.get_words(address)


class Node:
    def __init__(self, wrd):
        self.start = self.end = False
        self.word = wrd
        self.next = []
        self.probability = []

    def add_next(self, next_node):
        self.next.append(next_node)


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
node_list = []


def create_graph():
    for wrd in all_words:
        node = Node(wrd)
        if wrd in first_words:
            node.start = True
        if wrd in last_words:
            node.end = True
        node_list.append(node)
        word_list = []
        occurrences = dict()
        total = 0
        for item in next_options[node.word]:
            if item in occurrences:
                occurrences[item] += 1
            else:
                occurrences[item] = 1
            total += 1
        for (key, value) in occurrences.items():
            word_list.append((value, key))
        word_list.sort()
        p = 0
        for item in word_list:
            cnt = item[0]
            item_probability = cnt / total
            node.probability.append((p, p + item_probability))
            node.next.append(item[1])
            p += item_probability


create_graph()


def get_next_word(cur_word):
    node = node_list[all_words.index(cur_word)]
    rand_num = random.uniform(0, 1)
    for i in range(len(node.probability)):
        if node.probability[i][0] <= rand_num <= node.probability[i][1]:
            return node.next[i]
    return node.next[-1]


def get_random_sentence():
    current_word = random.choice(first_words)
    result = ""

    while current_word not in last_words:
        result += " " + current_word
        current_word = get_next_word(current_word)
    result += " " + current_word
    return result


print(get_random_sentence())
