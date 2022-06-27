from setuptools import setup,find_packages
from typing import List


 

## Declaring Variables for setup functions ##        
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Avnish Yadav"
DESCRIPTION="This is a first FSDS Nov batch Learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file
    return this function is going to return a list whcih
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name="housing-predictor",
version="0.0.1",
author="avinash",
description=DESCRIPTION,
##packages=PACKAGES,
packages=find_packages(),
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())