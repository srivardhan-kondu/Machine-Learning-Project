from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Return all the packages in requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove leading/trailing spaces/newlines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Srivardhan',
    author_email='Srivardhan.kondu@gmail.com',
    description='A machine learning package for various ML products',
    long_description=open('README.md').read(),  # Optional, if you have a README.md file
    long_description_content_type='text/markdown',  # Optional, if you have a README.md file
    url='https://github.com/yourusername/mlproject',  # Optional, replace with your project URL
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Ensure 'requirements.txt' is spelled correctly
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python versions supported
)
