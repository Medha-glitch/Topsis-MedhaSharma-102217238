
from setuptools import setup, find_packages

setup(
    name='Topsis-YourName-YourRollNumber',  # Modify this with your name and roll number
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'topsis-cli=cli:main',  # This will allow you to run cli.py using "topsis-cli"
        ]
    },
)
