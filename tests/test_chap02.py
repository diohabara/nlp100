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
