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
                        for line in read_file:
                            line.replace("\t", " ")
                            write_file.write(line)
                        write_file.close()
                        read_file.close()
                except EnvironmentError:
                    print("Error: fail to open the file")
        except EnvironmentError:
            print("Error: fail to read the file")

    def save_two_lines(self) -> None:
        original_path = "docs/popular-names.txt"
        try:
            with open(original_path, mode="r",
                      encoding="utf-8") as read_file:
                try:
                    with open("docs/col1.txt",
                              mode="w",
                              encoding="utf-8") as col1, open(
                                  "docs/col2.txt",
                                  mode="w",
                                  encoding="utf-8") as col2:
                        for line in read_file:
                            strs = list(line.split())
                            col1.write(strs[0] + "\n")
                            col2.write(strs[1] + "\n")
                    col1.close()
                    col2.close()
                    read_file.close()
                except EnvironmentError:
                    print("Error: fail to open the files")
        except EnvironmentError:
            print("Error: fail to read the file")

    def merge_two_textfiles(self) -> None:
        col1_path = "docs/col1.txt"
        col2_path = "docs/col2.txt"
        merged_path = "docs/merged.txt"
        try:
            with open(merged_path, "w",
                      encoding="utf-8") as merged_file:
                try:
                    with open(col1_path, "r",
                              encoding="utf-8") as col1, open(
                                  col2_path, "r",
                                  encoding="utf-8") as col2:
                        for c1, c2 in zip(col1, col2):
                            line = f"{c1.strip()}\t{c2.strip()}\n"
                            merged_file.write(line)
                except EnvironmentError:
                    print("Error: fail to read the files")
        except EnvironmentError:
            print("Error: fail to write the file")

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
