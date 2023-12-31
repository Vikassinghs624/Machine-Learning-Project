
from setuptools import setup,find_packages
from typing import List
# Declaring the variable for setup functions

PROJECT_NAME='housing-predictor'
VERSION='0.0.1'
AUTHOR='Vikas Singh Sikarwar'
DESCRIPTION='This is my First Machine Learning Project'
PACKAGE=["Housing"]
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    '''
    Description: This function is going to return list of requirement mention in the requirements.txt file.

    Return : this function will return a list which contains name of libraries mentioned in requirements.txt file
    
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
 

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)


if __name__=="__main__":
    print(get_requirements_list())