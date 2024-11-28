# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:57:52 2024

@author: Sherq
"""

import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
import os

def fetch_cpi_data():
    # Define the time period for CPI data (last 5 years)
    end_date = datetime.today()
    start_date = datetime(end_date.year - 5, end_date.month, end_date.day)

    # Fetch the CPI data from FRED (Federal Reserve Economic Data)
    cpi_data = web.DataReader('CPIAUCNS', 'fred', start_date, end_date)

    return cpi_data

def calculate_inflation(cpi_data):
    # Calculate year-over-year inflation for each quarter
    cpi_data['Inflation'] = cpi_data['CPIAUCNS'].pct_change(4) * 100  # Percentage change over 4 periods (quarters)

    # Filter the most recent 4 quarters
    inflation_last_4_quarters = cpi_data.tail(4)

    return inflation_last_4_quarters

def save_data(cpi_data, inflation_data):
    # Make sure the data folder exists
    os.makedirs('data', exist_ok=True)
    
    # Save CPI data to CSV
    cpi_data.to_csv('data/cpi_data.csv')
    print("CPI data saved to data/cpi_data.csv")
    
    # Save Inflation data to CSV
    inflation_data.to_csv('data/inflation_data.csv')
    print("Inflation data saved to data/inflation_data.csv")

if __name__ == "__main__":
    cpi_data = fetch_cpi_data()
    inflation_last_4_quarters = calculate_inflation(cpi_data)
    
    # Print the inflation for the last 4 quarters
    print("Last 4 Quarters of Inflation in the US:")
    print(inflation_last_4_quarters[['Inflation']])
    
    # Save the data to CSV files in the data folder
    save_data(cpi_data, inflation_last_4_quarters)

