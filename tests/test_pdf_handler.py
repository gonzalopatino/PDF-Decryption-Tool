import unittest
from pdf_decryption_tool.pdf_handler import decrypt_pdf_pikepdf
import os

class TestPDFHandler(unittest.TestCase):
    def test_decrypt_pdf_with_correct_password(self):
        input_file = r'C:\Users\coleg\PycharmProjects\PdfEncryptRemover\encrypted_test.pdf'
        output_file = r'C:\Users\coleg\PycharmProjects\PdfEncryptRemover\unencrypted_test.pdf'
        password = "BnqRh2j9"
        result = decrypt_pdf_pikepdf(input_file, password, output_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_file))

    def test_decrypt_pdf_with_incorrect_password(self):
        input_file = r'C:\Users\coleg\PycharmProjects\PdfEncryptRemover\encrypted_test.pdf'
        output_file = r'C:\Users\coleg\PycharmProjects\PdfEncryptRemover\unencrypted_test.pdf'
        password = "incorrect_password"
        result = decrypt_pdf_pikepdf(input_file, password, output_file)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
