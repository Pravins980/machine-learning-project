from setuptools import setup
from typing import List

def get requirements_list()->List[str]:
              with open("REQUIERMENT_FILE_NAME")as requirements_file:
                            return requirements_file.readline()

PROJECT_NAME="Housing=prediction"
VERSION="0.0.1"
AUTHOR="Pravin Sharma"
DESCRIPTION="This is first FSDS bactvh project"
PACKAGE=["Housing"]



setup (
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR
description=DESCRIPTION,
packaages=PACKAGE,
install_requires=get_requirements_list()
)

if __name__=="__main__":
              print(get_requierments_list())