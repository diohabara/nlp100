"""
Chapter 3: Regular Expression
"""

from nlp100.chap03 import fun20


def test_fun20() -> None:
    """
    Read the JSON documents and output the body of the article about the United Kingdom. Reuse the output in problems 21-29.
    """
    expected = "{{About-distinguish2|the country|[[Great Britain]]"
    achieved = fun20()
    assert expected == achieved
