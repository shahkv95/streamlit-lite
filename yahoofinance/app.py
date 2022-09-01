import pandas as pd
import numpy as np
import streamlit as st

from income_statement.income_statement import get_income_statement
from file_management.write_operations import write_file
from file_management.read_operations import web_scrapper


if __name__ == "__main__":

    ticker = st.selectbox(
        "Choose the ticker",
        ('TSLA','AAPL','MSFT')
    )

    scrapped_file = web_scrapper(ticker)

    write_file("income_soup", str(scrapped_file))

    income_df = get_income_statement(scrapped_file)

    st.markdown("### {}: Income Statement".format(ticker))
    st.markdown("###### (All numbers in thousands)")
    st.write(income_df)