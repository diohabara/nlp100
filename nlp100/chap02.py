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
            print("Error: fail to open the file")

        return number_of_line

    def make_tab_into_space(self) -> None:
        new_filename = "q11_modified_by_python.txt"
        try:
            with open("docs/popular-names.txt", mode="r",
                      encoding="utf-8") as read_file:
                try:
                    with open(f"docs/{new_filename}",
                              mode="w",
                              encoding="utf-8") as write_file:
                        lines = read_file.read()
                        for line in lines:
                            line.replace("\t", " ")
                            write_file.write(line)
                    read_file.close()
                    write_file.close()
                except EnvironmentError:
                    print("Error: fail to read the file")
        except EnvironmentError:
            print("Error: fail to open the file")
