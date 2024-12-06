"""
PDF to CSV Extractor for Bankinter VISA Statements.

This module provides functions to extract transaction data from Bankinter VISA 
statements in PDF format and convert them into structured CSV files. It handles 
both text-based PDFs and scanned PDFs using OCR.

Author: Sergio Santiago Bendaña Quesada
Date: 2024-12-6
"""

import fitz  # PyMuPDF for PDF text extraction
import pytesseract  # OCR library for scanned PDFs
from pdf2image import convert_from_path  # Convert PDF pages to images
import csv  # For saving data in CSV format
import re  # Regular expressions for text parsing
from PIL import Image  # For image processing
import argparse  # For command-line argument parsing


def extract_text_from_pdf_pymupdf(pdf_path):
    """
    Extract text from a PDF file using PyMuPDF.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file.
    """
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def extract_text_from_pdf_ocr(pdf_path):
    """
    Extract text from a scanned PDF file using OCR.

    Args:
        pdf_path (str): The path to the scanned PDF file.

    Returns:
        str: The extracted text from the scanned PDF file.
    """
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text


def process_text_to_data(text):
    """
    Process the extracted text to extract transaction data.

    Args:
        text (str): The extracted text from the PDF.

    Returns:
        list[dict]: A list of dictionaries containing transaction data.
    """
    data = []
    # Regular expression to extract transaction details
    pattern = (
        r"(\d{2}/\d{2}/\d{4})\s+(\d{4})\s+(.+?)\s+"
        r"(\d+,\d{2}|)\s+(\d+,\d{2}|)"
    )
    matches = re.findall(pattern, text)

    for match in matches:
        fecha, tarjeta, concepto, cargos, abonos = match
        data.append({
            "Transaction Date": fecha,
            "Card Number": tarjeta,
            "Description": concepto.strip(),
            "Debits (€)": cargos.replace(',', '.') if cargos else "",
            "Credits (€)": abonos.replace(',', '.') if abonos else "",
        })
    return data


def save_data_to_csv(data, csv_path):
    """
    Save the extracted transaction data into a CSV file.

    Args:
        data (list[dict]): The transaction data to save.
        csv_path (str): The path where the CSV file will be saved.

    Returns:
        None
    """
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            "Transaction Date",
            "Card Number",
            "Description",
            "Debits (€)",
            "Credits (€)"
        ])
        writer.writeheader()
        writer.writerows(data)


def convert_pdf_to_csv(pdf_path, csv_path):
    """
    Convert a Bankinter VISA statement from PDF to CSV.

    This function attempts to extract text using PyMuPDF. If PyMuPDF fails, it
    falls back to OCR for scanned PDFs. The extracted data is then processed
    and saved as a CSV file.

    Args:
        pdf_path (str): The path to the PDF file.
        csv_path (str): The path to save the CSV file.

    Returns:
        None
    """
    print("Processing Bankinter VISA statement...")

    # Attempt to extract text using PyMuPDF
    text = extract_text_from_pdf_pymupdf(pdf_path)

    # If PyMuPDF fails, attempt OCR
    if not text.strip():
        print("No text found with PyMuPDF. Falling back to OCR...")
        text = extract_text_from_pdf_ocr(pdf_path)

    # Process and save the data
    if text.strip():
        data = process_text_to_data(text)
        if data:
            save_data_to_csv(data, csv_path)
            print(f"Data successfully extracted and saved to {csv_path}")
        else:
            print("No transactions found in the extracted text.")
    else:
        print("Failed to extract text from the PDF.")


def main():
    """
    Entry point for the CLI command `bankinter_visa_extractor`.
    Parses command-line arguments and invokes `convert_pdf_to_csv`.
    """
    parser = argparse.ArgumentParser(
        description="Extract transaction data from a Bankinter VISA statement PDF and save it as a CSV file."
    )
    parser.add_argument(
        "pdf_path", type=str, help="The path to the Bankinter VISA statement PDF file."
    )
    parser.add_argument(
        "csv_path", type=str, help="The path to save the resulting CSV file."
    )
    args = parser.parse_args()

    # Pass parsed arguments to `convert_pdf_to_csv`
    convert_pdf_to_csv(args.pdf_path, args.csv_path)


if __name__ == "__main__":
    main()
