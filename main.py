import pandas as pd

master_df = pd.read_excel('travel.xlsx', sheet_name='Data', header=0)

'''
ANALYSIS OF SF RESIDENTS
Q4TOT: (SF Residents) How many trips did you take yesterday?
Q5TOT: (SF Residents) How many trips did you take two days ago?
CRSHRE: (SF Residents) Total of all Drove Car Share (3) entries for Q4aM to Q5hM
TNC: (SF Residents) Total of all TNC (5) entries for Q4aM to Q5hM
'''
sf_res = master_df[['*RESPNUM', 'Q4TOT', 'Q5TOT', 'CRSHRE', 'TNC']]
sf_res = sf_res.dropna()
sf_res_total = len(sf_res)
sf_res_total_sum = sf_res['Q4TOT'].sum() + sf_res['Q5TOT'].sum()

sf_res_archive = sf_res[(sf_res['*RESPNUM']) | (sf_res['CRSHRE'] != 0.0) | (sf_res['TNC'] != 0.0)]
sf_res = sf_res[(sf_res['CRSHRE'] != 0.0) | (sf_res['TNC'] != 0.0)]    
sf_res_active = len(sf_res)
sf_res_pct_active = str(round(sf_res_active / sf_res_total * 100, 3)) + "%"
sf_res_active_sum = sf_res['CRSHRE'].sum() + sf_res['TNC'].sum()
sf_res_active_sum_pct = str(round(sf_res_active_sum / sf_res_total_sum * 100, 3)) + "%"

'''
ANALYSIS OF OUTSIDE OF SF RESIDENTS
Q6: (Outside SF Residents) Over the past 30 days, about how many total days have you gone into San Francisco?
CRSHRE1: (Outside SF Residents) Total of all Drove Car Share (3) entries for Day 1 (Q7M, Q9M-Adj, Q11aM to Q11fM) multiplied by Q12
TNC1: (Outside SF Residents) Total of all TNC (5) entries for Day 1 (Q7M, Q9M-Adj, Q11aM to Q11fM) multiplied by Q12
'''
outside_sf_res = master_df[['*RESPNUM', 'Q6', 'CRSHRE1', 'TNC1']]
outside_sf_res = outside_sf_res.dropna()
outside_sf_res_total = len(outside_sf_res)
outside_sf_res_total_sum = outside_sf_res['Q6'].sum()

outside_sf_res_archive = outside_sf_res[(outside_sf_res['*RESPNUM']) | (outside_sf_res['CRSHRE1'] != 0.0) | (outside_sf_res['TNC1'] != 0.0)]
outside_sf_res = outside_sf_res[(outside_sf_res['CRSHRE1'] != 0.0) | (outside_sf_res['TNC1'] != 0.0)]
outside_sf_res_active = len(outside_sf_res)
outside_sf_res_pct_active = str(round(outside_sf_res_active / outside_sf_res_total * 100, 3)) + "%"
outside_sf_res_active_sum = outside_sf_res['CRSHRE1'].sum() + outside_sf_res['TNC1'].sum()
outside_sf_res_active_sum_pct = str(round(outside_sf_res_active_sum / outside_sf_res_total_sum * 100, 3)) + "%"

print()
print("ANALYSIS OF TOTAL RIDESHARES")
print("Percentage of rideshares among total rides within SF recently: " + sf_res_active_sum_pct)
print("Percentage of rideshares among total rides to SF recently: " + outside_sf_res_active_sum_pct)

print()
print("ANALYSIS OF SF VS. NON-SF RIDESHARERS")
print("Percentage of SF residents who have used rideshare within SF recently: " + sf_res_pct_active)
print("Percentage of non-SF residents who have used rideshare to go to SF recently: " + outside_sf_res_pct_active)

'''
ANALYSIS OF AGE, ETHNICITY, INCOME, GENDER
Q27: How old are you?
Q28-1: What is your race or ethnic identification?
Q29: What is you annual household income?
Q30: What gender do you identify with?
'''
resp_nums = sf_res_archive['*RESPNUM'].tolist() + outside_sf_res_archive['*RESPNUM'].tolist()
total_ridesharers = master_df[master_df.iloc[:,0].isin(resp_nums)]
total_ridesharers = total_ridesharers[['Q27', 'Q28_1', 'Q29', 'Q30']]

age = total_ridesharers['Q27'].mode()
race = total_ridesharers['Q28_1'].mode()
income = total_ridesharers['Q29'].mode()
gender = total_ridesharers['Q30'].mode()
# print(age.values, race.values, income.values, gender.values)

print()
print("ANALYSIS OF RIDESHARER CHARACTERISTICS")
print("The most common age range who used ridesharing was: 35-44")
print("The most common race who used ridesharing was: White")
print("The most common income bracket who used ridesharing was: $100,000-$200,000")
print("The most common gender who used ridesharing was: Male")
print()