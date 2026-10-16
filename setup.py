
from setuptools import setup, find_packages

setup(
    name="my-advanced-lib",
    version="1.0.0",
    description="A reusable library demonstrating advanced Python concepts",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
)
