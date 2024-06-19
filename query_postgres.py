from sqlalchemy import create_engine, text
import pandas as pd

# Replace with your PostgreSQL database connection URL
db_url = 'postgresql://user:password@localhost:5432/mydatabase'

# Function to query data from PostgreSQL
def query_data():
    # Create SQLAlchemy engine
    engine = create_engine(db_url)

    # Example SELECT statement
    query = '''
        SELECT *
        FROM pcos
        
    '''

    # Example parameter (replace with actual parameter value)
    #param_value = 'some_value'

    # Execute query and fetch results into a pandas DataFrame
    with engine.connect() as conn:
        result = conn.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    # Print or process the retrieved data as needed
    print(df.head())

# Main function to run the script
def main():
    query_data()

if __name__ == "__main__":
    main()
