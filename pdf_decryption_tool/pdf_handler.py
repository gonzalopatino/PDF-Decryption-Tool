import pikepdf

def decrypt_pdf_pikepdf(input_pdf_path, password, output_pdf_path):
    """
    Decrypts a password-protected PDF using pikepdf.

    Args:
        input_pdf_path (str): Path to the input PDF.
        password (str): Password to unlock the PDF.
        output_pdf_path (str): Path where the decrypted PDF will be saved.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Open the encrypted PDF with the password
        with pikepdf.open(input_pdf_path, password=password) as pdf:
            # Save the decrypted PDF to the output path
            pdf.save(output_pdf_path)
        return True
    except pikepdf.PasswordError:  # Correct exception for invalid password
        print("Incorrect password.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
