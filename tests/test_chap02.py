import sys
import subprocess
from nlp100.chap02 import Chap02

try:
    if sys.version_info < (2, 7):
        import unittest2
    else:
        raise ImportError()
except ImportError:
    import unittest


class Chap02Test(unittest.TestCase):
    def setUp(self):
        self.proc = Chap02()

    def test_count_lines(self):
        args = ["wc", "-l", "docs/popular-names.txt"]
        try:
            number_of_lines = int(subprocess.check_output(args).split()[0])
        except:
            print("Error: fail to wc")
        self.assertEqual(number_of_lines, self.proc.count_lines())