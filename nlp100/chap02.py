from collections import Counter


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
    with open("data/popular-names.txt", "r") as f, open("data/col1.txt", "w") as c1, open("data/col2.txt", "w") as c2:
        lines = f.readlines()
        for line in lines:
            c1.write(line.split()[0])
            c2.write(line.split()[1])
            c1.write("\n")
            c2.write("\n")


def fun13() -> None:
    with open("data/col1.txt", "r") as c1, open("data/col2.txt", "r") as c2, open("data/col1_col2.txt", "w") as c3:
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


def fun16(n: int) -> int:
    assert 0 < n
    count = 0
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), n):
            with open(f"data/chunk{count:02}.txt", "w") as c:
                c.write("".join(lines[i : min(i + n, len(lines))]))
            count += 1
    return count


def fun17() -> set[str]:
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        return set([line.split()[0] for line in lines])


def fun18() -> str:
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        lines.sort(key=lambda x: int(x.split()[2]), reverse=True)
    return "".join(lines[:5])


def fun19() -> str:
    with open("data/popular-names.txt", "r") as f:
        lines = f.readlines()
        word_to_freq = Counter([line.split()[0] for line in lines])
<<<<<<< Updated upstream
        sorted_word_to_freq = sorted(word_to_freq.items(), key=lambda x: x[1], reverse=True)
        return "".join([f" {ele[1]:3} {ele[0]}\n" for ele in sorted_word_to_freq][:10])
=======
        word_to_freq = sorted(word_to_freq.items(), key=lambda x: x[1], reverse=True)
        return "".join([f" {ele[1]:3} {ele[0]}\n" for ele in word_to_freq][:10])
>>>>>>> Stashed changes
