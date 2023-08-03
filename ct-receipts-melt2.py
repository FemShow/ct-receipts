import pandas as pd

# Define the file paths
input_file = '/Users/femisokoya/Documents/GitHub/ct-receipts/CT_Receipts_Live_Table_Q4_2022-23.xlsx'
output_file = '/Users/femisokoya/Documents/GitHub/ct-receipts/ct-receipts-result-q1.csv'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(input_file, sheet_name='Table_5')

# Drop rows 0 to 3
df = df.drop(range(4))

# Set row 4 as column headers
df.columns = df.iloc[0]
df = df[1:]

# Replace '[z]' with null and insert '[z]' in the 'Notes' column
df.replace('[z]', pd.NA, inplace=True)

# Define the list of value variables (quarters)
value_vars = [
    "April to June 2010 (Q1)", "July to September 2010 (Q2)", "October to December 2010 (Q3)", "January to March 2011 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2010 to 2011 (Q1 to Q4)",
    "April to June 2011 (Q1)", "July to September 2011 (Q2)", "October to December 2011 (Q3)", "January to March 2012 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2011 to 2012 (Q1 to Q4)" ,
    "April to June 2012 (Q1) ", "July to September 2012 (Q2)", "October to December 2012 (Q3)", "January to March 2013 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2012 to 2013 (Q1 to Q4)",
    "April to June 2013 (Q1)", "July to September 2013 (Q2)", "October to December 2013 (Q3)", "January to March 2014 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2013 to 2014 (Q1 to Q4) " ,
    "April to June 2014 (Q1) ", "July to September 2014 (Q2)", "October to December 2014 (Q3)", "January to March 2015 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2014 to 2015 (Q1 to Q4)",
    "April to June 2015 (Q1) ", "July to September 2015 (Q2)", "October to December 2015 (Q3)", "January to March 2016 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2015 to 2016 (Q1 to Q4)",
    "April to June 2016 (Q1)", "July to September 2016 (Q2)", "October to December 2016 (Q3)", "January to March 2017 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2016 to 2017 (Q1 to Q4)",
    "April to June 2017 (Q1)", "July to September 2017 (Q2)", "October to December 2017 (Q3)", "January to March 2018 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2017 to 2018 (Q1 to Q4)",
    "April to June 2018 (Q1)", "July to September 2018 (Q2)", "October to December 2018 (Q3)", "January to March 2019 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2018 to 2019 (Q1 to Q4)",
    "April to June 2019 (Q1)", "July to September 2019 (Q2)", "October to December 2019 (Q3)", "January to March 2020 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2019 to 2020 (Q1 to Q4)",
    "April to June 2020 (Q1) ", "July to September 2020 (Q2)", "October to December 2020 (Q3)", "January to March 2021 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2020 to 2021 (Q1 to Q4)",
    "April to June 2021 (Q1) ", "July to September 2021 (Q2)", "October to December 2021 (Q3)", "January to March 2022 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2021 to 2022 (Q1 to Q4)",
    "April to June 2022 (Q1)", "July to September 2022 (Q2)", "October to December 2022 (Q3)", "January to March 2023 (Q4)",
    "Total receipts of council taxes collected during the financial year - 2022 to 2023 (Q1 to Q4)"
]

# Melt the DataFrame
df_melted = df.melt(
    id_vars=["ONS Code", "Local authority", "Percentage Change (%) from Q4 2021", "Notes"],
    value_vars=value_vars,
    var_name="Occurrence",
    value_name="Observation"
)

# Insert '[z]' in the 'Notes' column for rows with null values in 'Percentage Change (%) from Q4 2021'
df_melted['Notes'] = df_melted.apply(lambda row: '[z]' if pd.isna(row["Percentage Change (%) from Q4 2021"]) else row['Notes'], axis=1)

# Save the melted DataFrame as a CSV file
df_melted.to_csv(output_file, index=False)

print("Result saved successfully as ct-receipts-result-q1.csv")
