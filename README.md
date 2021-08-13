# EPAi3-Session14

## Context Managers

### Question - 1

#### Objective: For this project you have 4 files containing information about persons.

~~~
The files are:
* `personal_info.csv` -   personal information such as name, gender, etc. (one row per person)
* `vehicles.csv` -   what vehicle people own (one row per person)
* `employment.csv` -   where a person is employed (one row per person)
* `update_status.csv` -   when the person's data was created and last updated

Each file contains a key, `SSN`, which **uniquely** identifies a person.This key is present in **all** four files.
You are guaranteed that the same SSN value is present in **every** file, and that it only appears **once per file**. In addition, the files are all sorted by SSN, i.e. the SSN values appear in the same order in each file.

Goal 1

Your first task is to create iterators for each of the four files that contained cleaned up data, of the correct type (e.g. string, int, date, etc), and represented by a named tuple. For now these four iterators are just separate, independent iterators.

Goal 2

Create a single iterable that combines all the columns from all the iterators. The iterable should yield named tuples containing all the columns. Make sure that the SSN's across the files match! All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file. Make sure the SSN is not repeated 4 times - one time per row is enough!

Goal 3

Next, you want to identify any stale records, where stale simply means the record has not been updated since 3/1/2017 (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale) based on the `last_updated` field from the `status_update` file.

Goal 4

Find the largest group of car makes for each gender. Possibly more than one such group per gender exists (equal sizes).
~~~

##### Functions
----------------

* __read_file()__
    - This method reads the csv file with ',' delimiter
    - Input: file_name - csv files to be read
    - Return: None

* __personal_info_generator()__
    - This function is a Generator for personal_info named tuple, generates a named tuple for each row in the file
    - input: None
    - return: None

* __vehicle_generator()__
    - This function is a Generator for vehicle_generator named tuple, generates a named tuple for each row in the file 
    - input: None
    - return: None

* __employment_generator()__
    - This function is a Generator for employment_generator named tuple, generates a named tuple for each row in the file
    - input: None
    - return: None

* __update_status_generator()__
    - This function is a Generator for update_status_generator named tuple, generates a named tuple for each row in the file
    - input: None
    - return: None

* __fetch_records()__
    - This function provides the list of rows from the generator
    - input: gen - Generator object to be passed
    - return: list of records extarcted from the generator

* __merge_tuples()__
    - This function merges the records from all the generators into a single list of named tuples,
    creates new named tuple by merging other named tuples with key "SSN"
    - input: ntuples - all the namedtuples generated
    - return: None

* __combined_generator()__
    - This function is a Generator for combining the namedtuple, Generates the namedtuple for each row in the file ,
    combines all named tuple merged records
    - input: l1, l2, l3, l4 - iterators
    - return: None

* __combined_records()__
    - This function combines all the generators to create a combined iterator and returns a list of records
    - input: None
    - return: combined_records - list of records read from individual csv's

* __print_stale_records()__
    - This function filters the stale records and prints them. i.e. last update date < 3/1/2017
    - input: combined_records - list of all the records
    - return: stale_records - list of records whose last update date < 3/1/2017

* __vehicle_make_gender_information()__
    - This function is a Generator for identifying Vehicle Make, Gender from given records
    - input: records - records extracted from current data
    - return: None

* __vehicle_make_gender_generator()__
    - This function is a Generator for Vehicle Make, Gender combinations
    - input: records - records extracted from current data
    - return: None

* __show_top_count()__
    - This function returns the Vehicle Make, gender combination count in list
    - input: records - records extracted from current data
    - return: top_count_list - list of top counts

__________________________________________________________________________________________________________________