import os
import sys
import unittest
from run_binary import create_input_csv, run_bytecode, read_output_csv
import run_binary



def print_test_str(req_violated, test_csv, descr):
    print(f"\nFailure: ({req_violated} violated) {test_csv}: {descr}")


class all_bad_tests(unittest.TestCase):
    pyc_location = "../bytecode_3_9/election.pyc"
    # def setUp(self):
    #     if len(sys.argv) > 1:
    #         print("argv: ", sys.argv)
    #         self.pyc_location = sys.argv[1]
    #     else:
    #         self.pyc_location = "../bytecode_3_9/election.pyc"

    def test_rq10_same_riding_same_party_by_space(self):
        # self.same_riding_same_party_space = [
        #     {"RidingNum": "1",
        #      "Riding": "home",
        #      "FirstName": "A",
        #      "LastName": "B",
        #      "Party": "home",
        #      "Votes": 4},
        #     {"RidingNum": "1",
        #      "Riding": "home",
        #      "FirstName": "X",
        #      "LastName": "Y",
        #      "Party": "home  ",
        #      "Votes": 4}
        # ]
        # create_input_csv(self.same_riding_same_party_space, "../test_input/same_riding_same_party_space.csv")
        code, out = run_bytecode("../test_input/same_riding_same_party_space.csv", "../test", self.pyc_location)
        print_test_str("R10", "/test_input/same_riding_same_party_space.csv", "The program does not correctly identify equivalent Party entries up to trailing whitespace, allowing for multiple candidates per riding")

        self.assertNotEqual(code, 0)

    def test_rq6_bad_error_fname(self):
        # self.bad_fname_bad_error_message = [
        #     {"RidingNum": "1",
        #      "Riding": "home",
        #      "FirstName": "p",
        #      "LastName": "B",
        #      "Party": "home",
        #      "Votes": 4},
        #     {"RidingNum": "2",
        #      "Riding": "school",
        #      "FirstName": "X",
        #      "LastName": "Y",
        #      "Party": "school",
        #      "Votes": 4},
        #     {"RidingNum": "2",
        #      "Riding": "school",
        #      "FirstName": "x",
        #      "LastName": "y",
        #      "Party": "work",
        #      "Votes": 4},
        #     {"RidingNum": "2",
        #      "Riding": "school",
        #      "FirstName": "$",
        #      "LastName": "n",
        #      "Party": "pool",
        #      "Votes": 4}
        # ]
        # create_input_csv(self.bad_fname_bad_error_message, "../test_input/bad_fname_bad_error_message.csv")
        code, out = run_bytecode("../test_input/bad_fname_bad_error_message.csv", "../test", self.pyc_location)
        print_test_str("R11", "/test_input/bad_fname_bad_error_message.csv", "The program does not identify correctly the row where the problem occurs")

        self.assertNotEqual(code, 0)
        self.assertIn("Row 4", out)

    def test_rq5_lname(self):
        # self.bad_l_name = [
        #     {"RidingNum": "1",
        #      "Riding": "A",
        #      "FirstName": "A",
        #      "LastName": "$",
        #      "Party": "home",
        #      "Votes": 4},
        #     {"RidingNum": "2",
        #      "Riding": "school",
        #      "FirstName": "X",
        #      "LastName": "Y",
        #      "Party": "school",
        #      "Votes": 4}
        # ]
        #
        # create_input_csv(self.bad_l_name, "../test_input/bad_l_name.csv")
        code, out = run_bytecode("../test_input/bad_l_name.csv", "../test", self.pyc_location)
        print_test_str("R5", "/test_input/bad_l_name.csv", "The program does not identify invalid characters in the LastName field")

        self.assertNotEqual(code, 0)


    def test_Type_Error(self):  # wtf type error when only independent candidates
        # self.type_csv = [
        #     {"RidingNum": "1",
        #      "Riding": "home",
        #      "FirstName": "A",
        #      "LastName": "B",
        #      "Party": "independent",
        #      "Votes": 4},
        # ]
        # create_input_csv(self.type_csv, "../test_input/type_csv.csv")
        code, out = run_bytecode("../test_input/type_csv.csv", "../test", self.pyc_location)
        print_test_str("R11, R12", "/test_input/type_csv.csv", "The program throws a TypeError when there are only \"independent\" entries under Party")

        self.assertEqual(code, 0)


    def test_rq29_minority_indep_equals_main_party(self):
        # self.minority_indep_equals_main_party = [
        #     {"RidingNum": 1,
        #      "Riding": "home",
        #      "FirstName": "A",
        #      "LastName": "B",
        #      "Party": "work",
        #      "Votes": 2},
        #     {"RidingNum": 2,
        #      "Riding": "s",
        #      "FirstName": "a",
        #      "LastName": "x",
        #      "Party": "work",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "a",
        #      "FirstName": "s",
        #      "LastName": "d",
        #      "Party": "school",
        #      "Votes": 1},
        #     {"RidingNum": 4,
        #      "Riding": "b",
        #      "FirstName": "b",
        #      "LastName": "x",
        #      "Party": "independent",
        #      "Votes": 2},
        #     {"RidingNum": 5,
        #      "Riding": "c",
        #      "FirstName": "s",
        #      "LastName": "a",
        #      "Party": "independent",
        #      "Votes": 1}
        # ]
        # create_input_csv(self.minority_indep_equals_main_party, "../test_input/minority_indep_equals_main_party.csv")
        code, out = run_bytecode("../test_input/minority_indep_equals_main_party.csv", "../test", self.pyc_location)
        self.assertEqual(code, 0)
        riding, nation = read_output_csv("../test")
        role_work = ""
        role_school = ""
        for line in nation:
            if line["Party"] == "work":
                role_work = line["Role"]
            if line["Party"] == "school":
                role_school = line["Role"]
        print_test_str("R29", "/test_input/minority_indep_equals_main_party.csv", "The program does not correctly output \"government (minority)\" under Role in federal_results.csv")

        self.assertEqual(role_work, "government (minority)")
        self.assertEqual(role_school, "official opposition")


    def test_number_with_space_before_riding(self):
        # input = [
        #     {"RidingNum": " 1",
        #      "Riding": "DoesNotMatchAnythingElse",
        #      "LastName": "Solis",
        #      "FirstName": "Em",
        #      "Party": "Math",
        #      "Votes": 4},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Zhu",
        #      "FirstName": "Clark",
        #      "Party": "Math",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Grav",
        #      "FirstName": "Soph",
        #      "Party": "Math",
        #      "Votes": 4},
        #     {"RidingNum": "1 ",
        #      "Riding": "AlsoDoesNotMatch",
        #      "FirstName": "Yol",
        #      "LastName": "Ren",
        #      "Party": "Green",
        #      "Votes": 32},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Br",
        #      "FirstName": "Ma",
        #      "Party": "Green",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Lowkey idk",
        #      "FirstName": "Rom",
        #      "Party": "Green",
        #      "Votes": 4},
        #     {"RidingNum": 1,
        #      "Riding": "Uni",
        #      "FirstName": "Av",
        #      "LastName": "New",
        #      "Party": "Buckethead",
        #      "Votes": 3},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Li",
        #      "FirstName": "Dec",
        #      "Party": "Buckethead",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "j",
        #      "FirstName": "Sar",
        #      "Party": "Buckethead",
        #      "Votes": 400},
        # ]
        # run_binary.create_input_csv(input, "../test_input/number_with_space_before_riding.csv")
        code, reason = run_binary.run_bytecode("../test_input/number_with_space_before_riding.csv", "../test", self.pyc_location)
        # ride_level, fed_level = run_binary.read_output_csv("../test")
        print_test_str("R4", "/test_input/number_with_space_before_riding.csv", "The program does not correctly detect the leading whitespace in the RidingNum field")

        self.assertEqual(code, 1)


    def test_riding_clash_caps(self):
        # input = [
        #     {"RidingNum": "1",
        #      "Riding": "Un i",
        #      "LastName": "Solis",
        #      "FirstName": "Em",
        #      "Party": "Math",
        #      "Votes": 4},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Zhu",
        #      "FirstName": "Clark",
        #      "Party": "Math",
        #      "Votes": 2},
        #     {"RidingNum": 5,
        #      "Riding": "Un I",
        #      "LastName": "Grav",
        #      "FirstName": "Soph",
        #      "Party": "Math",
        #      "Votes": 4},
        #     {"RidingNum": "1",
        #      "Riding": "Un I",
        #      "FirstName": "Yol",
        #      "LastName": "Ren",
        #      "Party": "Green",
        #      "Votes": 32},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Br",
        #      "FirstName": "Ma",
        #      "Party": "Green",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Lowkey idk",
        #      "FirstName": "Rom",
        #      "Party": "Green",
        #      "Votes": 4},
        #     {"RidingNum": 1,
        #      "Riding": "Un I",
        #      "FirstName": "Av",
        #      "LastName": "New",
        #      "Party": "Buckethead",
        #      "Votes": 3},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Li",
        #      "FirstName": "Dec",
        #      "Party": "Buckethead",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "j",
        #      "FirstName": "Sar",
        #      "Party": "Buckethead",
        #      "Votes": " 400"},
        # ]
        # run_binary.create_input_csv(input, "../test_input/riding_clash_caps.csv")
        code, reason = run_binary.run_bytecode("../test_input/riding_clash_caps.csv", "../test", self.pyc_location)
        # ride_level, fed_level = run_binary.read_output_csv("../test")
        print_test_str("R13, R8", "/test_input/riding_clash_caps.csv", "It is possible to create two rows with equivalent entries in Riding by inserting a space in the middle of an entry, but have the RidingNum be different")

        self.assertEqual(code, 1)



    def test_riding_clash_bad_integer(self):
        # input = [
        #     {"RidingNum": "01",
        #      "Riding": "Uni-",
        #      "LastName": "Solis",
        #      "FirstName": "Em",
        #      "Party": "Math",
        #      "Votes": 4},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Zhu",
        #      "FirstName": "Clark",
        #      "Party": "Math",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Grav",
        #      "FirstName": "Soph",
        #      "Party": "Math",
        #      "Votes": 4},
        #     {"RidingNum": "001",
        #      "Riding": "Un-i",
        #      "FirstName": "Yol",
        #      "LastName": "Ren",
        #      "Party": "Green",
        #      "Votes": 32},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Br",
        #      "FirstName": "Ma",
        #      "Party": "Green",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Lowkey idk",
        #      "FirstName": "Rom",
        #      "Party": "Green",
        #      "Votes": 4},
        #     {"RidingNum": 1,
        #      "Riding": "-Uni",
        #      "FirstName": "Av",
        #      "LastName": "New",
        #      "Party": "Buckethead",
        #      "Votes": 3},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Li",
        #      "FirstName": "Dec",
        #      "Party": "Buckethead",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "j",
        #      "FirstName": "Sar",
        #      "Party": "Buckethead",
        #      "Votes": " 400"},
        # ]
        # run_binary.create_input_csv(input, "../test_input/riding_clash_bad_integer.csv")
        code, reason = run_binary.run_bytecode("../test_input/riding_clash_bad_integer.csv", "../test", self.pyc_location)
        # ride_level, fed_level = run_binary.read_output_csv("../test")
        print_test_str("R8", "/test_input/riding_clash_bad_integer.csv", "The program does not correctly handle leading zeros in the RidingNum field, we can create two different Ridings for the same RidingNum")

        self.assertEqual(code, 1)


    def test_one_candidate_caps(self):
        # input = [
        #     {"RidingNum": "1",
        #      "Riding": "Uni",
        #      "LastName": "Solis",
        #      "FirstName": "Em",
        #      "Party": "Math",
        #      "Votes": 4},
        #     {"RidingNum": "1",
        #      "Riding": "Uni",
        #      "LastName": "Solis",
        #      "FirstName": "Emi",
        #      "Party": "MaTh",  # should be illegal
        #      "Votes": 4},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Zhu",
        #      "FirstName": "Clark",
        #      "Party": "Math",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Grav",
        #      "FirstName": "Soph",
        #      "Party": "Math",
        #      "Votes": 4},
        #     {"RidingNum": "1",
        #      "Riding": "Uni",
        #      "FirstName": "Yol",
        #      "LastName": "Ren",
        #      "Party": "Green",
        #      "Votes": 32},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Br",
        #      "FirstName": "Ma",
        #      "Party": "Green",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Lowkey idk",
        #      "FirstName": "Rom",
        #      "Party": "Green",
        #      "Votes": 4},
        #     {"RidingNum": 1,
        #      "Riding": "Uni",
        #      "FirstName": "Av",
        #      "LastName": "New",
        #      "Party": "Buckethead",
        #      "Votes": 3},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Li",
        #      "FirstName": "Dec",
        #      "Party": "Buckethead",
        #      "Votes": 2},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "j",
        #      "FirstName": "Sar",
        #      "Party": "Buckethead",
        #      "Votes": " 400"},
        # ]
        # run_binary.create_input_csv(input, "../test_input/one_candidate_caps.csv")
        code, reason = run_binary.run_bytecode("../test_input/one_candidate_caps.csv", "../test", self.pyc_location)
        # ride_level, fed_level = run_binary.read_output_csv("../test")
        print_test_str("R13, R8", "/test_input/one_candidate_caps.csv", "The program incorrectly allows for multiple Parties with equivalent names")

        self.assertEqual(code, 1)



    def test_vote_total_no_votes(self):
        # input = [
        #     {"RidingNum": 1,
        #      "Riding": "Uni",
        #      "LastName": "Solis",
        #      "FirstName": "Em",
        #      "Party": "Math",
        #      "Votes": 0},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Zhu",
        #      "FirstName": "Clark",
        #      "Party": "Math",
        #      "Votes": 0},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Grav",
        #      "FirstName": "Soph",
        #      "Party": "Math",
        #      "Votes": 0},
        #     {"RidingNum": 1,
        #      "Riding": "Uni",
        #      "FirstName": "Yol",
        #      "LastName": "Ren",
        #      "Party": "Green",
        #      "Votes": 0},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Br",
        #      "FirstName": "Ma",
        #      "Party": "Green",
        #      "Votes": 0},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "Lowkey idk",
        #      "FirstName": "Rom",
        #      "Party": "Green",
        #      "Votes": 0},
        #     {"RidingNum": 1,
        #      "Riding": "Uni",
        #      "FirstName": "Av",
        #      "LastName": "New",
        #      "Party": "Buckethead",
        #      "Votes": 0},
        #     {"RidingNum": 2,
        #      "Riding": "Ken",
        #      "LastName": "Li",
        #      "FirstName": "Dec",
        #      "Party": "Buckethead",
        #      "Votes": 0},
        #     {"RidingNum": 3,
        #      "Riding": "York",
        #      "LastName": "j",
        #      "FirstName": "Sar",
        #      "Party": "Buckethead",
        #      "Votes": 0},
        # ]
        # run_binary.create_input_csv(input, "../test_input/vote_total_no_votes.csv")
        code, reason = run_binary.run_bytecode("../test_input/vote_total_no_votes.csv", "../test", self.pyc_location)
        # ride_level, fed_level = run_binary.read_output_csv("../test")
        print_test_str("R11, R12", "/test_input/vote_total_no_votes.csv", "The program throws a ValueError when all Votes are 0 instead of terminating ")

        self.assertEqual(code, 0)



    def test_outcome_only_recount_on_point(self):
        # input = [
        #     {"RidingNum": 1,
        #      "Riding": "Uni",
        #      "LastName": "Solis",
        #      "FirstName": "Em",
        #      "Party": "Math",
        #      "Votes": 333},
        #     {"RidingNum": 1,
        #      "Riding": "Uni",
        #      "FirstName": "Yol",
        #      "LastName": "Ren",
        #      "Party": "Green",
        #      "Votes": 333},
        #     {"RidingNum": 1,
        #      "Riding": "Uni",
        #      "FirstName": "Av",
        #      "LastName": "New",
        #      "Party": "Buckethead",
        #      "Votes": 334},
        # ]
        # run_binary.create_input_csv(input, "../test_input/outcome_only_recount_on_point.csv")
        run_binary.run_bytecode("../test_input/outcome_only_recount_on_point.csv", "../test", self.pyc_location)
        ride_level, fed_level = run_binary.read_output_csv("../test")
        for line in ride_level:
            if line["RidingNum"] == "1":
                print_test_str("R17", "/test_input/outcome_only_recount_on_point.csv",
                               "The program incorrectly outputs \"plurality\" under the Outcome in riding_result.csv instead of \"recount\"")

                self.assertEqual(line["Outcome"], "Recount")



    def tearDown(self) -> None:
        if os.path.exists("../test/input.csv"):
            os.remove("../test/input.csv")
        if os.path.exists("../test/a.csv"):
            os.remove("../test/a.csv")
        if os.path.exists("../test/b.csv"):
            os.remove("../test/b.csv")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # print("argv: ", sys.argv)
        all_bad_tests.pyc_location = sys.argv.pop()
    unittest.main()