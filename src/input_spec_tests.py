import os
import unittest
from run_binary import create_input_csv, run_bytecode, read_output_csv


class riding_csv_tests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
               "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "school",
             "Votes": 4}
        ]
        self.invalid_csv = [  # missing entry on second row
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "",
             "Riding": "school",
             "FirstName": "",
             "LastName": "Y",
             "Party": "school",
             "Votes": ""}
        ]

        self.empty_csv = [  # missing entry on second row
            {"RidingNum": "",
             "Riding": "",
             "FirstName": "",
             "LastName": "",
             "Party": "",
             "Votes": ""},
        ]

        self.bad_riding = [
            {"RidingNum": "1",
             "Riding": "$",
             "FirstName": "A",
             "LastName": "B",
               "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "school",
             "Votes": 4}
        ]

        self.bad_f_name = [
            {"RidingNum": "1",
             "Riding": "A",
             "FirstName": "$",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "school",
             "Votes": 4}
        ]

        self.bad_l_name = [
            {"RidingNum": "1",
             "Riding": "A",
             "FirstName": "A",
             "LastName": "$",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "school",
             "Votes": 4}
        ]

        self.bad_num_name = [
            {"RidingNum": "1",
             "Riding": "A",
             "FirstName": 1234,
             "LastName": "A",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "school",
             "Votes": 4}
        ]

        self.bad_party_space = [
            {"RidingNum": "1",
             "Riding": "A",
             "FirstName": "A",
             "LastName": "A",
             "Party": "home     ",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "school",
             "Votes": 4}
        ]

        self.bad_party_invalid_char = [
            {"RidingNum": "1",
             "Riding": "A",
             "FirstName": "A",
             "LastName": "A",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "$$$",
             "Votes": 4}
        ]

        self.bad_riding_bad_error_message = [
            {"RidingNum": "1",
             "Riding": "$",
             "FirstName": "A",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "school",
             "Votes": 4}
        ]

        self.bad_fname_bad_error_message = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "p",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "x",
             "LastName": "y",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "$",
             "LastName": "n",
             "Party": "pool",
             "Votes": 4}
        ]

        self.bad_party_int = [
            {"RidingNum": "1",
             "Riding": "A",
             "FirstName": "A",
             "LastName": "A",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": 12,
             "Votes": 4}
        ]

        self.bad_party_float = [
            {"RidingNum": "1",
             "Riding": "A",
             "FirstName": "A",
             "LastName": "A",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": 12.2223,
             "Votes": 4}
        ]

        self.bad_same_names_diff_riding = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "A",
             "LastName": "B",
             "Party": "school",
             "Votes": 4}
        ]

        self.bad_same_names_same_riding = [
            {"RidingNum": "1",
             "Riding": "school",
             "FirstName": "A",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "1",
             "Riding": "school",
             "FirstName": "A",
             "LastName": "B",
             "Party": "school",
             "Votes": 4}
        ]

        self.diff_names_space = [
            {"RidingNum": "1",
             "Riding": "school",
             "FirstName": "A",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "1",
             "Riding": "school",
             "FirstName": "A ",
             "LastName": "B",
             "Party": "school",
             "Votes": 4}
        ]

        self.diff_names_space_middle = [
            {"RidingNum": "1",
             "Riding": "school",
             "FirstName": "A  Aaa",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "1",
             "Riding": "school",
             "FirstName": "A aaa",
             "LastName": "B",
             "Party": "school",
             "Votes": 4}
        ]

        self.space_diff_names = [
            {"RidingNum": "1",
             "Riding": "school",
             "FirstName": " ",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "1",
             "Riding": "school",
             "FirstName": "  ",
             "LastName": "B",
             "Party": "school",
             "Votes": 4}
        ]

        self.same_riding_same_party = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "home",
             "Votes": 4}
        ]

        self.same_riding_same_party_space = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "home  ",
             "Votes": 4}
        ]

    def test_valid(self):
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)

    def test_rq1_invalid(self):
        create_input_csv(self.empty_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq3_invalid(self):
        create_input_csv(self.invalid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq5_riding(self):
        create_input_csv(self.bad_riding, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq5_fname(self):
        create_input_csv(self.bad_f_name, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq5_lname(self):
        create_input_csv(self.bad_l_name, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq5_numname(self):
        create_input_csv(self.bad_num_name, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq6_space(self):
        create_input_csv(self.bad_party_space, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)

    def test_rq6_invalid_char(self):
        create_input_csv(self.bad_party_invalid_char, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq6_int(self):
        create_input_csv(self.bad_party_int, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq6_float(self):
        create_input_csv(self.bad_party_float, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq6_bad_error_riding(self):  # outputs row 2 even when not row 2
        create_input_csv(self.bad_riding_bad_error_message, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)
        self.assertIn("Row 1", out)

    def test_rq6_bad_error_fname(self):
        create_input_csv(self.bad_fname_bad_error_message, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)
        self.assertIn("Row 4", out)

    def test_rq9_bad_same_name_diff_riding(self):
        create_input_csv(self.bad_same_names_diff_riding, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq9_bad_same_name_same_riding(self):
        create_input_csv(self.bad_same_names_same_riding, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq9_diff_by_space(self):
        create_input_csv(self.diff_names_space, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq9_random_capitalization(self):
        create_input_csv(self.diff_names_space_middle, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq10_same_riding_same_party(self):
        create_input_csv(self.same_riding_same_party, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)

    def test_rq10_same_riding_same_party_by_space(self):
        create_input_csv(self.same_riding_same_party_space, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertNotEqual(code, 0)



    def tearDown(self) -> None:
        if os.path.exists("../test/input.csv"):
            os.remove("../test/input.csv")
        if os.path.exists("../test/a.csv"):
            os.remove("../test/a.csv")
        if os.path.exists("../test/b.csv"):
            os.remove("../test/b.csv")


if __name__ == '__main__':
    unittest.main()



