from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List(str):
    '''
    this funtion will require the list of requirements
    '''
    requirments = []
    with open('requirments.txt') as file_obj:
        requirments = file_obj.readline()
        requirments[req.replace("\n","") for req in requirments]

    if HYPHEN_E_DOT in requirments:
        requirments.remove(HYPHEN_E_DOT)
    
    return requirments

setup(
    name='mlproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Adeel Farooq Khan',
    author_email='adeelfarooq417@gmail.com',
)