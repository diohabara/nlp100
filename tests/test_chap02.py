import subprocess
import unittest
from nlp100.chap02 import Chap02


class Chap02Test(unittest.TestCase):
    def setUp(self):
        self.proc = Chap02()

    def test_count_lines(self):
        args = ["wc", "-l", "docs/popular-names.txt"]
        try:
            number_of_lines = int(subprocess.check_output(args).split()[0])
        except subprocess.CalledProcessError:
            print("Error: fail to wc")
        self.assertEqual(number_of_lines, self.proc.count_lines())

    def test_make_tab_into_space(self):
        pass

    def test_save_two_lines(self):
        pass

    def test_merge_two_textfiles(self):
        pass

    def test_n_lines_permalink(self):
        pass

    def test_last_n_lines_permalink(self):
        pass

    def test_split_a_file_into_n_pieces(self):
        pass

    def test_distict_string_in_the_first_column_permalink(self):
        pass

    def test_sort_lines_in_asc_of_third_column_permalink(self):
        pass

    def test_frequency_of_a_string_in_the_first_column_in_des(self):
        pass
