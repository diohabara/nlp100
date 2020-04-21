import os


class Chap02():
    def count_lines(self) -> int:
        number_of_line = 0
        try:
            with open("docs/popular-names.txt", mode="r",
                      encoding="utf-8") as f:
                for _ in f:
                    number_of_line += 1
            f.close()
        except EnvironmentError:
            print("We failed to open the file")

        return number_of_line