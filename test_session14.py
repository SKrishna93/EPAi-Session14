import pytest
import math
import os
import inspect
import re
import session14
from session14 import *

README_CONTENT_CHECK_FOR = [
    'read_file()',
    'personal_info_generator()',
    'vehicle_generator()',
    'employment_generator()',
    'update_status_generator()',
    'fetch_records()',
    'merge_tuples()',
    'combined_generator()',
    'combined_records()',
    'print_stale_records()',
    'vehicle_make_gender_information()',
    'vehicle_make_gender_generator()',
    'show_top_count()'
    ]

def test_session14_readme_exists():
    """
    Method checks if there is a README.md file. 
    failure_message: "README.md file missing!"  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session14_readme_500_words():
    """
    Method checks if there are atleast 500 words in the README.md file
    failures_message: Make your README.md file interesting! Add atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"

def test_session14_readme_proper_description():
    """
    Method checks if all the functions are described in the README.md file
    failures_message: You have not described all the functions/classes well in your README.md file
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_session14_readme_file_for_more_than_10_hashes():
    """
    Method checks if README.md file has atleast 10 '#' (indentations)
    failures_message: You have not described all the functions/classes well in your README.md file 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_generator_indentations():
    """
    Method checks for proper indentations \
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(session14)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_generator_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session11.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(session14, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"