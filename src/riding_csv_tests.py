import os
import unittest
from run_binary import create_input_csv, run_bytecode, read_output_csv


class riding_csv_tests(unittest.TestCase):
    def setUp(self) -> None:


    def test_part_name_with_space(self):
        create_input_csv(self.bad_party_space, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        riding, nation = read_output_csv("../test")
        self.assertNotEqual(code, 0)
        print(riding)

    def tearDown(self) -> None:
        if os.path.exists("../test/input.csv"):
            os.remove("../test/input.csv")
        if os.path.exists("../test/a.csv"):
            os.remove("../test/a.csv")
        if os.path.exists("../test/b.csv"):
            os.remove("../test/b.csv")


if __name__ == '__main__':
    unittest.main()