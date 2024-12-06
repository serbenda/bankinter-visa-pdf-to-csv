from setuptools import setup, find_packages

setup(
    name="bankinter-visa-statement-extractor",
    version="1.0.0",
    description="A tool to extract and convert Bankinter VISA statements from PDF to CSV.",
    author="Sergio Santiago Bendaña Quesada",
    author_email="serbenda@gmail.com",
    url="https://github.com/serbenda/bankinter-visa-statement-extractor",
    packages=find_packages(),
    install_requires=[
        "PyMuPDF",
        "pytesseract",
        "pdf2image",
        "Pillow",
    ],
    entry_points={
        "console_scripts": [
            "bankinter-visa-extractor=bankinter_visa_extractor.extractor:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)