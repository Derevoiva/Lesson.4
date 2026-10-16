import unittest
import lesson4 as m

class LessonTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(m.salary(2,10,5),25)
        self.assertEqual(m.greater_than_previous([3,1,2]),[2])
        self.assertEqual(m.unique_numbers([1,2,1,3]),[2,3])
        self.assertEqual(list(m.factorials(4)),[1,2,6,24])
        self.assertEqual(m.repeat_items([1,2],5),[1,2,1,2,1])

if __name__ == "__main__":
    unittest.main()
