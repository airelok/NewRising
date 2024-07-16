import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

#   find the filepath for the invoice documents
filepaths = glob.glob("/Users/airelking/Desktop/NewRising/Projects/Portfolio/PDF_Maker/Invoices_pdf/Invoices/Excels/*.xlsx")
for filepath in filepaths:
    print(f"\nThis is the filepath for {filepath.split("/")[-1]}:" + "\n" + filepath +"\n")

#   create a data frame for each excel file
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name = "Sheet 1")

    #   Extract the file name
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]

    print(f"The data frame for {invoice_nr} invoice statement:\n" , df , "\n")
    pdf = FPDF(orientation = "P", unit = "mm", format="A4")
    pdf.add_page()

    #   set the header
    pdf.set_font(family = "Times", size = 24, style = "B")
    pdf.cell(w = 50,  h = 8, txt = f"Invoice nr. {invoice_nr}", ln = 1)

    #   set the subheader
    invoice_date = filename.split("-")[1]
    pdf.set_font(family = "Times", size = 18, style = "B")
    pdf.cell(w = 50, h = 8, txt = f"Invoice Date: {invoice_date}", ln = 2)


    #   generate the pdf file and name it as follows
    pdf_output = pdf.output(f"Invoices/PDFs/{filename}.pdf")





