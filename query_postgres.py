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
    ORDER BY table_name
    '''
    
    with engine.connect() as conn:
        result = conn.execute(text(query))
        tables = [row[0] for row in result.fetchall()]
    
    return tables

# Function to perform a SELECT query on a specific table
def select_from_table(engine, table_name):
    query = text(f'SELECT * FROM {table_name} LIMIT 5')
    
    with engine.connect() as conn:
        result = conn.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    
    return df

# Main function to run the script
def main():
    engine = create_engine(db_url)
    
    # List all tables
    tables = list_tables(engine)
    
    # Write to output file
    with open('pcos_data/output.txt', 'w') as f:
        f.write("Tables in the database:\n")
        f.write(", ".join(tables))
        f.write("\n\n")
        
        # Perform SELECT queries on each table
        for table in tables:
            df = select_from_table(engine, table)
            f.write(f"Data from table {table}:\n")
            f.write(df.to_string(index=False))
            f.write("\n\n")

if __name__ == "__main__":
    main()
