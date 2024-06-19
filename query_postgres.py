from sqlalchemy import create_engine, text
import pandas as pd

# Replace with your PostgreSQL database connection URL
db_url = 'postgresql://user:password@localhost:5432/mydatabase'

# Function to list all tables in the public schema
def list_tables(engine):
    query = '''
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    '''
    
    with engine.connect() as conn:
        result = conn.execute(text(query))
        tables_df = pd.DataFrame(result.fetchall(), columns=result.keys())
    
    print("Tables in the database:")
    print(tables_df)

# Function to perform a SELECT query on a specific table
def select_from_table(engine, table_name):
    query = text(f'SELECT * FROM {table_name} LIMIT 5')
    
    with engine.connect() as conn:
        result = conn.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    
    print(f"Data from table {table_name}:")
    print(df)

# Main function to run the script
def main():
    engine = create_engine(db_url)
    
    # List all tables
    list_tables(engine)
    
    # Perform a SELECT query on a specific table (replace 'your_table_name' with actual table name)
    table_name = 'your_table_name'  # Replace with the actual table name you want to query
    select_from_table(engine, table_name)

if __name__ == "__main__":
    main()
