import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

#   find the filepath for the excel formatted invoice documents
filepaths = glob.glob("/Users/airelking/Desktop/NewRising/Projects/Portfolio/PDF_Maker/Invoices_pdf/Invoices/Excels/*.xlsx")
for filepath in filepaths:

    #   Extract the file name
    filename = Path(filepath).stem.split("/")[-1]
    print(f"\n This is the filepath for {filename}: \n {filepath} \n")

    #   Initialize the pdf document (create it)
    pdf = FPDF(orientation = "P", unit = "mm", format="A4")
    pdf.add_page()

    #   Set the header
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family = "Times", size = 24, style = "B")
    pdf.cell(w = 50,  h = 8, txt = f"Invoice nr. {invoice_nr}", ln = 1)

    #   Set the subheader
    invoice_date = filename.split("-")[1]
    pdf.set_font(family = "Times", size = 18, style = "B")
    pdf.cell(w = 50, h = 8, txt = f"Invoice Date: {invoice_date}", ln = 2)

    #   add the invoice data in a table format
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=50, h=8, txt="Invoice Transaction Data", ln=2)

    #   Create a dataframe for each excel file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(f"The data frame ---> \n {df}")

    #   Store the table headers in an iterable
    columns = list(df.columns)

    #   Reformat header for each colum
    header_cols = [item.replace("_"," ").title() for item in columns]
    pdf.cell(w = 30, h = 8, txt = header_cols[0], border = 1)
    pdf.cell(w = 70, h = 8, txt = header_cols[1], border = 1)
    pdf.cell(w = 30, h = 8, txt = header_cols[2], border = 1)
    pdf.cell(w = 30, h = 8, txt = header_cols[3], border = 1)
    pdf.cell(w = 30, h = 8, txt = header_cols[4], border = 1, ln = 1)
    print(f"This is the header: \n \n {header_cols} \n")

    #   Add the rows (values) to the table
    for index, row in df.iterrows():
        pdf.set_font(family = "Times", size = 9, style = "B")
        pdf.set_text_color(80, 80, 80)

        #   Moving through each colum add the column name & the required format style
        pdf.cell(w = 30, h = 8, txt = str(row["product_id"]), border = 1)
        pdf.cell(w = 70, h = 8, txt = str(row["product_name"]), border = 1)
        pdf.cell(w = 30, h = 8, txt = str(row["amount_purchased"]), border = 1)
        pdf.cell(w = 30, h = 8, txt = str(row["price_per_unit"]), border = 1)
        pdf.cell(w = 30, h = 8, txt = str(row["total_price"]), border = 1)

        pdf.ln()

#   generate the pdf file and name it as follows
pdf_output = pdf.output(f"Invoices/PDFs/{filename}.pdf")





