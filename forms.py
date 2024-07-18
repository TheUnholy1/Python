import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import fitz  # PyMuPDF

class PDFViewerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Viewer")

        self.pdf_document = None
        self.current_page = 0

        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        self.btn_open = tk.Button(self, text="Open PDF", command=self.open_pdf)
        self.btn_open.pack()

        self.btn_prev = tk.Button(self, text="Previous Page", command=self.prev_page)
        self.btn_prev.pack(side=tk.LEFT)

        self.btn_next = tk.Button(self, text="Next Page", command=self.next_page)
        self.btn_next.pack(side=tk.RIGHT)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_document = fitz.open(file_path)
            self.current_page = 0
            self.show_page()

    def show_page(self):
        if self.pdf_document:
            page = self.pdf_document.load_page(self.current_page)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            self.imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imgtk)
            self.title(f"PDF Viewer - Page {self.current_page + 1}")

    def prev_page(self):
        if self.pdf_document and self.current_page > 0:
            self.current_page -= 1
            self.show_page()

    def next_page(self):
        if self.pdf_document and self.current_page < len(self.pdf_document) - 1:
            self.current_page += 1
            self.show_page()

if __name__ == "__main__":
    app = PDFViewerApp()
    app.mainloop()
    
    
# tpye pygubu-designer to design efficiently
