from setuptools import setup, find_packages
import io
import os


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="csvs_to_sqlite",
    description="Convert CSV files into a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    version="0.9",
    license="Apache License, Version 2.0",
    packages=find_packages(),
    install_requires=[
        "click>=6.0.0",
        "dateparser>=0.7.0",
        "pandas>=0.23.4",
        "py-lru-cache==0.1.4",
        "six",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest>=4.1.1"],
    entry_points="""
        [console_scripts]
        csvs-to-sqlite=csvs_to_sqlite.cli:cli
    """,
    url="https://github.com/simonw/csvs-to-sqlite",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Database",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ],
)
