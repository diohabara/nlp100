from typing import List
from typing import Mapping
from typing import Union
import random


class Chap01():
    """
    00. 文字列の逆順
    文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """

    def reverse_str(self, s: str) -> str:
        return s[::-1]

    """
    01. 「パタトクカシーー
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    """

    def get1357(self, s: str) -> str:
        return s[::2]

    """
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー
    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    """

    def concat_two_str(self, s1: str, s2: str) -> str:
        res = ""
        for (c1, c2) in zip(s1, s2):
            res += c1 + c2
        return res

    """
    03. 円周率
    “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """

    def get_length_list_of_splitted_words(self, sentence: str) -> List[int]:
        word_list = [x.strip(",.") for x in sentence.split()]
        return list(map(len, word_list))

    """
    04. 元素記号
    “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    """

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

    """
    05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
    """

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

    """
    06. 集合
    “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
    written in the test file.
    """

    """
    07. テンプレートによる文生成
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
    """

    def get_template(self, x: Union[int, float, str],
                     y: Union[int, float, str], z: Union[int, float,
                                                         str]) -> str:
        """
        07. Template-based sentence generationPermalink
        Implement a function that receives arguments, x, y, and z and returns a string “{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z, respectively. In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.
        """
        return f"{x}時の{y}は{z}"

    """
    08. 暗号文
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
        英小文字ならば(219 - 文字コード)の文字に置換
        その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """

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

    """
    09. Typoglycemia
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
    """

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
