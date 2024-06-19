import os
import pandas as pd
from sqlalchemy import create_engine

# Database connection URL
db_url = os.getenv('DB_URL')

# Directory containing the data files
data_dir = 'pcos_data'

# Establish database connection
engine = create_engine(db_url)

# Function to create table from a file
def create_table_from_file(file_path):
    file_name = os.path.basename(file_path)
    table_name, file_extension = os.path.splitext(file_name)

    if file_extension == '.csv':
        df = pd.read_csv(file_path)
    elif file_extension == '.xlsx':
        df = pd.read_excel(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")
        return

    # Convert DataFrame to SQL table
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Table '{table_name}' created successfully from '{file_name}'.")

# Loop through each file in the data directory
for file_name in os.listdir(data_dir):
    file_path = os.path.join(data_dir, file_name)
    if os.path.isfile(file_path):
        create_table_from_file(file_path)
