"""
gitrecon
"""
from gettext import install
from importlib.metadata import entry_points
from setuptools import setup, find_packages


setup(
    name="gitrecon",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "gitrecon=gitrecon.gitrecon:main",
        ],
    },
    author="zackey-heuristics",
    description="gitrecon",
    url="https://github.com/zackey-heuristics/gitrecon"
)
