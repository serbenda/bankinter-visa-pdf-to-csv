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

Use the bankinter-visa-extractor command to process your Bankinter VISA statements 📄➡️📊:

```bash
bankinter-visa-extractor <path_to_pdf> <path_to_csv>
```

### Example 📝

Convert a Bankinter VISA statement named bank_statement.pdf into a CSV file called transactions.csv:

```bash
bankinter-visa-extractor bank_statement.pdf transactions.csv
```

After running this command, the tool will extract all transaction data from the PDF and save it in the specified CSV file. The resulting CSV file can be opened in tools like Excel, Power BI, or other financial analysis software.

---

## 📊 CSV Output Example

Here’s how your CSV will look:

| 🗓️ Transaction Date | 💳 Card Number | 🏷️ Description                          | 💸 Debits (€) | 💰 Credits (€) |
|---------------------|---------------|------------------------------------------|--------------|---------------|
| 31/10/2024          | 1533          | SUMUP, SESENA                            | 15.00        |               |
| 01/11/2024          | 1533          | ALGACA, S.L., SAN SEBASTIAN              | 4.11         |               |
| 02/11/2024          | 1533          | PAYPAL *MAKSU XXXXXXXX, XXXXXXXXXXX      | 2.07         |               |
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

### 📥 Downloading the PDF from Bankinter

To use this tool, you first need to download your VISA statement in PDF format from the Bankinter online banking portal. Follow these steps:

1. **Log in to Bankinter Online Banking**:
   - Open your browser and go to [Bankinter Online Banking](https://www.bankinter.com).
   - Enter your credentials to log in.

2. **Navigate to the VISA Section**:
   - Once logged in, go to the section for your **VISA card statements**.
   - You can find this under the "Cards" or "VISA" menu, depending on your account setup.

3. **Select the Statement Period**:
   - Choose the specific period for which you want to download the statement (e.g., "November 2024").
   - Ensure the period matches the one you want to process.

4. **Download the PDF**:
   - Click on the option to download the statement as a PDF file.
   - Save the file locally on your computer in an easily accessible location.

5. **Verify the PDF**:
   - Ensure the file is in PDF format and contains the transaction details.
   - Avoid renaming the file to something generic like `document.pdf`. Use descriptive names like `bankinter_statement_nov_2024.pdf`.

6. **Ready to Process**:
   - Use the downloaded PDF with this tool by running the command:
     ```bash
     bankinter-visa-extractor <path_to_pdf> <path_to_csv>
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
This project is licensed under the MIT License 📜. Feel free to use, modify, and share it! Check the [MIT License](https://opensource.org/licenses/MIT)
file for more details.

---

## 💡 Need Help?
If you have any questions or encounter issues 🐛, feel free to open an issue or reach out!