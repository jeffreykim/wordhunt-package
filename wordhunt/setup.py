from setuptools import setup, find_packages

setup(
    name="wordhunt_bot",
    version="0.1.4",
    author="Jeffrey Kim",
    author_email="jkjeffrey7@gmail.com",
    description="This script will take a string and output possible words in Wordhunt.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jeffreykim/wordhunt-bot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "wordhunt=wordhunt_package.solver:run",
        ],
    },
)