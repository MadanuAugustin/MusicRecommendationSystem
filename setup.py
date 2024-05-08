

from setuptools import find_packages, setup

from typing import List

hypen_e = '-e .'

def requirements_function(requirements_file) -> List:
    requirements = []
    with open(requirements_file) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]

        if hypen_e in requirements:
            requirements.remove(hypen_e)

    return requirements



setup(
    name = 'MusicRecommendationSystem',
    version= '0.0.0.0',
    author='augustin',
    author_email='augustin7766@gmail.com',
    packages = find_packages(),
    install_requires = requirements_function('requirements.txt')
    )