from setuptools import setup,find_packages
from typing import List
 


PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Avnish Yadav"
DESCRIPTION="This is a first FSDS Nov batch Learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
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

