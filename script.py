from setuptools import setup, find_packages

def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="mobile",
    version="0.2.0",
    packages=find_packages(),
    install_requires=get_requirements(),
)