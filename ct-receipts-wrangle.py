import pandas as pd

# Define the file paths
input_file = '/Users/femisokoya/Documents/GitHub/ct-receipts/CT_Receipts_Live_Table_Q4_2022-23.xlsx'
output_file = '/Users/femisokoya/Documents/GitHub/ct-receipts/ct-receipts-result-q.csv'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(input_file, sheet_name='Table_5')

# Drop rows 0 to 4
df = df.drop(range(4))

# Set row 6 as column headers
df.columns = df.iloc[0]
df = df[1:]

# Replace '[z]' with null and insert '[z]' in the 'Notes' column if necessary
for index, row in df.iterrows():
    if '[z]' in row.values:
        df.at[index, 'Notes'] = '[z]'
        df.loc[index] = df.loc[index].replace('[z]', pd.NA)

# Save the result as a CSV file
df.to_csv(output_file, index=False)

print("Result saved successfully as ct-receipts-result-q.csv")
