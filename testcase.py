import unittest
import PROJECT as prog

class TestMyProgram(unittest.TestCase):
    def test_Total(self):
        self.assertEqual(prog.total, 6756714)

    def test_Mean(self):
        self.assertEqual(prog.mean, 2252236.67)

if __name__ == '__main__':
    unittest.main()
