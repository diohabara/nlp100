import subprocess
import unittest
from nlp100.chap02 import Chap02


class Chap02Test(unittest.TestCase):
    def setUp(self):
        self.proc = Chap02()

    def test_count_lines(self):
        """
        10. 行数のカウント
        行数をカウントせよ．確認にはwcコマンドを用いよ．
        """
        args = ["wc", "-l", "docs/popular-names.txt"]
        try:
            number_of_lines = int(subprocess.check_output(args).split()[0])
        except subprocess.CalledProcessError:
            print("Error: fail to wc")
        self.assertEqual(number_of_lines, self.proc.count_lines())

    def test_make_tab_into_space(self):
        """
        11. タブをスペースに置換
        タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
        """
        pass

    def test_save_two_lines(self):
        """
        12. 1列目をcol1.txtに，2列目をcol2.txtに保存Permalink
        各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
        """
        pass

    def test_merge_two_textfiles(self):
        """
        13. col1.txtとcol2.txtをマージPermalink
        12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
        """
        pass

    def test_n_lines(self):
        """
        14. 先頭からN行を出力Permalink
        自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
        """
        pass

    def test_last_n_lines(self):
        """
        15. 末尾のN行を出力Permalink
        自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
        """
        pass

    def test_split_a_file_into_n_pieces(self):
        """
        16. ファイルをN分割するPermalink
        自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
        """
        pass

    def test_distict_string_in_the_first_column(self):
        """
        17. １列目の文字列の異なりPermalink
        1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
        """
        pass

    def test_sort_lines_in_asc_of_third_column(self):
        """
        18. 各行を3コラム目の数値の降順にソートPermalink
        各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
        """
        pass

    def test_frequency_of_a_string_in_the_first_column_in_des(self):
        """
        19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べるPermalink
        各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
        """
        pass
