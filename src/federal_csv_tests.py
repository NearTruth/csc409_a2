import os
import unittest
from run_binary import create_input_csv, run_bytecode, read_output_csv


class federal_csv_tests(unittest.TestCase):
    def setUp(self) -> None:
        pass




    def test_rq24_valid(self):
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
             "Votes": 4},
            {"RidingNum": "3",
             "Riding": "work",
             "FirstName": "y",
             "LastName": "z",
             "Party": "school",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        self.assertEqual(list(nation[0].keys()), ['Party', 'Seats', 'Votes', '%vote', 'Role'])

    def test_rq24_no_winner(self):
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
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "3",
             "Riding": "work",
             "FirstName": "y",
             "LastName": "z",
             "Party": "school",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        self.assertEqual(list(nation[0].keys()), ['Party', 'Seats', 'Votes', '%vote', 'Role'])

    def test_rq25_independents(self):
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
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "independent",
             "Votes": 4},
            {"RidingNum": "3",
             "Riding": "work",
             "FirstName": "y",
             "LastName": "z",
             "Party": "independent",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        ref_set = {"home", "independent", "school", "total"}
        csv_set = set()
        for line in nation:
            csv_set.add(line["Party"])
        self.assertEqual(csv_set, ref_set)

    def test_rq25_no_independents(self):
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
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "3",
             "Riding": "work",
             "FirstName": "y",
             "LastName": "z",
             "Party": "play",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        ref_set = {"home", "work", "school", "play", "total"}
        csv_set = set()
        for line in nation:
            csv_set.add(line["Party"])
        self.assertEqual(csv_set, ref_set)


    def test_rq25_one_party(self):
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
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "home",
             "Votes": 4},
            {"RidingNum": "3",
             "Riding": "work",
             "FirstName": "y",
             "LastName": "z",
             "Party": "home",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        ref_set = {"home", "total"}
        csv_set = set()
        for line in nation:
            csv_set.add(line["Party"])
        self.assertEqual(csv_set, ref_set)

    def test_rq25_only_independent(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "independent",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "independent",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "independent",
             "Votes": 4},
            {"RidingNum": "3",
             "Riding": "work",
             "FirstName": "y",
             "LastName": "z",
             "Party": "independent",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        ref_set = {"independent", "total"}
        csv_set = set()
        for line in nation:
            csv_set.add(line["Party"])
        self.assertEqual(csv_set, ref_set)

    def test_Type_Error(self):  # wtf type error when only independent candidates
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "independent",
             "Votes": 4},
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)

    def test_rq26_one_seat_with_independents(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "independent",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "independent",
             "Votes": 4},
            {"RidingNum": "3",
             "Riding": "work",
             "FirstName": "y",
             "LastName": "z",
             "Party": "independent",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        num_ridings_indep = 0
        num_ridings = 0
        for line in nation:
            if line["Party"] == "independent":
                num_ridings_indep = line["Seats"]
            elif line["Party"] == "work":
                num_ridings = line["Seats"]

        self.assertEqual(num_ridings_indep, '3')
        self.assertEqual(num_ridings, '1')


    def test_rq26_multi_parties(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "school",
             "FirstName": "X",
             "LastName": "Y",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "3",
             "Riding": "work",
             "FirstName": "y",
             "LastName": "z",
             "Party": "school",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        num_ridings_sch = 0
        num_ridings = 0
        for line in nation:
            if line["Party"] == "school":
                num_ridings_sch = line["Seats"]
            elif line["Party"] == "work":
                num_ridings = line["Seats"]

        self.assertEqual(num_ridings_sch, '2')
        self.assertEqual(num_ridings, '2')

    def test_rq26_multi_parties_single_instance(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        num_ridings_sch = 0
        num_ridings = 0
        for line in nation:
            if line["Party"] == "school":
                num_ridings_sch = line["Seats"]
            elif line["Party"] == "work":
                num_ridings = line["Seats"]

        self.assertEqual(num_ridings_sch, '1')
        self.assertEqual(num_ridings, '1')

    def test_rq26_single_party_single_instance(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        num_ridings = 0
        for line in nation:
            if line["Party"] == "work":
                num_ridings = line["Seats"]

        self.assertEqual(num_ridings, '1')

    def test_rq26_multi_parties_contested(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "x",
             "LastName": "y",
             "Party": "work",
             "Votes": 3}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        num_ridings_sch = 0
        num_ridings = 0
        for line in nation:
            if line["Party"] == "school":
                num_ridings_sch = line["Seats"]
            elif line["Party"] == "work":
                num_ridings = line["Seats"]

        self.assertEqual(num_ridings_sch, '1')
        self.assertEqual(num_ridings, '1')


    def test_rq26_multi_parties_one_winner(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "p",
             "LastName": "l",
             "Party": "school",
             "Votes": 5},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "x",
             "LastName": "y",
             "Party": "work",
             "Votes": 3}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        num_ridings_sch = 0
        num_ridings = 0
        for line in nation:
            if line["Party"] == "school":
                num_ridings_sch = int(line["Seats"])
            elif line["Party"] == "work":
                num_ridings = int(line["Seats"])

        self.assertEqual(num_ridings_sch, 2)
        self.assertEqual(num_ridings, 0)

    def test_rq26_multi_parties_all_zero(self):  # division by 0
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 0},
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "p",
             "LastName": "l",
             "Party": "school",
             "Votes": 0},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 0},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "x",
             "LastName": "y",
             "Party": "work",
             "Votes": 0}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        num_ridings_sch = 0
        num_ridings = 0
        for line in nation:
            if line["Party"] == "school":
                num_ridings_sch = int(line["Seats"])
            elif line["Party"] == "work":
                num_ridings = int(line["Seats"])

        self.assertEqual(num_ridings_sch, 0)
        self.assertEqual(num_ridings, 0)


    def test_rq27_single_party(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["Votes"])

        self.assertEqual(percent_work, 4)

    def test_rq27_two_party(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "x",
             "LastName": "y",
             "Party": "school",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        percent_school = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["Votes"])
            if line["Party"] == "school":
                percent_school = float(line["Votes"])

        self.assertEqual(percent_work, 4)
        self.assertEqual(percent_school, 8)

    def test_rq27_two_party_contested(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "x",
             "LastName": "y",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "d",
             "LastName": "e",
             "Party": "work",
             "Votes": 3}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        percent_school = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = int(line["Votes"])
            if line["Party"] == "school":
                percent_school = int(line["Votes"])

        self.assertEqual(percent_work, 7)
        self.assertEqual(percent_school, 8)

    def test_rq27_with_independents(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "x",
             "LastName": "y",
             "Party": "independent",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "d",
             "LastName": "e",
             "Party": "independent",
             "Votes": 3}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        percent_school = 0
        percent_independent = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = int(line["Votes"])
            if line["Party"] == "school":
                percent_school = int(line["Votes"])
            if line["Party"] == "independent":
                percent_independent = int(line["Votes"])

        self.assertEqual(percent_work, 4)
        self.assertEqual(percent_school, 4)
        self.assertEqual(percent_independent, 7)

    def test_rq27_single_party_with_independent_no_votes(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 0},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "d",
             "LastName": "e",
             "Party": "independent",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        percent_independent = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["Votes"])
            if line["Party"] == "independent":
                percent_independent = float(line["Votes"])

        self.assertEqual(percent_work, 0)
        self.assertEqual(percent_independent, 4)

    def test_rq27_single_party_no_votes(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 0}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["Votes"])

        self.assertEqual(percent_work, 0)

    def test_rq28_single_party(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["%vote"])

        self.assertEqual(percent_work, 100.0)

    def test_rq28_two_party(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "x",
             "LastName": "y",
             "Party": "school",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        percent_school = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["%vote"])
            if line["Party"] == "school":
                percent_school = float(line["%vote"])

        self.assertEqual(percent_work, 33.333)
        self.assertEqual(percent_school, 66.667)

    def test_rq28_two_party_contested(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "x",
             "LastName": "y",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "d",
             "LastName": "e",
             "Party": "work",
             "Votes": 3}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        percent_school = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["%vote"])
            if line["Party"] == "school":
                percent_school = float(line["%vote"])

        self.assertEqual(percent_work, 46.667)
        self.assertEqual(percent_school, 53.333)

    def test_rq28_with_independents(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 4},
            {"RidingNum": "4",
             "Riding": "a",
             "FirstName": "p",
             "LastName": "q",
             "Party": "school",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "x",
             "LastName": "y",
             "Party": "independent",
             "Votes": 4},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "d",
             "LastName": "e",
             "Party": "independent",
             "Votes": 3}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        percent_school = 0
        percent_independent = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["%vote"])
            if line["Party"] == "school":
                percent_school = float(line["%vote"])
            if line["Party"] == "independent":
                percent_independent = float(line["%vote"])

        self.assertEqual(percent_work, 26.667)
        self.assertEqual(percent_school, 26.667)
        self.assertEqual(percent_independent, 46.667)

    def test_rq28_single_party_with_independent_no_votes(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 0},
            {"RidingNum": "2",
             "Riding": "b",
             "FirstName": "d",
             "LastName": "e",
             "Party": "independent",
             "Votes": 4}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        percent_independent = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["%vote"])
            if line["Party"] == "independent":
                percent_independent = float(line["%vote"])

        self.assertEqual(percent_work, 0)
        self.assertEqual(percent_independent, 100.0)

    def test_rq28_single_party_no_votes(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 0}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = float(line["%vote"])

        self.assertEqual(percent_work, 0.0)

    def test_rq29_majority(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 1}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        percent_work = 0
        for line in nation:
            if line["Party"] == "work":
                percent_work = line["Role"]
        self.assertEqual(percent_work, "government (majority)")

    def test_rq29_majority_opposition(self):
        self.valid_csv = [
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 2},
            {"RidingNum": 2,
             "Riding": "s",
             "FirstName": "a",
             "LastName": "x",
             "Party": "work",
             "Votes": 2},
            {"RidingNum": "1",
             "Riding": "home",
             "FirstName": "s",
             "LastName": "d",
             "Party": "school",
             "Votes": 1}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        role_work = ""
        role_school = ""
        for line in nation:
            if line["Party"] == "work":
                role_work = line["Role"]
            if line["Party"] == "school":
                role_school = line["Role"]
        self.assertEqual(role_work, "government (majority)")
        self.assertEqual(role_school, "official opposition")

    def test_rq29_minority(self):
        self.valid_csv = [
            {"RidingNum": 1,
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 2},
            {"RidingNum": 2,
             "Riding": "s",
             "FirstName": "a",
             "LastName": "x",
             "Party": "work",
             "Votes": 2},
            {"RidingNum": 3,
             "Riding": "a",
             "FirstName": "s",
             "LastName": "d",
             "Party": "school",
             "Votes": 1},
            {"RidingNum": 4,
             "Riding": "b",
             "FirstName": "b",
             "LastName": "x",
             "Party": "independent",
             "Votes": 2},
            {"RidingNum": 5,
             "Riding": "c",
             "FirstName": "s",
             "LastName": "a",
             "Party": "independent",
             "Votes": 1},
            {"RidingNum": 6,
             "Riding": "d",
             "FirstName": "p",
             "LastName": "a",
             "Party": "independent",
             "Votes": 1},
            {"RidingNum": 7,
             "Riding": "e",
             "FirstName": "q",
             "LastName": "a",
             "Party": "independent",
             "Votes": 1}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        role_work = ""
        role_school = ""
        for line in nation:
            if line["Party"] == "work":
                role_work = line["Role"]
            if line["Party"] == "school":
                role_school = line["Role"]
        self.assertEqual(role_work, "government (minority)")
        self.assertEqual(role_school, "official opposition")

    def test_rq29_minority_indep_equals_main_party(self):
        self.valid_csv = [
            {"RidingNum": 1,
             "Riding": "home",
             "FirstName": "A",
             "LastName": "B",
             "Party": "work",
             "Votes": 2},
            {"RidingNum": 2,
             "Riding": "s",
             "FirstName": "a",
             "LastName": "x",
             "Party": "work",
             "Votes": 2},
            {"RidingNum": 3,
             "Riding": "a",
             "FirstName": "s",
             "LastName": "d",
             "Party": "school",
             "Votes": 1},
            {"RidingNum": 4,
             "Riding": "b",
             "FirstName": "b",
             "LastName": "x",
             "Party": "independent",
             "Votes": 2},
            {"RidingNum": 5,
             "Riding": "c",
             "FirstName": "s",
             "LastName": "a",
             "Party": "independent",
             "Votes": 1}
        ]
        create_input_csv(self.valid_csv, "../test")
        code, out = run_bytecode("../test/input.csv", "../test")
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        role_work = ""
        role_school = ""
        for line in nation:
            if line["Party"] == "work":
                role_work = line["Role"]
            if line["Party"] == "school":
                role_school = line["Role"]
        self.assertEqual(role_work, "government (minority)")
        self.assertEqual(role_school, "official opposition")

    def tearDown(self) -> None:
        if os.path.exists("../test/input.csv"):
            os.remove("../test/input.csv")
        if os.path.exists("../test/a.csv"):
            os.remove("../test/a.csv")
        if os.path.exists("../test/b.csv"):
            os.remove("../test/b.csv")


if __name__ == '__main__':
    unittest.main()