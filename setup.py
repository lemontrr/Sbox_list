from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Sbox_list",
    version="0.0.1",
    author="YJ",
    author_email="idealtop18@kookmin.ac.kr",
    description="Sbox list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lemontrr/Sbox_list",
    project_urls={
        "Bug Tracker": "https://github.com/lemontrr/Sbox_list",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
