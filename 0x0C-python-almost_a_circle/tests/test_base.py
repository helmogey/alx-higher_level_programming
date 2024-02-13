import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty(self):
        data = [{"id": 1, "name": "Alice"}]
        self.assertEqual(Base.to_json_string(data), '[{"id": 1, "name": "Alice"}]')

    def test_save_to_file_empty(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    # def test_save_to_file_non_empty(self):
    #     obj1 = Base(id=10)
    #     obj2 = Base(id=20)
    #     Base.save_to_file([obj1, obj2])
    #     with open("Base.json", "r") as f:
    #         self.assertEqual(json.loads(f.read()), [{"id": 10}, {"id": 20}])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_non_empty(self):
        json_string = '[{"id": 30, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"id": 30, "name": "Bob"}])

    def test_create_empty(self):
        self.assertEqual(Base.create(), None)

    # def test_create_non_empty(self):
    #     obj = Base.create(id=40, name="Charlie")
    #     self.assertEqual(obj.id, 40)
    #     self.assertEqual(obj.name, "Charlie")  # Assuming the Base class has a "name" attribute
    #
    # def test_load_from_file_empty(self):
    #     self.assertEqual(Base.load_from_file(), [])
    #
    # def test_load_from_file_non_empty(self):
    #     Base.save_to_file([Base(id=50), Base(id=60)])
    #     objects = Base.load_from_file()
    #     self.assertEqual([obj.id for obj in objects], [50, 60])

if __name__ == "__main__":
    unittest.main()
