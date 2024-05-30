from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Implements the foo function'
LONG_DESCRIPTION = 'Implements the foo function, finding the volume of a 3 dimensional sphere from its radius'

setup(
        name="SphereRadiusPython", 
        version=VERSION,
        author="David Calgan",
        author_email="<davidpcalgan96@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'foo', 'sphere'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
