import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pdf_decryption_tool.pdf_handler import decrypt_pdf_pikepdf
from pdf_decryption_tool.constants import SUCCESS_MSG, ERROR_MSG

class PDFDecryptionApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PDF Decryption Tool")
        self.window.geometry("400x200")
        self.selected_file = None

        # Title Label
        self.label = tk.Label(self.window, text="Select a password-protected PDF")
        self.label.pack(pady=10)

        # File selection button
        self.select_button = tk.Button(self.window, text="Select PDF", command=self.select_pdf)
        self.select_button.pack(pady=5)

        # Password entry
        self.password_label = tk.Label(self.window, text="Enter password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack(pady=5)

        # Decrypt button
        self.decrypt_button = tk.Button(self.window, text="Decrypt PDF", command=self.decrypt_pdf)
        self.decrypt_button.pack(pady=5)

        # Status label
        self.status_label = tk.Label(self.window, text="")
        self.status_label.pack(pady=10)

    def select_pdf(self):
        self.selected_file = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Select a PDF File"
        )
        if self.selected_file:
            self.label.config(text=os.path.basename(self.selected_file))

    def decrypt_pdf(self):
        password = self.password_entry.get()

        if not self.selected_file:
            messagebox.showerror("Error", ERROR_MSG['no_file'])
            return

        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save Decrypted PDF"
        )

        if output_file and decrypt_pdf_pikepdf(self.selected_file, password, output_file):
            messagebox.showinfo("Success", SUCCESS_MSG['decryption_successful'])
        else:
            messagebox.showerror("Error", ERROR_MSG['invalid_password'])

    def run(self):
        self.window.mainloop()
