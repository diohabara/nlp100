import unittest
from nlp100.chap01 import Chap01


class Chap01Test(unittest.TestCase):
    def setUp(self):
        self.proc = Chap01()

    def test_reverse(self):
        s = "stressed"
        self.assertEqual(self.proc.reverse_str(s), "desserts")

    def test_get1357(self):
        s = "パタトクカシーー"
        self.assertEqual(self.proc.get1357(s), "パトカー")

    def test_concat_two_str(self):
        s1 = "パトカー"
        s2 = "タクシー"
        self.assertEqual(self.proc.concat_two_str(s1, s2), "パタトクカシーー")

    def test_get_length_list_of_splitted_words(self):
        sentence = "Now I need a drink, alcoholic of course, after the heavy \
            lectures involving quantum mechanics."
        self.assertEqual(self.proc.get_length_list_of_splitted_words(sentence),
                         [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9])

    def test_get_map_of_splitted_words(self):
        sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New \
            Nations Might Also Sign Peace Security Clause. Arthur King Can."
        map_of_splitted_words = self.proc.get_map_of_splitted_words(sentence)
        self.assertEqual(map_of_splitted_words["H"], 0)
        self.assertEqual(map_of_splitted_words["He"], 1)

    def test_get_bigram(self):
        sentence = "I am an NLPer"
        self.assertEqual(
            self.proc.get_ngram(sentence, 2),
            ["Ia", "am", "ma", "an", "nN", "NL", "LP", "Pe", "er"])

    def test_set(self):
        """
        06. SetPermalink
        Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” $X$ and $Y$, respectively. Obtain the union, intersection, difference of the two sets. In addition, check whether the bigram “se” is included in the sets $X$ and $Y$
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
        x = 12
        y = "気温"
        z = 22.4
        self.assertEqual(self.proc.get_template(x, y, z), "12時の気温は22.4")

    def test_cipher(self):
        sentence_to_be_cipherd = "Hi He Lied Because Boron Could Not Oxidize \
            Fluorine. New Nations Might Also Sign Peace Security Clause. \
                Arthur King Can."
        ciphered_sentence = self.proc.cipher(sentence_to_be_cipherd)
        self.assertEqual(self.proc.cipher(sentence_to_be_cipherd),
                         ciphered_sentence)
        self.assertEqual(self.proc.decipher(ciphered_sentence),
                         sentence_to_be_cipherd)

    def test_get_typoglycemia(self):
        sentence_to_be_typoed = "I couldn’t believe that I could actually \
            understand what I was reading : the phenomenal power of the human \
                mind."
        self.assertNotEqual(self.proc.get_typoglycemia(sentence_to_be_typoed),
                            sentence_to_be_typoed)


if __name__ == '__main__':
    unittest.main(failfast=False, buffer=False, catchbreak=False)
