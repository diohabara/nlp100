import random


def fun00(s: str) -> str:
    return s[::-1]


def fun01(s: str) -> str:
    return s[::2]


def fun02(s1: str, s2: str) -> str:
    res = []
    for (c1, c2) in zip(s1, s2):
        res.append(c1)
        res.append(c2)
    return "".join(res)


def fun03(s: str) -> list[int]:
    word_list = [x.strip(",.") for x in s.split()]
    return list(map(len, word_list))


def fun04(sentence: str) -> dict[str, int]:
    word_list = [x.strip(",.") for x in sentence.split()]
    map_of_splitted_words = {}
    for idx, word in enumerate(word_list):
        if idx in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
            map_of_splitted_words[word[0]] = idx
        else:
            map_of_splitted_words[word[0:2]] = idx
    return map_of_splitted_words


def fun05(s: str, gram_size: int) -> list[str]:
    s = s.replace(" ", "")
    return [s[start : start + gram_size] for start in range(len(s) + 1 - gram_size)]


def fun06(s: str) -> set[str]:
    return set(fun05(s, 2))


def fun07(
    x: int | float | str,
    y: int | float | str,
    z: int | float | str,
) -> str:
    return f"{y} is {z} at {x}"


def fun08_cipher(s: str) -> str:
    res = []
    for c in s:
        if c.islower():
            res.append(chr(219 - ord(c)))
        else:
            res.append(c)
    return "".join(res)


def fun08_decipher(s: str) -> str:
    return fun08_cipher(s)


def fun09(s: str) -> str:
    words_list = s.split()
    for i in range(len(words_list)):
        if len(words_list[i]) <= 4:
            continue
        words_list[i] = words_list[i][0] + _fun09(words_list[i][1:-1]) + words_list[i][-1]
    return " ".join(words_list)


def _fun09(s: str) -> str:
    return "".join(random.sample(s, len(s)))
