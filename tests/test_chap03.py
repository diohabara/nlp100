"""
Chapter 3: Regular Expression
"""

from nlp100.chap03 import fun20, fun21, fun22, fun23


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
    expected = [
        "United Kingdom| ",
        "British Islands",
        "Countries in Europe",
        "English-speaking countries and territories",
        "G7 nations",
        "Group of Eight nations",
        "G20 nations",
        "Island countries",
        "Northern European countries",
        "Former member states of the European Union",
        "Member states of NATO",
        "Member states of the Commonwealth of Nations",
        "Member states of the Council of Europe",
        "Member states of the Union for the Mediterranean",
        "Member states of the United Nations",
        "Priority articles for attention after Brexit",
        "Western European countries",
    ]
    achieved = fun22()
    assert expected == achieved


def test_fun23() -> None:
    """
    Extract section names in the article with their levels. For example, the level of the section is 1 for the MediaWiki markup "== Section name ==".
    """
    expected = [
        ("Etymology and terminology", 1),
        ("History", 1),
        ("=Background=", 1),
        ("=Treaty of Union=", 1),
        ("=From the union with Ireland to the end of the First World War=", 1),
        ("=Between the World Wars=", 1),
        ("=Since the Second World War=", 1),
        ("Geography", 1),
        ("=Climate=", 1),
        ("=Administrative divisions=", 1),
        ("Dependencies", 1),
        ("Politics", 1),
        ("=Government=", 1),
        ("=Devolved administrations=", 1),
        ("=Law and criminal justice=", 1),
        ("=Foreign relations=", 1),
        ("=Military=", 1),
        ("Economy", 1),
        ("=Overview=", 1),
        ("=Science and technology=", 1),
        ("=Transport=", 1),
        ("=Energy=", 1),
        ("=Water supply and sanitation=", 1),
        ("Demographics", 1),
        ("=Ethnic groups=", 1),
        ("=Languages=", 1),
        ("=Religion=", 1),
        ("=Migration=", 1),
        ("=Education=", 1),
        ("=Health=", 1),
        ("Culture", 1),
        ("=Literature=", 1),
        ("=Music=", 1),
        ("=Visual art=", 1),
        ("=Cinema=", 1),
        ("= Cuisine =", 1),
        ("=Media=", 1),
        ("=Philosophy=", 1),
        ("=Sport=", 1),
        ("=Symbols=", 1),
        ("=Stereotypes=", 1),
        ("Historiography", 1),
        ("See also", 1),
        ("Notes", 1),
        ("References", 1),
        ("External links", 1),
        ("Background", 2),
        ("Treaty of Union", 2),
        ("From the union with Ireland to the end of the First World War", 2),
        ("Between the World Wars", 2),
        ("Since the Second World War", 2),
        ("Climate", 2),
        ("Administrative divisions", 2),
        ("Government", 2),
        ("Devolved administrations", 2),
        ("Law and criminal justice", 2),
        ("Foreign relations", 2),
        ("Military", 2),
        ("Overview", 2),
        ("Science and technology", 2),
        ("Transport", 2),
        ("Energy", 2),
        ("Water supply and sanitation", 2),
        ("Ethnic groups", 2),
        ("Languages", 2),
        ("Religion", 2),
        ("Migration", 2),
        ("Education", 2),
        ("Health", 2),
        ("Literature", 2),
        ("Music", 2),
        ("Visual art", 2),
        ("Cinema", 2),
        (" Cuisine ", 2),
        ("Media", 2),
        ("Philosophy", 2),
        ("Sport", 2),
        ("Symbols", 2),
        ("Stereotypes", 2),
    ]
    achieved = fun23()
    assert expected == achieved


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
