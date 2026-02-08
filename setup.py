from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Clean up newline characters
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if present to prevent recursive loops
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='CUSTOMER-SEGMENTATION',
    version='0.0.1',
    author='AbhinavKhajurgi',
    author_email='abhinav.khajurgi23@spit.ac.in',
    packages=find_packages(),
    # FIXED THE TYPO BELOW
    install_requires=get_requirements('requirements.txt')
)