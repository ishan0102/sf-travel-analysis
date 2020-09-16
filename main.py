import pandas as pd

master_df = pd.read_excel('travel.xlsx', sheet_name='Data', header=0, index_col=0)

'''
Q4TOT: (SF Residents) How many trips did you take yesterday?
Q5TOT: (SF Residents) How many trips did you take two days ago?
CRSHRE: (SF Residents) Total of all Drove Car Share (3) entries for Q4aM to Q5hM
TNC: (SF Residents) Total of all TNC (5) entries for Q4aM to Q5hM
'''
sf_res = master_df[['Q4TOT', 'Q5TOT', 'CRSHRE', 'TNC']]
sf_res = sf_res.dropna()
sf_res_total = len(sf_res)
sf_res_total_sum = sf_res['Q4TOT'].sum() + sf_res['Q5TOT'].sum()

sf_res = sf_res[(sf_res['CRSHRE'] != 0.0) | (sf_res['TNC'] != 0.0)]    
sf_res_active = len(sf_res)
sf_res_pct_active = str(round(sf_res_active / sf_res_total * 100, 3)) + "%"
sf_res_active_sum = sf_res['CRSHRE'].sum() + sf_res['TNC'].sum()
sf_res_active_sum_pct = str(round(sf_res_active_sum / sf_res_total_sum * 100, 3)) + "%"

'''
Q6: (Outside SF Residents) Over the past 30 days, about how many total days have you gone into San Francisco?
CRSHRE1: (Outside SF Residents) Total of all Drove Car Share (3) entries for Day 1 (Q7M, Q9M-Adj, Q11aM to Q11fM) multiplied by Q12
TNC1: (Outside SF Residents) Total of all TNC (5) entries for Day 1 (Q7M, Q9M-Adj, Q11aM to Q11fM) multiplied by Q12
'''
outside_sf_res = master_df[['Q6', 'CRSHRE1', 'TNC1']]
outside_sf_res = outside_sf_res.dropna()
outside_sf_res_total = len(outside_sf_res)
outside_sf_res_total_sum = outside_sf_res['Q6'].sum()

outside_sf_res = outside_sf_res[(outside_sf_res['CRSHRE1'] != 0.0) | (outside_sf_res['TNC1'] != 0.0)]
outside_sf_res_active = len(outside_sf_res)
outside_sf_res_pct_active = str(round(outside_sf_res_active / outside_sf_res_total * 100, 3)) + "%"
outside_sf_res_active_sum = outside_sf_res['CRSHRE1'].sum() + outside_sf_res['TNC1'].sum()
outside_sf_res_active_sum_pct = str(round(outside_sf_res_active_sum / outside_sf_res_total_sum * 100, 3)) + "%"

print("Percentage of rideshares among total rides within SF recently: " + sf_res_active_sum_pct)
print("Percentage of rideshares among total rides to SF recently: " + outside_sf_res_active_sum_pct)
print("Percentage of SF residents who have used rideshare within SF recently: " + sf_res_pct_active)
print("Percentage of non-SF residents who have used rideshare to go to SF recently: " + outside_sf_res_pct_active)

'''
Q27: How old are you?
Q28-1: What is your race or ethnic identification?
'''

