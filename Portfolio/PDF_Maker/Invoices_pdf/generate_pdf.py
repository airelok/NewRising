import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("/Users/airelking/Desktop/NewRising/Projects/Portfolio/PDF_Maker/Invoices_pdf/Invoices/*.xlsx")
for filepath in filepaths:
    print(f"\nThis is the filepath for {filepath.split("/")[-1]}:" + "\n" + filepath +"\n")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name = "Sheet 1")

    # Extract the file name
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]

    print(f"The data frame for {invoice_nr} invoice statement:\n" , df , "\n")
    pdf = FPDF(orientation = "P", unit = "mm", format="A4")
    pdf.add_page()

    # set the header
    pdf.set_font(family = "Times", size = 16, style = "B")
    pdf.cell(w=50,  h=8, txt = f"Invoice nr. {invoice_nr}")

    #generate the pdf file and name it as follows
    pdf_output = pdf.output(f"Invoices/{filename}.pdf")




