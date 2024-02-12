

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(5)
        self.assertEqual(square.id, Base.__nb_objects - 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        square2 = Square(3, 2, 1, 42)
        self.assertEqual(square2.id, 42)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.width, 3)
        self.assertEqual(square2.height, 3)
        self.assertEqual(square2.x, 2)
        self.assertEqual(square2.y, 1)

    def test_init_errors(self):
        with self.assertRaises(TypeError):
            Square("invalid")  # Size as string
        with self.assertRaises(ValueError):
            Square(0)  # Size zero
        with self.assertRaises(TypeError):
            Square(5, "invalid")  # X as string
        with self.assertRaises(ValueError):
            Square(5, -1)  # X negative
        with self.assertRaises(TypeError):
            Square(5, 2, "invalid")  # Y as string
        with self.assertRaises(ValueError):
            Square(5, 2, -1)  # Y negative

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        # Capture display output in a StringIO buffer
        from io import StringIO
        buffer = StringIO()
        square = Square(3)
        square.display(buffer)
        expected_output = "\n\n###\n###\n"
        self.assertEqual(buffer.getvalue(), expected_output)

    def test_str(self):
        square = Square(4, 1, 2, 42)
        self.assertEqual(str(square), "[Square] (42) 1/2 - 4")

    def test_update(self):
        square = Square(5)

        # Test no-keyword arguments
        square.update(2, 1, 2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

        # Test keyword arguments
        square.update(id=10, size=7, y=3)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 1)  # X remains unchanged
        self.assertEqual(square.y, 3)

        # Test mixed arguments (raises error)
        with self.assertRaises(ValueError):
            square.update(1, 2, x=3)

    def test_to_dictionary(self):
        square = Square(2, 1, 2, 42)
        expected_dict = {"id": 42, "size": 2, "x": 1, "y": 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
