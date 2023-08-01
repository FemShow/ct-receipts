import pandas as pd

# Define the file paths
input_file = '/Users/femisokoya/Documents/GitHub/ct-receipts/CT_Receipts_Live_Table_Q4_2022-23.xlsx'
output_file = '/Users/femisokoya/Documents/GitHub/ct-receipts/ct-receipts-result.csv'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(input_file, sheet_name='Table_4')

# Drop rows 0 to 4
df = df.drop(range(5))

# Set row 6 as column headers
df.columns = df.iloc[0]
df = df[1:]

# Melt the DataFrame
df_melted = df.melt(
    id_vars=["ONS Code", "Local authority"],
    value_vars=[
        "Receipts of council taxes in respect of 2022 to 2023",
        "Receipts of previous years council taxes",
        "Receipts of council taxes in respect of 2023 to 2024",
        "Total receipts of council taxes collected during the financial year"
    ],
    var_name="Occurrence",
    value_name="Observation"
)

# Save the melted DataFrame as a CSV file
df_melted.to_csv(output_file, index=False)

print("Result saved successfully as ct-receipts-result.csv")
