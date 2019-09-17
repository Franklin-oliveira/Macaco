import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="macaco",
    version="1.0",
    author="Franklin Oliveira - Felipe Costa",
    description="A simple dataframe for Python, compiled in C++.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Franklin-oliveira/Macaco",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
