from nlp100.chap01 import fun00, fun01, fun02, fun03, fun04, fun05, fun06, fun07, fun08_cipher, fun08_decipher, fun09


def test_fun00() -> None:
    """
    Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).
    """
    assert fun00("stressed") == "desserts"


def test_fun01() -> None:
    """
    Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string “schooled”.
    """
    assert fun01("schooled") == "shoe"


def test_fun02() -> None:
    """
    Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.
    """
    assert fun02("shoe", "cold") == "schooled"


def test_fun03() -> None:
    """
    Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics”. into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.
    """
    assert fun03("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.") == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]


def test_fun04() -> None:
    """
    Split the sentence “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can”. into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and the first two letters from the other words. Create an associative array (dictionary object or mapping object) that maps from the extracted string to the position (offset in the sentence) of the corresponding word.
    """
    assert fun04("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can") == {
        "H": 0,
        "He": 1,
        "Li": 2,
        "Be": 3,
        "B": 4,
        "C": 5,
        "N": 6,
        "O": 7,
        "F": 8,
        "Ne": 9,
        "Na": 10,
        "Mi": 11,
        "Al": 12,
        "Si": 13,
        "P": 14,
        "S": 15,
        "Cl": 16,
        "Ar": 17,
        "K": 18,
        "Ca": 19,
    }


def test_fun05() -> None:
    """
    Implement a function that obtains n-grams from a given sequence object (e.g., string and list). Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”
    """
    assert fun05("I am an NLPer", 2) == [
        "Ia",
        "am",
        "ma",
        "an",
        "nN",
        "NL",
        "LP",
        "Pe",
        "er",
    ]


def test_fun06() -> None:
    """
    Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” X and Y, respectively. Obtain the union, intersection, difference of the two sets. In addition, check whether the bigram “se” is included in the sets X and Y
    """
    X = fun06("paraparaparadise")
    Y = fun06("paragraph")
    assert X | Y == {
        "ad",
        "ag",
        "ap",
        "ar",
        "di",
        "gr",
        "is",
        "pa",
        "ph",
        "ra",
        "se",
    }
    assert X & Y == {
        "ap",
        "ar",
        "pa",
        "ra",
    }
    assert X - Y == {
        "ad",
        "di",
        "is",
        "se",
    }
    assert "se" in X
    assert "se" not in Y


def test_fun07() -> None:
    """
    Implement a function that receives arguments, x, y, and z and returns a string “{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z, respectively. In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.
    """
    assert fun07(12, "temperature", 22.4) == "temperature is 22.4 at 12"


def test_fun08() -> None:
    """
    Implement a function cipher that converts a given string with the specification:

        - Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
        - Keep other letters unchanged

    Use this function to cipher and decipher an English message.
    """
    original = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    converted = "I xlfowm'g yvorvev gszg I xlfow zxgfzoob fmwvihgzmw dszg I dzh ivzwrmt : gsv ksvmlnvmzo kldvi lu gsv sfnzm nrmw ."
    assert fun08_cipher(original) == converted
    assert fun08_decipher(converted) == original


def test_fun09() -> None:
    """
    Write a program with the specification:

    - Receive a word sequence separated by space
    - For each word in the sequence:
        - If the word is no longer than four letters, keep the word unchanged
        - Otherwise,
            - Keep the first and last letters unchanged
            - Shuffle other letters in other positions (in the middle of the word)
    Observe the result by giving a sentence, e.g., “I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind “.
    """
    given = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind"

    def verify(s1: str, s2: str) -> bool:
        l1 = list(s1.split())
        l2 = list(s2.split())
        for i in range(len(l1)):
            w1 = l1[i]
            w2 = l2[i]
            if len(w1) > 4:
                assert w1[0] == w2[0]
                assert w1[-1] == w2[-1]
                assert sorted(w1) == sorted(w2)
            else:
                assert w1 == w2
        return True

    assert verify(given, fun09(given))
