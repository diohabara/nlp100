class Chap02():
    def count_lines(self) -> int:
        """
        10. Line countPermalink
        Count the number of lines of the file. Confirm the result by using wc command.
        """
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
        """
        11. Replace tabs into spacesPermalink
        Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.
        """
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

    def save_two_lines(self) -> None:
        """
        12. col1.txt from the first column, col2.txt from the second columnPermalink
        Extract the value of the first column of each line, and store the output into col1.txt. Extract the value of the second column of each line, and store the output into col2.txt. Confirm the result by using cut command.
        """
        pass

    def merge_two_textfiles(self) -> None:
        """
        13. Merging col1.txt and col2.txtPermalink
        Join the contents of col1.txt and col2.txt, and create a text file whose each line contains the values of the first and second columns (separated by tab character) of the original file. Confirm the result by using paste command.
        """
        pass

    def n_lines_permalink(self) -> None:
        """
        14. First N linesPermalink
        Receive a natural number $N$ from a command-line argument, and output the first $N$ lines of the file. Confirm the result by using head command.
        """
        pass

    def last_n_lines_permalink(self) -> None:
        """
        15. Last N linesPermalink
        Receive a natural number $N$ from a command-line argument, and output the last $N$ lines of the file. Confirm the result by using tail command.
        """
        pass

    def split_a_file_into_n_pieces(self) -> None:
        """
        16. Split a file into N piecesPermalink
        Receive a natural number $N$ from a command-line argument, and split the input file into $N$ pieces at line boundaries. Confirm the result by using split command.
        """
        pass

    def distict_string_in_the_first_column_permalink(self) -> None:
        """
        17. Distinct strings in the first columnPermalink
        Find distinct strings (a set of strings) of the first column of the file. Confirm the result by using cut, sort, and uniq commands.
        """
        pass

    def sort_lines_in_asc_of_third_column_permalink(self) -> None:
        """
        18. Sort lines in ascending order of the third columnPermalink
        Sort the lines in ascending numeric order of the third column (sort lines without changing the content of each line). Confirm the result by using sort command.
        """
        pass

    def frequency_of_a_string_in_the_first_column_in_des(self) -> None:
        """
        19. Frequency of a string in the first column in descending orderPermalink
        Find the frequency of a string in the first column, and sort the strings by descending order of their frequencies. Confirm the result by using cut, uniq, and sort commands.
        """
        pass
