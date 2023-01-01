"""Chapter 2: UNIX Commands
The file popular-names.txt stores names of babies born in US with their genders, numbers of births, and years of births in tab-separated format. Create a program with the specifications below. Run the program with popular-names.txt as an input. Furthermore, confirm that the same (similar) result can be obtained by running a UNIX command.
"""


import subprocess

from nlp100.chap02 import fun10, fun11, fun12, fun13


def test_fun10() -> None:
    """
    Write a function that counts the number of lines in a file
    """
    expected = subprocess.run(
        ["wc", "-l", "data/popular-names.txt"], capture_output=True, text=True
    ).stdout.split()[0]
    assert fun10() == int(expected)


def test_fun11() -> None:
    """
    Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.
    """
    expected = subprocess.run(
        ["cat", "data/popular-names.txt"], capture_output=True, text=True
    ).stdout.replace("\t", " ")
    assert fun11() == expected


def test_fun12() -> None:
    """
    Extract the value of the first column of each line, and store the output into col1.txt. Extract the value of the second column of each line, and store the output into col2.txt. Confirm the result by using cut command.
    """
    expected1 = subprocess.run(
        ["cut", "-f", "1", "data/popular-names.txt"], capture_output=True, text=True
    ).stdout
    expected2 = subprocess.run(
        ["cut", "-f", "2", "data/popular-names.txt"], capture_output=True, text=True
    ).stdout
    fun12()
    with open("data/col1.txt", "r") as f:
        assert f.read() == expected1
    with open("data/col2.txt", "r") as f:
        assert f.read() == expected2


def test_fun13() -> None:
    """
    Join the contents of col1.txt and col2.txt, and create a text file whose each line contains the values of the first and second columns (separated by tab character) of the original file. Confirm the result by using paste command.
    """
    expected = subprocess.run(
        ["paste", "data/col1.txt", "data/col2.txt"], capture_output=True, text=True
    ).stdout
    fun13()
    with open("data/col1_col2.txt", "r") as f:
        assert f.read() == expected
