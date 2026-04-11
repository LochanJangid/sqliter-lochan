from setuptools import setup, find_packages

setup(
    name="sqliter",
    version="0.1.0",
    author="Lochan Jangid",
    author_email="lochanjangidcoder@gmail.com",
    description="A simple, clean SQLite database wrapper for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sqliter",
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
