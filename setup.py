from setuptools import setup,find_packages #Automatically find all packages in your project
from typing import List

AUTHOR_NAME = 'Arjun Singh'
AUTHOR_EMAIL = 'shekhawatsingharjun12345@gmail.com'
DESCRIPTION = 'Resume Analyzer'
VERSION = '0.0.1'
NAME = 'Resume Analyzer'
HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name=NAME,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    version=VERSION,
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)


