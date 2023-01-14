import json
import re


def fun20() -> str:
    data = [json.loads(line) for line in open("./data/enwiki-country.json")]
    uk_data = [datum for datum in data if datum["title"] == "United Kingdom"]
    return str(uk_data[0]["text"])


def fun21() -> str:
    data = fun20()
    pattern = r"\[\[Category:.*\s*\]\]"
    prog = re.compile(pattern)
    return "\n".join(prog.findall(data))


if __name__ == "__main__":
    fun21()
