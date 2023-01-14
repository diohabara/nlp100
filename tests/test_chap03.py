"""
Chapter 3: Regular Expression
"""

from nlp100.chap03 import fun20, fun21


def test_fun20() -> None:
    """
    Read the JSON documents and output the body of the article about the United Kingdom. Reuse the output in problems 21-29.
    """
    expected = "{{About-distinguish2|the country|[[Great Britain]]"
    achieved = fun20()[:50]
    assert expected == achieved


def test_fun21() -> None:
    """
    Extract lines that define the categories of the article.
    """
    expected = """[[Category:United Kingdom| ]]
[[Category:British Islands]]
[[Category:Countries in Europe]]
[[Category:English-speaking countries and territories]]
[[Category:G7 nations]]
[[Category:Group of Eight nations]]
[[Category:G20 nations]]
[[Category:Island countries]]
[[Category:Northern European countries]]
[[Category:Former member states of the European Union]]
[[Category:Member states of NATO]]
[[Category:Member states of the Commonwealth of Nations]]
[[Category:Member states of the Council of Europe]]
[[Category:Member states of the Union for the Mediterranean]]
[[Category:Member states of the United Nations]]
[[Category:Priority articles for attention after Brexit]]
[[Category:Western European countries]]"""
    achieved = fun21()
    assert expected == achieved


def test_fun22() -> None:
    """
    Extract the category names of the article.
    """


def test_fun23() -> None:
    """
    Extract section names in the article with their levels. For example, the level of the section is 1 for the MediaWiki markup "== Section name ==".
    """


def test_fun24() -> None:
    """
    Extract references to media files linked from the article.
    """


def test_fun25() -> None:
    """
    Extract field names and their values in the Infobox “country”, and store them in a dictionary object.
    """


def test_fun26() -> None:
    """
    In addition to the process of the problem 25, remove emphasis MediaWiki markups from the values. See Help:Cheatsheet.
    """


def test_fun27() -> None:
    """
    In addition to the process of the problem 26, remove internal links from the values. See Help:Cheatsheet.
    """


def test_fun28() -> None:
    """
    In addition to the process of the problem 27, remove MediaWiki markups from the values as much as you can, and obtain the basic information of the country in plain text format.
    """


def test_fun29() -> None:
    """
    Obtain the URL of the country flag by using the analysis result of Infobox. (Hint: convert a file reference to a URL by calling imageinfo in MediaWiki API)
    """
