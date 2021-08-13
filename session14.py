#Importing packages
from datetime import datetime
from backports.datetime_fromisoformat import MonkeyPatch
MonkeyPatch.patch_fromisoformat()
from collections import namedtuple, Counter
import csv

#Creating namedtuples
personal_info = namedtuple("personal_info", ["SSN", "First_Name", "Last_Name", "Gender", "Language"])
vehicles = namedtuple("vehicles", ["SSN", "Vehicle_Make", "Vehicle_Model", "Model_Year"])
employment = namedtuple("employment", ["Employer", "Department", "Employee_Id", "SSN"])
update_status = namedtuple("update_status", ["SSN", "Last_Updated", "Created"])

def read_file(file_name: "csv_file")->None:
    """
    This method reads the csv file with ',' delimiter
    Input: file_name - csv files to be read
    Return: None
    """
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=",", quotechar='"')
        yield from rows

def personal_info_generator():
    """
    This function is a Generator for personal_info named tuple, generates a named tuple for each row in the file
    input: None
    Return: None
    """
    data = read_file("personal_info.csv")
    next(data)
    for row in data:
        ssn = row[0]
        first_name = row[1]
        last_name = row[2]
        gender = row[3]
        language = row[4]
        yield personal_info(ssn, first_name, last_name, gender, language)

def vehicle_generator():
    """
    This function is a Generator for vehicle_generator named tuple, generates a named tuple for each row in the file 
    input: None
    Return: None
    """
    data = read_file("vehicles.csv")
    next(data)
    for row in data:
        ssn = row[0]
        vehicle_make = row[1]
        vehicle_model = row[2]
        model_year = int(row[3])
        yield vehicles(ssn, vehicle_make, vehicle_model, model_year)

def employment_generator():
    """
    This function is a Generator for employment_generator named tuple, generates a named tuple for each row in the file
    input: None
    Return: None
    """
    data = read_file("employment.csv")
    next(data)
    for row in data:
        employer = row[0]
        department = row[1]
        employee_id = row[2]
        ssn = row[3]
        yield employment(employer, department, employee_id, ssn)

def update_status_generator():
    """
    This function is a Generator for update_status_generator named tuple, generates a named tuple for each row in the file
    input: None
    Return: None
    """
    data = read_file("update_status.csv")
    next(data)
    for row in data:
        ssn = row[0]
        last_updated = datetime.strptime(
            datetime.fromisoformat(row[1].replace("Z", "+00:00")).strftime("%d/%m/%Y"),
            "%d/%m/%Y",
        )
        created = datetime.strptime(
            datetime.fromisoformat(row[2].replace("Z", "+00:00")).strftime("%d/%m/%Y"),
            "%d/%m/%Y",
        )
        yield update_status(ssn, last_updated, created)

def fetch_records(gen):
    """
    This function provides the list of rows from the generator
    input: gen - Generator object to be passed
    return: list of records extarcted from the generator
    """
    return [record for record in gen()]

# Goal 2 :create a single iterable that combines all the columns from all the iterators.
def merge_tuples(*ntuples):
    """
    This function merges the records from all the generators into a single list of named tuples,
    creates new named tuple by merging other named tuples with key "SSN"
    input: ntuples - all the namedtuples generated
    return: None
    """
    record_dict = {}
    for item in ntuples:
        record_dict.update(item._asdict())
    yield namedtuple("combined", record_dict.keys())(*record_dict.values())

def combined_generator(l1, l2, l3, l4):
    """
    This function is a Generator for combining the namedtuple, Generates the namedtuple for each row in the file ,
    combines all named tuple merged records
    input: l1, l2, l3, l4 - iterators
    return: None
    """
    for a, b, c, d in zip(l1, l2, l3, l4):
        yield from merge_tuples(a, b, c, d)

def combined_records():
    """
    This function combines all the generators to create a combined iterator and returns a list of records
    input: None
    return: combined_records - list of records read from individual csv's
    """
    personal_info_iterator = fetch_records(personal_info_generator)
    vehicle_iterator = fetch_records(vehicle_generator)
    employment_iterator = fetch_records(employment_generator)
    update_status_iterator = fetch_records(update_status_generator)

    combined_iter = combined_generator(
        personal_info_iterator,
        vehicle_iterator,
        employment_iterator,
        update_status_iterator,
    )

    # Creating a final records list
    combined_records = list(combined_iter)
    return combined_records

# Goal 3 :identify any stale records, where stale simply means the record has not been updated
# since 3/1/2017 (e.g. last update date < 3/1/2017)

def print_stale_records(combined_records):
    """
    This function filters the stale records and prints them. i.e. last update date < 3/1/2017
    input: combined_records - list of all the records
    return: stale_records - list of records whose last update date < 3/1/2017
    """
    format_date = datetime.strptime("03/01/2017", "%m/%d/%Y")
    stale_records = [x for x in filter(lambda x: x.Last_Updated < format_date, combined_records)]
    current_records = [
        x for x in filter(lambda x: x.Last_Updated > format_date, combined_records)
    ]

    print(f"Total number of stale records: {len(stale_records)}")
    print(f"Total number of current records: {len(current_records)}")

    return stale_records

# Goal 4 :Find the largest group of car makes for each gender
def vehicle_make_gender_information(records):
    """
    This function is a Generator for identifying Vehicle Make, Gender from given records
    input: records - records extracted from current data
    return: None
    """
    for record in records:
        yield record.Vehicle_Make, record.Gender

def vehicle_make_gender_generator(records):
    """
    This function is a Generator for Vehicle Make, Gender combinations
    input: records - records extracted from current data
    return: None
    """
    vehicle_make_list = [
        (vehicle_make, gender)
        for vehicle_make, gender in vehicle_make_gender_information(records)
    ]
    violation_by_vehicle_make = Counter(vehicle_make_list)
    for make_gender, Count in violation_by_vehicle_make.most_common():
        yield [make_gender, Count]

def show_top_count(records):
    """
    This function returns the Vehicle Make, gender combination count in list
    input: records - records extracted from current data
    return: top_count_list - list of top counts
    """
    top_count_list = list(vehicle_make_gender_generator(records))[0:5]
    return top_count_list