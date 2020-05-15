import subprocess
import unittest
import filecmp
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
        self.proc.make_tab_into_space()
        python_file_path = "docs/q11_modified_by_python.txt"
        sed_file_path = "docs/q11_modified_by_sed.txt"
        f = open(sed_file_path, "w")
        args = ["sed", "-e", "s/<tab>/<space>/g", "docs/popular-names.txt"]
        try:
            subprocess.run(args, stdout=f)
        except subprocess.CalledProcessError:
            print("Error: fail to sed")
        self.assertTrue(filecmp.cmp(python_file_path,
                                    sed_file_path,
                                    shallow=False))
        f.close()

    def test_save_two_lines(self):
        """
        12. 1列目をcol1.txtに，2列目をcol2.txtに保存
        各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
        """
        self.proc.save_two_lines()
        original_path = "docs/popular-names.txt"
        col1_path = "docs/col1.txt"
        col2_path = "docs/col2.txt"
        test1_path = "docs/col1_test.txt"
        test2_path = "docs/col2_test.txt"
        args1 = ["cut", "-f1", "-d", '\t', original_path]
        args2 = ["cut", "-f2", "-d", '\t', original_path]
        f1 = open(test1_path, "w")
        f2 = open(test2_path, "w")
        try:
            subprocess.run(args1, stdout=f1)
            subprocess.run(args2, stdout=f2)
        except subprocess.CalledProcessError:
            print("Error: fail to cut")
        self.assertTrue(filecmp.cmp(col1_path,
                                    test1_path,
                                    shallow=False))
        self.assertTrue(filecmp.cmp(col2_path,
                                    test2_path,
                                    shallow=False))
        f1.close()
        f2.close()

    def test_merge_two_textfiles(self):
        """
        13. col1.txtとcol2.txtをマージ
        12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
        """
        self.proc.merge_two_textfiles()
        col1_path = "docs/col1.txt"
        col2_path = "docs/col2.txt"
        merged_path = "docs/merged.txt"
        test_merged_path = "docs/test_merged.txt"
        args = ["paste", col1_path, col2_path]
        f = open(test_merged_path, "w")
        try:
            subprocess.run(args, stdout=f)
        except subprocess.CalledProcessError:
            print("Error: fail to paste")
        self.assertTrue(filecmp.cmp(merged_path,
                                    test_merged_path,
                                    shallow=False))
        f.close()

    def test_n_lines(self):
        """
        14. 先頭からN行を出力
        自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
        """
        pass

    def test_last_n_lines(self):
        """
        15. 末尾のN行を出力
        自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
        """
        pass

    def test_split_a_file_into_n_pieces(self):
        """
        16. ファイルをN分割する
        自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
        """
        pass

    def test_distict_string_in_the_first_column(self):
        """
        17. １列目の文字列の異なり
        1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
        """
        pass

    def test_sort_lines_in_asc_of_third_column(self):
        """
        18. 各行を3コラム目の数値の降順にソート
        各行を3コラム目の数値の逆順で整列せよ\
        （注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
        """
        pass

    def test_frequency_of_a_string_in_the_first_column_in_des(self):
        """
        19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
        各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
        """
        pass
