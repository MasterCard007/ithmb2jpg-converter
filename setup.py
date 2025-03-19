from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ithmb2jpg-converter",
    version="0.0.14",  # Removed the need of ithmbconverter
    author="MasterCard007",
    author_email="",
    description="A tool to extract and convert .ithmb files into .jpg images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MasterCard007/ithmb2jpg-converter",
    packages=find_packages(),
    py_modules=["ithmb_converter"],  # Updated to match the new script name
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "tqdm",
        "opencv-python",  # Replacing ithmbconverter with OpenCV, which we actually use
        "icecream"
    ],
    entry_points={
        'console_scripts': [
            'ithmb2jpg=ithmb_converter:scan_and_convert_ithmb'
        ]
    },
)
