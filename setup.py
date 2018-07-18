from setuptools import setup, find_packages


with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="python-cli-example",
    version="0.0.1",
    description="A small example package",
    url="https://github.com/karakaram/python-cli-example",
    author="karakaram",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "myapp=myapp.main:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
