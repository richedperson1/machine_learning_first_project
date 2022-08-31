from setuptools import setup
from typing import *

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirement_list()->List[str]:
    """
    Description : 
    This function is going to return list of requirement mention in requirement.txt file

    return : list of require file 
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


PROJECT_NAME = "housing-predictor"
# VERSION = "0.0.1"
AUTHOR = "Rutvik"
descripition = "This my first"
# NAME = 
setup(name = PROJECT_NAME,author=AUTHOR,packages=["housing"],install_requires = get_requirement_list())
print(get_requirement_list())