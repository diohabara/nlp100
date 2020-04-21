from typing import List
from typing import Mapping
from typing import Union
import random


class Chap01():
    def reverse_str(self, s: str) -> str:
        return s[::-1]

    def get1357(self, s: str) -> str:
        return s[0] + s[2] + s[4] + s[6]

    def concat_two_str(self, s1: str, s2: str) -> str:
        res = ""
        for (c1, c2) in zip(s1, s2):
            res += c1 + c2
        return res

    def get_length_list_of_splitted_words(self, sentence: str) -> List[int]:
        word_list = [x.strip(",.") for x in sentence.split()]
        return list(map(len, word_list))

    def get_map_of_splitted_words(self, sentence: str) -> Mapping[str, int]:
        word_list = [x.strip(",.") for x in sentence.split()]
        map_of_splitted_words = {}
        for idx, word in enumerate(word_list):
            if idx in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
                map_of_splitted_words[word[0]] = idx
            else:
                map_of_splitted_words[word[0:2]] = idx
        return map_of_splitted_words

    def get_ngram(self, s: str, gram_size: int) -> List[str]:
        s = s.replace(" ", "")
        return [
            s[start:start + gram_size]
            for start in range(len(s) + 1 - gram_size)
        ]

    def get_bigram(self, s: str) -> List[str]:
        return self.get_ngram(s, 2)

    def get_template(self, x: Union[int, float, str],
                     y: Union[int, float, str], z: Union[int, float,
                                                         str]) -> str:
        return f"{x}時の{y}は{z}"

    def cipher(self, s: str) -> str:
        res = ""
        for c in s:
            if c.islower():
                res += chr(219 - ord(c))
            else:
                res += c
        return res

    def decipher(self, s: str) -> str:
        return self.cipher(s)

    def get_typoglycemia(self, s: str) -> str:
        words_list = s.split()
        for i in range(len(words_list)):
            if len(words_list[i]) <= 4:
                continue
            words_list[i] = words_list[i][0] + self._get_shuffled_string(
                words_list[i][1:-1]) + words_list[i][-1]
        return str(words_list)

    def _get_shuffled_string(self, s: str) -> str:
        return "".join(random.sample(s, len(s)))
