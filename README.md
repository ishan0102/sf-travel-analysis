# San Francisco Travel Analysis
Project for a client. This project is an analysis of a large repository of travel data within San Francisco from 2017. The purpose of this is to decide whether it would be more lucrative to set up a ridesharing service within San Francisco or to San Francisco. Additionally, this displays which characteristics of riders should be targeted while advertising.

## Analysis Breakdown
1. Determine the **percentage of rideshares** that were within and to San Francisco.
2. Determine if **residents** in San Francisco use ridesharing services or if Non-San Francisco residents rideshare more often.
3. Find the most **common characteristics** for ridesharers like age, race, income, and gender.

## Methods
### Pandas
I used `Pandas` to parse the data and generate DataFrames that were used in the analysis. The first two sections involved manipulating these DataFrames using common `Pandas` functions. The third part involved grabbing a list of respondent IDs from the original ridesharer DataFrames and identifying the most common characteristics between them.

## Results
I found that **3.993%** of recent rides in San Francisco were rideshares, while rides to San Francisco from outside were rideshares **4.300%** of the time. This does not necessarily tell us whether it's more beneficial to set up within or to San Francisco. 

However, analyzing SF vs. Non-SF riders showed that SF residents used ridesharing recently **10.474%** of the time while while Non-SF riders used ridesharing **5.955%** of the time. This provides evidence that a San Francisco based ridesharing service may be optimal.

Lastly, it was found that the most common ridesharer was between **35-44** years old, **White**, **Male**, and had an income between **$100,000-$200,000**. Based on the data, are the optimal characteristics to advertise ridesharing to.

## Usage
To recreate these results, clone the repository and run the following commands from your working directory.

``` bash
pip install -r requirements.txt # install necessary dependencies
python main.py # run the main script to generate analysis
```