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
    
    # Write to output file
    with open('output.txt', 'w') as f:
        f.write("Tables in the database:\n")
        f.write(tables_df.to_string(index=False))
        f.write("\n\n")



# Main function to run the script
def main():
    engine = create_engine(db_url)
    
    # List all tables
    list_tables(engine)
    
  

if __name__ == "__main__":
    main()
