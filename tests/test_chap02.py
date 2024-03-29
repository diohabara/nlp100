"""Chapter 2: UNIX Commands
The file popular-names.txt stores names of babies born in US with their genders, numbers of births, and years of births in tab-separated format. Create a program with the specifications below. Run the program with popular-names.txt as an input. Furthermore, confirm that the same (similar) result can be obtained by running a UNIX command.
"""


import subprocess

from nlp100.chap02 import fun10, fun11, fun12, fun13, fun14, fun15, fun16, fun17, fun18, fun19


def test_fun10() -> None:
    """
    Write a function that counts the number of lines in a file
    """
    expected = subprocess.run(["wc", "-l", "data/popular-names.txt"], capture_output=True, text=True).stdout.split()[0]
    assert fun10() == int(expected)


def test_fun11() -> None:
    """
    Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.
    """
    expected = subprocess.run(["cat", "data/popular-names.txt"], capture_output=True, text=True).stdout.replace("\t", " ")
    assert fun11() == expected


def test_fun12() -> None:
    """
    Extract the value of the first column of each line, and store the output into col1.txt. Extract the value of the second column of each line, and store the output into col2.txt. Confirm the result by using cut command.
    """
    expected1 = subprocess.run(["cut", "-f", "1", "data/popular-names.txt"], capture_output=True, text=True).stdout
    expected2 = subprocess.run(["cut", "-f", "2", "data/popular-names.txt"], capture_output=True, text=True).stdout
    fun12()
    with open("data/col1.txt", "r") as f:
        assert f.read() == expected1
    with open("data/col2.txt", "r") as f:
        assert f.read() == expected2


def test_fun13() -> None:
    """
    Join the contents of col1.txt and col2.txt, and create a text file whose each line contains the values of the first and second columns (separated by tab character) of the original file. Confirm the result by using paste command.
    """
    expected = subprocess.run(["paste", "data/col1.txt", "data/col2.txt"], capture_output=True, text=True).stdout
    fun13()
    with open("data/col1_col2.txt", "r") as f:
        assert f.read() == expected


def test_fun14() -> None:
    """
    Receive a natural number N from a command-line argument, and output the first N lines of the file. Confirm the result by using head command.
    """
    n = 5
    expected = subprocess.run(
        ["head", "-n", str(n), "data/popular-names.txt"],
        capture_output=True,
        text=True,
    ).stdout
    assert fun14(n) == expected


def test_fun15() -> None:
    """
    Receive a natural number N from a command-line argument, and output the last N lines of the file. Confirm the result by using tail command.
    """
    n = 5
    expected = subprocess.run(
        ["tail", "-n", str(n), "data/popular-names.txt"],
        capture_output=True,
        text=True,
    ).stdout
    assert fun15(n) == expected


def test_fun16() -> None:
    """
    Receive a natural number $N$ from a command-line argument, and split the input file into $N$ pieces at line boundaries. Confirm the result by using split command.
    """
    n = 200
    subprocess.run(
        ["split", "-l", f"{n}", "-d", "data/popular-names.txt", "data/expected"],
        capture_output=True,
        text=True,
    ).stdout
    count = fun16(n)
    for i in range(count):
        with open(f"data/chunk{i:02}.txt", "r") as chunk, open(f"data/expected{i:02}", "r") as expect:
            print(i)
            assert chunk.read() == expect.read()


def test_fun17() -> None:
    """
    Find distinct strings (a set of strings) of the first column of the file. Confirm the result by using cut, sort, and uniq commands.
    """
    expected = subprocess.run(["cut -f 1 data/popular-names.txt | sort | uniq"], capture_output=True, text=True, shell=True).stdout
    assert fun17() == set(expected.split())


def test_fun18() -> None:
    """
    Sort the lines in descending numeric order of the third column (sort lines without changing the content of each line). Confirm the result by using sort command.
    """
    expected = subprocess.run(
        ["sort -rnk 3 data/popular-names.txt | head -n 5"],
        capture_output=True,
        text=True,
        shell=True,
    ).stdout
    assert fun18() == expected


def test_fun19() -> None:
    """
    Find the frequency of a string in the first column, and sort the strings by descending order of their frequencies. Confirm the result by using cut, uniq, and sort commands.
    """
    expected = subprocess.run(
        ["cut -f 1 data/popular-names.txt | sort | uniq -c | sort -k1,1r -k2 | head -n 10"],
        capture_output=True,
        text=True,
        shell=True,
    ).stdout
    assert fun19() == expected
