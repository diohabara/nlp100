def fun10() -> int:
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        return len(lines)


def fun11() -> str:
    res = []
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            res.append(line.replace("\t", " "))
    return "".join(res)


def fun12() -> None:
    with open("data/popular-names.txt", "r") as f, open(
        "data/col1.txt", "w"
    ) as c1, open("data/col2.txt", "w") as c2:
        lines = f.readlines()
        for line in lines:
            c1.write(line.split()[0])
            c2.write(line.split()[1])
            c1.write("\n")
            c2.write("\n")


def fun13() -> None:
    with open("data/col1.txt", "r") as c1, open("data/col2.txt", "r") as c2, open(
        "data/col1_col2.txt", "w"
    ) as c3:
        lines1 = c1.readlines()
        lines2 = c2.readlines()
        for line1, line2 in zip(lines1, lines2):
            c3.write(line1.replace("\n", "") + "\t" + line2)


def fun14(n: int) -> str:
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        return "".join(lines[:n])


def fun15(n: int) -> str:
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        return "".join(lines[-n:])


def fun16(n: int) -> None:
    assert 0 < n
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), len(lines) // n):
            with open(f"data/chunk{i}.txt", "w") as c:
                c.write("".join(lines[i : i + n]))
