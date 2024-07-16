import pandas as pd
import glob

filepaths = glob.glob("/Users/airelking/Desktop/NewRising/Projects/Portfolio/PDF_Maker/Invoices_pdf/Invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name = "Sheet 1")
    print(df)