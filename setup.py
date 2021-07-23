import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HPrice",
    version="0.0.1",
    author="MrHBogart",
    description="A package to convert simple OHLC candlestick data to HPrice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrHbogart/HPrice",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)