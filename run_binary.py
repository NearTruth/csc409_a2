import csv
import subprocess
import typing

headers = ("RidingNum", "Riding", "LastName", "FirstName", "Party", "Votes")
pyc_location = "../../bytecode_3_11/election.pyc"

def create_input_csv(input_dict: list(dict[str, any]), file_location: str):  # file_location is the place to put the generated input file
    with open(file_location + "/input.csv", "w", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(input_dict)

def run_bytecode(output_location: str):  # assuming that output location is the same as where the input.csv is
    try:
        subprocess.check_output(["python.exe", pyc_location, output_location + "/input.csv", output_location + "/a.csv", output_location + "/b.csv"],
                            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as ex:
        print("FAIL\n" + f"CODE: {ex.returncode}\n"+ "REASON:" + ex.output.decode("ascii"))

def read_output_csv(output_location: str):
    lst_a = []
    lst_b = []
    with open(output_location+ "/a.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lst_a.append(row)

    print(lst_a)
    with open(output_location+ "/b.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lst_b.append(row)
    print(lst_b)
    return lst_a, lst_b

if __name__ == "__main__":
    dd = [
        {"RidingNum": 1,
        "Riding": "a",
        "LastName": "$",
        "FirstName": "Xaaaa",
        "Party": "a",
        "Votes": 4},
        {"RidingNum": 1,
         "Riding": "a",
         "LastName": "D",
         "FirstName": "d",
         "Party": "a",
         "Votes": 2},
        {"RidingNum": "-2",
        "Riding": "b",
        "FirstName": "Y",
        "LastName": "B",
        "Party": "a",
        "Votes": 4},
        ]

    create_input_csv(dd, "../test")
    run_bytecode("../test")
    read_output_csv("../test")




