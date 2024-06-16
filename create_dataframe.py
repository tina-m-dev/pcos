import pandas as pd

# Replace 'PCOS_infertility.csv' with the actual path to your CSV file
csv_file = 'PCOS_infertility.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Display the DataFrame
print(df)
