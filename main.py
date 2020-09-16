import pandas as pd

master_df = pd.read_excel('travel.xlsx', sheet_name='Data', header=0, index_col=0)

'''
Q4TOT: (SF Residents) How many trips did you take yesterday?
Q5TOT: (SF Residents) How many trips did you take (outside of your home) TWO DAYS AGO.
CRSHRE: Total of all Drove Car Share (3) entries for Q4aM to Q5hM
TNC: Total of all TNC (5) entries for Q4aM to Q5hM
'''
sf_residents = master_df[['Q4TOT', 'Q5TOT', 'CRSHRE', 'TNC']]
sf_residents = sf_residents.dropna()
print(len(sf_residents))

sf_residents = sf_residents[(sf_residents['CRSHRE'] != 0.0)
                           | sf_residents['TNC'] != 0.0]    
print(len(sf_residents))

'''
Q6: (Outside SF Residents) Over the past 30 days, about how many total days have you gone into San Francisco
CRSHRE1: Total of all Drove Car Share (3) entries for Day 1 (Q7M, Q9M-Adj, Q11aM to Q11fM) multiplied by Q12
TNC1: Total of all TNC (5) entries for Day 1 (Q7M, Q9M-Adj, Q11aM to Q11fM) multiplied by Q12
'''
outside_sf_residents = master_df[['Q6', 'CRSHRE1', 'TNC1']]
outside_sf_residents = outside_sf_residents.dropna()
print(len(outside_sf_residents))

outside_sf_residents = outside_sf_residents[(outside_sf_residents['CRSHRE1'] != 0.0)
                                           | outside_sf_residents['TNC1'] != 0.0]
print(len(outside_sf_residents))