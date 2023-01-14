import json


def fun20() -> str:
    data = [json.loads(line) for line in open("./data/enwiki-country.json")]
    uk_data = [datum for datum in data if datum["title"] == "United Kingdom"]
    return str(uk_data[0]["text"])[:50]
