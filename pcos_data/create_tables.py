import os
import pandas as pd
from sqlalchemy import create_engine

# Retrieve DB_URL from environment variables
DB_URL = os.getenv('DB_URL')

def create_tables():
    # Establish database connection
    engine = create_engine(DB_URL)

    # List all CSV and Excel files in pcos_data directory
    files = [file for file in os.listdir('pcos_data') if file.endswith('.csv') or file.endswith('.xlsx')]

    # Iterate through each file and create tables
    for file in files:
        table_name = os.path.splitext(file)[0]  # Use file name as table name
        file_path = os.path.join('pcos_data', file)

        # Read CSV or Excel file into Pandas DataFrame
        if file.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file.endswith('.xlsx'):
            df = pd.read_excel(file_path, engine='openpyxl')
        else:
            continue

        # Write DataFrame to SQL table
        df.to_sql(table_name, con=engine, index=False, if_exists='replace')

        print(f"Table '{table_name}' created successfully.")

if __name__ == '__main__':
    create_tables()
