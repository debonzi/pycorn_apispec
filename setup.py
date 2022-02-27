from io import open
from os import path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pycorn_apispec",
    version="0.1",
    description="Automated APISpec documentation with Pyramid Cornice and Marshmallow ",
    long_description=long_description,
    license="BSD",
    long_description_content_type="text/markdown",
    url="https://github.com/debonzi/pycorn_apispec",
    author="Daniel Debonzi",
    author_email="debonzi@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="pyramid apispec marshmallow cornice rest restful",
    packages=find_packages(
        exclude=[
            "tests",
        ]
    ),
    package_data={},
    install_requires=[
        "pyramid-apispec>=0.4",
        "cornice>=6.0.0",
        "marshmallow>=3.13.0,<4.0.0",
        "marshmallow-oneofschema>=3.0.1,<4.0.0",
    ],
    setup_requires=[],
    extras_require={
        "dev": ["pytest", "webtest", "black"],
        "demo": ["marshmallow>=3.13.0,<4.0.0", "apispec>=5.1.0,<6.0.0"],
    },
)
