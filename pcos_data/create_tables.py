import pandas as pd
import glob

# Path to CSV and Excel files directory
files_path = './'

# Function to process CSV files
def process_csv_files():
    csv_files = glob.glob(files_path + '*.csv')
    for file in csv_files:
        df = pd.read_csv(file)
        # Process data as needed
        print(f'Processing {file}')
        print(df.head())

# Function to process Excel files
def process_excel_files():
    excel_files = glob.glob(files_path + '*.xlsx')
    for file in excel_files:
        df = pd.read_excel(file, sheet_name='Sheet1')  # Adjust sheet_name as needed
        # Process data as needed
        print(f'Processing {file}')
        print(df.head())

# Main function
def main():
    process_csv_files()
    process_excel_files()

if __name__ == "__main__":
    main()
