from setuptools import find_packages, setup
from typing import List 

hyphen_in_reqtxt='-e .'
def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open('requirements.txt', 'r') as f:
        requirements=f.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if hyphen_in_reqtxt in requirements:
            requirements.remove(hyphen_in_reqtxt)
        
    return requirements
        


setup(
name='mlproject',
version='0.0.1',
author='Arjun',
author_email='arjunverma098@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
)