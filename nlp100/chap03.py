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


if __name__ == "__main__":
    fun21()
