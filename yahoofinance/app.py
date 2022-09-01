import pandas as pd
import numpy as np
import streamlit as st

from income_statement.income_statement import income_statement
from file_management.write_operations import write_file
from file_management.read_operations import web_scrapper


if __name__ == "__main__":
    ticker = 'TSLA'

    income_soup = web_scrapper(ticker)
    
    # create a file and write the xml/html file extracted by BeautifulSoup
    write_file("income_soup", str(income_soup))
    
    income_df = income_statement(income_soup)
    st.markdown("### {}: Income Statement".format(ticker))
    st.markdown("###### (All numbers in thousands)")
    st.write(income_df)

