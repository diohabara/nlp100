import unittest
from nlp100.chap01 import Chap01


class Chap01Test(unittest.TestCase):
    def setUp(self):
        self.proc = Chap01()

    def test_reverse(self):
        """
        00. 文字列の逆順
        文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
        """
        s = "stressed"
        self.assertEqual(self.proc.reverse_str(s), "desserts")

    def test_get1357(self):
        """
        01. 「パタトクカシーー
        「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
        """
        s = "パタトクカシーー"
        self.assertEqual(self.proc.get1357(s), "パトカー")

    def test_concat_two_str(self):
        """
        02. 「パトカー」＋「タクシー」＝「パタトクカシーー
        「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
        """
        s1 = "パトカー"
        s2 = "タクシー"
        self.assertEqual(self.proc.concat_two_str(s1, s2), "パタトクカシーー")

    def test_get_length_list_of_splitted_words(self):
        """
        03. 円周率
        “Now I need a drink, alcoholic of course,\
        after the heavy lectures involving quantum mechanics.”\
        という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
        """
        sentence = "Now I need a drink, alcoholic of course, after the heavy \
            lectures involving quantum mechanics."
        self.assertEqual(self.proc.get_length_list_of_splitted_words(sentence),
                         [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9])

    def test_get_map_of_splitted_words(self):
        """
        04. 元素記号
        “Hi He Lied Because Boron Could Not Oxidize Fluorine.\
        New Nations Might Also Sign Peace Security Clause. Arthur King Can.”\
        という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，\
        それ以外の単語は先頭に2文字を取り出し，\
        取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
        """
        sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New \
            Nations Might Also Sign Peace Security Clause. Arthur King Can."
        map_of_splitted_words = self.proc.get_map_of_splitted_words(sentence)
        self.assertEqual(map_of_splitted_words["H"], 0)
        self.assertEqual(map_of_splitted_words["He"], 1)

    def test_get_bigram(self):
        """
        05. n-gram
        与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．\
        この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
        """
        sentence = "I am an NLPer"
        self.assertEqual(
            self.proc.get_ngram(sentence, 2),
            ["Ia", "am", "ma", "an", "nN", "NL", "LP", "Pe", "er"])

    def test_set(self):
        """
        06. 集合
        “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，\
        それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．\
        さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
        written in the test file.
        """
        s1 = "paraparaparadise"
        s2 = "paragraph"
        X = self.proc.get_bigram(s1)  # s1's bi-gram
        Y = self.proc.get_bigram(s2)  # s2's bi-gram
        set_X = set(X)
        set_Y = set(Y)
        self.assertEqual(set_X & set_Y, {"pa", "ar", "ra", "ap"})
        self.assertEqual(
            set_X | set_Y,
            {"di", "ph", "ra", "ar", "ad", "is", "se", "ag", "pa", "gr", "ap"})
        self.assertEqual(set_X - set_Y, {"is", "di", "se", "ad"})

    def test_get_template(self):
        """
        07. テンプレートによる文生成
        引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．\
        さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
        """
        x = 12
        y = "気温"
        z = 22.4
        self.assertEqual(self.proc.get_template(x, y, z), "12時の気温は22.4")

    def test_cipher(self):
        """
        08. 暗号文
        与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
            英小文字ならば(219 - 文字コード)の文字に置換
            その他の文字はそのまま出力
        この関数を用い，英語のメッセージを暗号化・復号化せよ．
        """
        sentence_to_be_cipherd = "Hi He Lied Because Boron Could Not Oxidize \
            Fluorine. New Nations Might Also Sign Peace Security Clause. \
                Arthur King Can."
        ciphered_sentence = self.proc.cipher(sentence_to_be_cipherd)
        self.assertEqual(self.proc.cipher(sentence_to_be_cipherd),
                         ciphered_sentence)
        self.assertEqual(self.proc.decipher(ciphered_sentence),
                         sentence_to_be_cipherd)

    def test_get_typoglycemia(self):
        """
        09. Typoglycemia
        スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．\
        ただし，長さが４以下の単語は並び替えないこととする．\
        適当な英語の文（例えば”I couldn’t believe that I could actually understand \
        what I was reading : the phenomenal power of the human mind .”）\
        を与え，その実行結果を確認せよ．
        """
        sentence_to_be_typoed = "I couldn’t believe that I could actually \
            understand what I was reading : the phenomenal power of the human \
                mind."
        self.assertNotEqual(self.proc.get_typoglycemia(sentence_to_be_typoed),
                            sentence_to_be_typoed)


if __name__ == '__main__':
    unittest.main(failfast=False, buffer=False, catchbreak=False)
