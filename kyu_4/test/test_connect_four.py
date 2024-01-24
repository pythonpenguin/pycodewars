import unittest
import kyu_4.src.connect_four


class TestVector(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(kyu_4.src.connect_four.Vector(3), kyu_4.src.connect_four.Vector)

    def test_fill_vector(self):
        v = kyu_4.src.connect_four.Vector(7)
        c41=kyu_4.src.connect_four.Cell(4)
        v.add_cell(c41)
        self.assertListEqual([c41], v.cells)
        c71 = kyu_4.src.connect_four.Cell(7)
        v.add_cell(c71)
        c72 = kyu_4.src.connect_four.Cell(7)
        v.add_cell(c72)
        c51=kyu_4.src.connect_four.Cell(5)
        v.add_cell(c51)
        self.assertListEqual([c41,c71, c72,c51], v.cells)

    def test_get_cell_by_index(self):
        v = kyu_4.src.connect_four.Vector(7)
        c71 = kyu_4.src.connect_four.Cell(7)
        v.add_cell(c71)
        c72 = kyu_4.src.connect_four.Cell(7)
        v.add_cell(c72)
        self.assertEqual(c72, v.get_cell_by_index(1))

    def test_winner(self):
        v = kyu_4.src.connect_four.Vector(7)
        c71 = kyu_4.src.connect_four.Cell(7)
        c71.colour = "Red"
        for i in range(4):
            v.add_cell(c71)
        self.assertTrue(v.is_there_a_winner("Red"))
        self.assertFalse(v.is_there_a_winner("Yellow"))

    def test_draw_winner(self):
        v = kyu_4.src.connect_four.Vector(7)
        c71 = kyu_4.src.connect_four.Cell(7)
        c72 = kyu_4.src.connect_four.Cell(7)
        c72.colour = "Yellow"
        c71.colour = "Red"
        for i in range(3):
            v.add_cell(c71)
        v.add_cell(c72)
        v.add_cell(c71)
        v.add_cell(c71)
        self.assertFalse(v.is_there_a_winner("Red"))
        self.assertFalse(v.is_there_a_winner("Yellow"))


class MyTestCase(unittest.TestCase):
    def test_yellow_antidiagonal(self):
        self.assertEqual("Yellow", kyu_4.src.connect_four.who_is_winner([
            "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
            "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
            "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"]))

    def test_red_column(self):
        self.assertEqual("Red", kyu_4.src.connect_four.who_is_winner([
            "A_Yellow", "B_Red", "C_Yellow", "B_Red", "D_Yellow", "B_Red", "A_Yellow", "B_Red"]))

    def test_yellow_column(self):
        self.assertEqual("Yellow", kyu_4.src.connect_four.who_is_winner([
            "A_Yellow", "B_Red", "A_Yellow", "B_Red", "A_Yellow", "B_Red", "A_Yellow"]))

    def test_yellow_diagonal(self):
        self.assertEqual("Yellow", kyu_4.src.connect_four.who_is_winner([
            "E_Yellow", "D_Red", "D_Yellow", "C_Red", "B_Yellow", "C_Red", "C_Yellow", "B_Red",
            "A_Yellow", "B_Red", "B_Yellow"]))

    def test_draw(self):
        self.assertEqual("Draw", kyu_4.src.connect_four.who_is_winner([
            "E_Yellow", "D_Red", "D_Yellow", "C_Red", "B_Yellow", "C_Red", "C_Yellow", "B_Red",
            "A_Yellow", "B_Red"]))

    def test_red(self):
        self.assertEqual("Red", kyu_4.src.connect_four.who_is_winner(
            ["F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
             "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
             "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
             "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
             "B_Yellow", "B_Red"]))


if __name__ == '__main__':
    unittest.main()
