import pandas as pd
from sqlalchemy import create_engine
import glob
import os
import subprocess

# Path to CSV and Excel files directory
files_path = 'pcos_data/'


# Function to process CSV files
def process_csv_files():
    csv_files = glob.glob(files_path +'*.csv')
    print(csv_files)
    for file in csv_files:
        df = pd.read_csv(file)
        table_name = file.split('/')[-1].split('.')[0]  # Extract table name from file name
        df_to_sql(df, table_name)
        


# Function to process Excel files
def process_excel_files():
    excel_files = glob.glob(files_path + '*.xlsx')
    for file in excel_files:
        df = pd.read_excel(file, sheet_name='Sheet1')  # Adjust sheet_name as needed
        table_name = file.split('/')[-1].split('.')[0]  # Extract table name from file name
        df_to_sql(df, table_name)

# Function to convert DataFrame to SQL table
def df_to_sql(df, table_name):
    engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')  # Replace with your database connection URL
    df.to_sql(table_name, engine, index=False, if_exists='replace')  # Change if_exists as needed ('replace', 'append', 'fail')

# Function to export database to SQL file
def export_database_to_sql():
    try:
        result = subprocess.run(['pg_dump', '-U', 'user', '-d', 'mydatabase', '-f', 'pcos_data/mydatabase.sql'],
                                capture_output=True, text=True, check=True)
        print("pg_dump output:", result.stdout)
        print("pg_dump errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("Error during pg_dump:", e.output)
        print("pg_dump stdout:", e.stdout)
        print("pg_dump stderr:", e.stderr)


# Main function
def main():
    print("Processing CSV files:")
    process_csv_files()
    print("\nProcessing Excel files:")
    process_excel_files()
    print("\nExporting database to SQL file:")
    export_database_to_sql()

if __name__ == "__main__":
    main()
