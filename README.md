# PDF Decryption Tool

A simple Python application that decrypts password-protected PDF files using `pikepdf` and provides a user-friendly interface via Tkinter.

**Developer**: Gonzalo Patino
## Features
- Decrypts password-protected PDFs using the `pikepdf` library.
- User-friendly graphical interface built with Tkinter.
- Allows the user to save the decrypted PDF in the desired location.

## Prerequisites
- Python 3.x
- Required Python packages:
  - `pikepdf`
  - `tkinter`
## Setup Instructions

### Using the Executable

To use the pre-built executable, no installation is required. Simply follow the steps below:

1. Download the `main.exe` file from the `dist/` folder.
2. Double-click the executable to launch the application.
3. Select a password-protected PDF, enter the password, and decrypt it.

### Running from Source

Alternatively, if you prefer to run from the source, follow these instructions:

## Setup Instructions

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/yourusername/pdf-decryption-tool.git
   cd pdf-decryption-tool
### Step 2: Install Dependencies

Install the necessary Python dependencies by running:
```bash
pip install pikepdf
```
Note: Tkinter is pre-installed with Python on most platforms, so you usually don’t need to install it separately.

---
### Step 3: Run the application:
To launch the graphical interface, run the following command:
```bash
python main.py
```
---
### Usage

- **Launch the application**: After running `main.py`, a window will appear allowing you to select a password-protected PDF file.
- **Enter the correct password**: Input the password required to unlock the PDF.
- **Save the decrypted PDF**: Once the PDF is decrypted, save it to your preferred location.
---
### Running the Unit Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover tests/
```
### Example Output of Tests

If the tests pass successfully, you should see output similar to this:

```plaintext
Ran 2 tests in 0.001s

OK
```
---
### Project Structure

```plaintext
PdfEncryptRemover/
│   encrypted_test.pdf         # Test PDF file (password-protected)
│   main.py                    # Main entry point of the application
│   README.md                  # Documentation file (this file)
│   uncrypted_PDF_output.pdf   # Output file after decryption
│
├───pdf_decryption_tool        # Core package containing the decryption logic and GUI
│   │   __init__.py
│   │   constants.py           # Contains user feedback messages (success/error)
│   │   gui.py                 # Tkinter GUI logic
│   │   pdf_handler.py         # PDF decryption logic using pikepdf
│
├───tests                      # Unit tests to ensure the functionality works correctly
│   │   __init__.py
│   │   test_pdf_handler.py    # Tests for PDF decryption functionality
│
└───assets (optional)          # Optional folder for storing images/icons if needed

```
---
### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---



