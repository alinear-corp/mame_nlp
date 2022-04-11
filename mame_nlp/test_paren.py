from unittest import TestCase

from mame_nlp.paren import ParenRemover


class TestParenRemover(TestCase):
    def setUp(self) -> None:
        self.remover = ParenRemover()

    def test_remove(self):
        actual = self.remover.remove("括弧のないパターン。")
        expected = "括弧のないパターン。"
        self.assertEqual(actual, expected)

        actual = self.remover.remove("正しく括弧が対応している（このように）パターン。")
        expected = "正しく括弧が対応しているパターン。"
        self.assertEqual(actual, expected)

        actual = self.remover.remove("括弧の中に括弧（例えばこのように（ここに括弧がある）。）があるパターン。")
        expected = "括弧の中に括弧があるパターン。"
        self.assertEqual(actual, expected)

    def test_remove_give_up(self):
        actual = self.remover.remove(
            "括弧が対応していない中で別の括弧があるパターン。（例えばこのように適当な括弧[適当な補足]があるものの、外側が対応していない場合)"
        )
        expected = "括弧が対応していない中で別の括弧があるパターン。（例えばこのように適当な括弧[適当な補足]があるものの、外側が対応していない場合)"
        self.assertEqual(actual, expected)

        actual = self.remover.remove("括弧が対応していないパターン（このように)パターン。")
        expected = "括弧が対応していないパターン（このように)パターン。"
        self.assertEqual(actual, expected)

        actual = self.remover.remove(
            "括弧の中の括弧が（このように（内側の括弧)だけが）対応していないパターン。"
        )
        expected = "括弧の中の括弧が（このように（内側の括弧)だけが）対応していないパターン。"
        self.assertEqual(actual, expected)


class TestParenRemoverAlt(TestCase):
    def setUp(self) -> None:
        self.remover = ParenRemover(alt=" ")

    def test_remove(self):
        actual = self.remover.remove("正しく括弧が対応している（このように）パターン。")
        expected = "正しく括弧が対応している パターン。"
        self.assertEqual(actual, expected)
