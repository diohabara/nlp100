import json
import re


def fun20() -> str:
    data = [json.loads(line) for line in open("./data/enwiki-country.json")]
    uk_data = [datum for datum in data if datum["title"] == "United Kingdom"]
    return str(uk_data[0]["text"])


def fun21() -> str:
    data = fun20()
    pattern = r"\[\[Category:.*\]\]"
    prog = re.compile(pattern)
    return "\n".join(prog.findall(data))


def fun22() -> list[str]:
    data = fun20()
    pattern = r"\[\[Category:(.*)\]\]"
    prog = re.compile(pattern)
    return prog.findall(data)


def fun23() -> list[tuple[str, int]]:
    data = fun20()
    res = []
    level1_pattern = r"={2}(.*)={2}"
    prog1 = re.compile(level1_pattern)
    res.extend([(name, 1) for name in prog1.findall(data)])
    level2_pattern = r"={3}(.*)={3}"
    prog2 = re.compile(level2_pattern)
    res.extend([(name, 2) for name in prog2.findall(data)])
    return res


def fun24() -> list[str]:
    data = fun20()
    #  [[File:United Kingdom (+overseas territories and crown dependencies) in the World (+Antarctica claims).svg|frameless|upright=1.15]]
    pattern = r"\[\[File:([^\.]*\.[^\|]*)\|[^\|]*\|[^\]]*\]\]"
    prog = re.compile(pattern)
    return prog.findall(data)


def fun25() -> dict[str, str]:
    data = fun20()
    # print(data)
    infobox_pattern = r"\{\{Infobox country.*\}\}\n\n"
    infobox_prog = re.compile(infobox_pattern)
    print(infobox_prog.findall(data))
    kv_pattern = r"\| (\S*)\s= (.*)\n"
    kv_prog = re.compile(kv_pattern)
    res = {}
    for infobox_text in infobox_prog.findall(data):
        print(infobox_text)
        for k, v in kv_prog.findall(infobox_text):
            print(k, v)
            res[k] = v
    return res


def fun26():
    pass


def fun27():
    pass


def fun28():
    pass


def fun29():
    pass


if __name__ == "__main__":
    fun25()
