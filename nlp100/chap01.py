from typing import List
from typing import Mapping
from typing import Union
import random


class Chap01():
    def reverse_str(self, s: str) -> str:
        """
        00. Reversed stringPermalink
        Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).
        """
        return s[::-1]

    def get1357(self, s: str) -> str:
        """
        01. “schooled”Permalink
        Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string “schooled”.
        """
        return s[::2]

    def concat_two_str(self, s1: str, s2: str) -> str:
        """
        02. “shoe” + “cold” = “schooled”Permalink
        Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.
        """
        res = ""
        for (c1, c2) in zip(s1, s2):
            res += c1 + c2
        return res

    def get_length_list_of_splitted_words(self, sentence: str) -> List[int]:
        """
        03. PiPermalink
        Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.” into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.
        """
        word_list = [x.strip(",.") for x in sentence.split()]
        return list(map(len, word_list))

    def get_map_of_splitted_words(self, sentence: str) -> Mapping[str, int]:
        """
        04. Atomic symbolsPermalink
        Split the sentence “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.” into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and the first two letters from the other words. Create an associative array (dictionary object or mapping object) that maps from the extracted string to the position (offset in the sentence) of the corresponding word.
        """
        word_list = [x.strip(",.") for x in sentence.split()]
        map_of_splitted_words = {}
        for idx, word in enumerate(word_list):
            if idx in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
                map_of_splitted_words[word[0]] = idx
            else:
                map_of_splitted_words[word[0:2]] = idx
        return map_of_splitted_words

    def get_ngram(self, s: str, gram_size: int) -> List[str]:
        """
        05. n-gramPermalink
        Implement a function that obtains n-grams from a given sequence object (e.g., string and list). Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”
        """
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
        """
        07. Template-based sentence generationPermalink
        Implement a function that receives arguments, x, y, and z and returns a string “{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z, respectively. In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.
        """
        return f"{x}時の{y}は{z}"

    def cipher(self, s: str) -> str:
        """
        08. cipher textPermalink
        Implement a function cipher that converts a given string with the specification:

        Every alphabetical letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
        Keep other letters unchanged
        Use this function to cipher and decipher an English message.
        """
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
        """
        09. TypoglycemiaPermalink
        Write a program with the specification:

        Receive a word sequence separated by space
        For each word in the sequence:
        If the word is no longer than four letters, keep the word unchanged
        Otherwise,
        Keep the first and last letters unchanged
        Shuffle other letters in other positions (in the middle of the word)
        Observe the result by giving a sentence, e.g., “I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”
        """

        words_list = s.split()
        for i in range(len(words_list)):
            if len(words_list[i]) <= 4:
                continue
            words_list[i] = words_list[i][0] + self._get_shuffled_string(
                words_list[i][1:-1]) + words_list[i][-1]
        return str(words_list)
    def _get_shuffled_string(self, s: str) -> str:
        return "".join(random.sample(s, len(s)))
