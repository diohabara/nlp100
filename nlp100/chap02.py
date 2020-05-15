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
        original_filename = "popular-names.txt"
        new_filename = "q11_modified_by_python.txt"
        try:
            with open(f"docs/{original_filename}", mode="r",
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

    def save_two_lines(self) -> None:
        pass

    def merge_two_textfiles(self) -> None:
        pass

    def first_n_lines(self) -> None:
        pass

    def last_n_lines(self) -> None:
        pass

    def split_a_file_into_n_pieces(self) -> None:
        pass

    def distict_string_in_the_first_column(self) -> None:
        pass

    def sort_lines_in_asc_of_third_column(self) -> None:
        pass

    def frequency_of_a_string_in_the_first_column_in_des(self) -> None:
        pass
