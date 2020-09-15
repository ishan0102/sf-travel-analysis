import pandas as pd

master_df = pd.read_excel('travel.xlsx', sheet_name='Data', header=0, index_col=0)
print(master_df)

