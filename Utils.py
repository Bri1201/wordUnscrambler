import json
import itertools

f = open('words_dictionary.json')
data = json.load(f)


def check(word: str):
    flag = 1
    for i in data:
        if i == word:
            return True
            flag = 0
            break
    if flag == 1:
        return False


def anagrams(word: str):
    if len(word) <= 1:
        return word
    else:
        temp = []
        for p in anagrams(word[1:]):
            for i in range(len(word)):
                w = p[:i] + word[0:1] + p[i:]
                if check(w):
                    temp.append(w)
        return temp


def find(w: str):
    word_list = list(w)
    all = []
    for r in range(len(word_list) + 1):
        object1 = itertools.combinations(word_list, r)
        cl = list(object1)
        for i in cl:
            i = list(i)
            st = ""
            all.append(st.join(i))
    all.pop(0)
    final = []
    for i in all:
        if len(i) > 1:
            for k in anagrams(i):
                final.append(k)
    finalset = set(final)
    return finalset
