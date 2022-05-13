from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.output("./First_PDF.pdf", 'F')


