import pandas as pd
import numpy as np
# import warnings
import bs4 as bs
import requests
import streamlit as st

from income_statement.income_statement import income_statement
from file_management.write_operations import write_file


if __name__ == "__main__":
    ticker = 'TSLA'

    # ## Read the yahoo income statement url and assign URL
    income_url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'

    read_income_url = requests.get(income_url, headers={'User-Agent': 'Custom'})

    # BeautifulSoup the xml
    income_soup = bs.BeautifulSoup(read_income_url.text, "lxml")
    
    # create a file and write the xml/html file extracted by BeautifulSoup
    write_file("income_soup", str(income_soup))
    
    income_df = income_statement(income_soup)
    st.markdown("### {}: Income Statement".format(ticker))
    st.markdown("###### (All numbers in thousands)")
    st.write(income_df)

