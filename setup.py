from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
        """
        This function return list of requirements 
        """
        requirement_lst:List[str]=[]
        try:
                with open('requirements.txt','r') as file:
                        # Read lines from the line
                        lines=file.readlines()
                        ## Process Each line
                        for line in lines:
                                requirement=line.strip()
                                ## remove line and -e .
                                if requirement and requirement!='-e .':
                                        requirement_lst.append(requirement)
        except FileNotFoundError:
                print("requirements.txt file not found")
        return requirement_lst
# print(get_requirements())

# Set meta data

setup(
        name='NetworkSecurity',
        version='0.0.1',
        author='Vidyanshu Kushawaha',
        author_email='vidyanshukushawaha@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements()
)