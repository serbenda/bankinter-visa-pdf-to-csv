# 📄💳 Bankinter VISA Statement Extractor 🚀📊

## 🌟 Description

**Bankinter VISA Statement Extractor** is a 🐍 Python tool designed to extract transaction data from **Bankinter VISA** card statements in PDF format 📄 and convert them into structured CSV files 📊. Perfect for Bankinter customers who want to analyze their transactions in tools like Excel, Power BI, or other financial software 💼.

---

## ✨ Features

✔️ **Tailored for Bankinter VISA Statements**: Extracts data with precision.  
✔️ **Dual Extraction Methods**: Handles both text-based PDFs 📝 and scanned PDFs with OCR 🖼️.  
✔️ **Outputs Structured CSVs**: Easy to analyze and compatible with financial tools.  
✔️ **Detailed Information Extracted**:  
   - 🗓️ Transaction Date  
   - 💳 Card Last 4 Digits  
   - 🏷️ Transaction Description  
   - 💸 Debit and Credit Amounts  

---

## ⚙️ Installation

### 🔧 Prerequisites

1. **Python 3.6+** 🐍  

2. **Tesseract OCR** for scanned PDFs 🖼️ (if needed):  
   - 🐧 On Linux (Ubuntu/Debian):  
     ```bash
     sudo apt install tesseract-ocr
     ```
   - 🪟 On Windows: Download from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).  

3. Install dependencies 📦:  

   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Installing the Project

Clone the repository 🛎️ and install the package:  

```bash
git clone https://github.com/serbenda/bankinter-visa-pdf-to-csv.git
cd bankinter-visa-pdf-to-csv
pip install .
```

---

## 🚀 Usage

Use the pdf-to-csv command to process your Bankinter VISA statements 📄➡️📊:

```bash
pdf-to-csv <path_to_pdf> <path_to_csv>
```

### Example 📝

Convert a Bankinter VISA statement named bank_statement.pdf into a CSV file called transactions.csv:

```bash
pdf-to-csv bank_statement.pdf transactions.csv
```

After running this command, the tool will extract all transaction data from the PDF and save it in the specified CSV file. The resulting CSV file can be opened in tools like Excel, Power BI, or other financial analysis software.

---

## 📊 CSV Output Example

Here’s how your CSV will look:

| 🗓️ Transaction Date | 💳 Card Number | 🏷️ Description                          | 💸 Debits (€) | 💰 Credits (€) |
|---------------------|---------------|------------------------------------------|--------------|---------------|
| 31/10/2024          | 1533          | SUMUP, SESENA                            | 15.00        |               |
| 01/11/2024          | 1533          | ALGACA, S.L., SAN SEBASTIAN              | 4.11         |               |
| 02/11/2024          | 1533          | PAYPAL *MAKSU 32040525, 35314369001      | 2.07         |               |
| 02/11/2024          | 1533          | AWS EMEA, aws.amazon.co                  | 5.89         |               |
| 02/11/2024          | 1533          | BM SAN SEBASTIAN DE LOS R, 28703         |              | 31.23         |

---

✅ Testing
Run tests 🧪 to ensure everything works as expected:

```bash
pip install pytest
pytest -s
```

---

## 🤝 Contributing
We welcome contributions! 🎉 If you'd like to help, follow these steps:

1. 🍴 Fork the repository.
2. 🌱 Create a new branch:

```bash
git checkout -b new-feature
```

3. 🛠️ Make your changes and push them:

```bash
git commit -m "Add a new feature"
git push origin new-feature
```

4. 🔄 Open a pull request and explain your changes.

---

## 🛡️ License
This project is licensed under the MIT License 📜. Feel free to use, modify, and share it! Check the LICENSE file for more details.

---

## 💡 Need Help?
If you have any questions or encounter issues 🐛, feel free to open an issue or reach out!