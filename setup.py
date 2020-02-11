import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libs3",
    version="1.0",
    author="Pankaj Rawat",
    author_email="pankajr141@gmail.com",
    description="This is python implementation for for interacting with s3, with familier syntax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pankajr141/libs3",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
          'boto3',
    ],
)
