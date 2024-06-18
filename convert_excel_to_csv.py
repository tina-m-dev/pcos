# convert_excel_to_csv.py

import pandas as pd

# Load the Excel file
xlsx_file = 'pcos.xlsx'  # Replace with your XLSX file path
df = pd.read_excel(xlsx_file, sheet_name='Sheet1')  # Adjust sheet_name as needed

# Save as CSV (adjust file name if necessary)
csv_file = 'pcos_w_i.csv'
df.to_csv(csv_file, index=False)
