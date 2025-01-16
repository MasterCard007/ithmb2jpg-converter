from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ithmb2jpg-converter",
    version="0.0.12",
    author="Your Name",
    author_email="",
    description="A tool to convert .ithmb files into .jpg images",
    long_description=long_description,
    long_description_content_type="",
    url="https://github.com/MasterCard007/ithmb2jpg-converter",
    packages=find_packages(),
    py_modules=["ithmb_to_jpg_input"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "tqdm",
        "ithmbconverter"
    ],
    entry_points={
        'console_scripts': [
            'ithmb2jpg=ithmb_to_jpg_input:scan_and_convert_ithmb'
        ]
    },
)
