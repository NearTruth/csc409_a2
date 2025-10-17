import csv
import subprocess
import typing

headers = ("RidingNum", "Riding", "LastName", "FirstName", "Party", "Votes")
# pyc_location = "../bytecode_3_9/election.pyc"

def create_input_csv(input_dict: list[dict[str, any]], file_location: str):  # file_location is the place to put the generated input file
    with open(file_location, "w", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(input_dict)

def run_bytecode(input_location: str, output_location: str, pyc_location: str):  # assuming that output location is the same as where the input.csv is
    try:
        subprocess.check_output(["python.exe", pyc_location, input_location, output_location + "/a.csv", output_location + "/b.csv"],
                            stderr=subprocess.STDOUT)
        return 0, None
    except subprocess.CalledProcessError as ex:
        # print("FAIL\n" + f"CODE: {ex.returncode}\n"+"REASON:" + ex.output.decode("ascii"))
        return ex.returncode, ex.output.decode("ascii")

def read_output_csv(output_location: str):

    """
    returns list of rows as dictionary
    """
    lst_a = []
    lst_b = []
    with open(output_location+ "/a.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lst_a.append(row)
    with open(output_location+ "/b.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lst_b.append(row)
    return lst_a, lst_b


if __name__ == "__main__":
    dd = [
        {"RidingNum": 1,
        "Riding": "a",
        "LastName": "e",
        "FirstName": "Xaaaa",
        "Party": "a",
        "Votes": 4},
        {"RidingNum": 4,
         "Riding": "ad",
         "LastName": "D",
         "FirstName": "d",
         "Party": "a   ",
         "Votes": 2},
        {"RidingNum": "2",
        "Riding": "b",
        "FirstName": "Y",
        "LastName": "a",
        "Party": "a",
        "Votes": f"4"},
        {"RidingNum": "6",
        "Riding": "y",
        "FirstName": "d",
        "LastName": "B",
        "Party": "a",
        "Votes": f"4"}
        ]

    create_input_csv(dd, "../test")
    run_bytecode("../test/input.csv", "../test")
    print(read_output_csv("../test"))




