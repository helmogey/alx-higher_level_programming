import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        rect = Rectangle(10, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

        rect2 = Rectangle(3, 2, 2, 1, 42)
        self.assertEqual(rect2.id, 42)
        self.assertEqual(rect2.width, 3)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2.y, 1)

    def test_init_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 5)  # Width as string
        with self.assertRaises(ValueError):
            Rectangle(0, 5)  # Width zero
        with self.assertRaises(TypeError):
            Rectangle(10, "invalid")  # Height as string
        with self.assertRaises(ValueError):
            Rectangle(10, 0)  # Height zero
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "invalid")  # X as string
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -1)  # X negative
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 2, "invalid")  # Y as string
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 2, -1)  # Y negative

    def test_area(self):
        rect = Rectangle(5, 3)
        self.assertEqual(rect.area(), 15)


    def test_str(self):
        rect = Rectangle(4, 2, 1, 2, 42)
        self.assertEqual(str(rect), "[Rectangle] (42) 1/2 - 4/2")


    def test_to_dictionary(self):
        rect = Rectangle(2, 3, 1, 2, 42)
        expected_dict = {"id": 42, "width": 2, "height": 3, "x": 1, "y": 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

if __name__ == "__main__":
    unittest.main()