import pandas as pd
import numpy as np
# import warnings
import bs4 as bs
import requests
import streamlit as st



def income_statement(ticker, income_soup):
    pass

    # ## Empty List of div tags
    financials_div_list = []

    # List of  all div tags
    for div in income_soup.find_all('div'):
        # Get the contents and titles
        financials_div_list.append(div.string)

        # Prevent duplicate titles
        if not div.string == div.get('title'):
            financials_div_list.append(div.get('title'))
            
    # ## Filter out irrelevant data
    financials_div_list = [category for category in financials_div_list if category not in
                ('Operating Expenses', 'Expand All')]

    # # Filter out 'empty' elements
    financials_div_list = list(filter(None, financials_div_list))

    # # Filter out functions
    financials_div_list = [category for category in financials_div_list if not category.startswith('(function')]

    print("financials_div_list: ", financials_div_list)
    
    # Sublist the relevant financial information
    income_list = financials_div_list[13: -5]

    income_list.insert(0, 'Breakdown')

    # ## DataFrame of the financial data

    # Store the financial items as a list of tuples
    income_data = list(zip(*[iter(income_list)]*6))

    income_df = pd.DataFrame(income_data)
    # st.write(income_df)
    
    # Make the top row the headers
    headers = income_df.iloc[0]
    income_df = income_df[1:]
   
    income_df.columns = headers
    income_df.set_index('Breakdown', inplace=True, drop=True)

    print(income_df)

    return income_df

def write_file(name, content):
    f = open("{}.txt".format(name), "w")
    f.write(content)
    f.close()
    return

if __name__ == "__main__":
    ticker = 'TSLA'

    # ## Read the yahoo income statement url and assign URL
    income_url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'

    read_income_url = requests.get(income_url, headers={'User-Agent': 'Custom'})

    # BeautifulSoup the xml
    income_soup = bs.BeautifulSoup(read_income_url.text, "lxml")
    
    # create a file and write the xml/html file extracted by BeautifulSoup
    write_file("income_soup", str(income_soup))
    
    income_df = income_statement(ticker, income_soup)
    st.markdown("### {}: Income Statement".format(ticker))
    st.markdown("###### (All numbers in thousands)")
    st.write(income_df)







# chart_data = pd.DataFrame(
#     income_df.columns,
#     columns=income_df.iloc[0]
# )

# st.write(chart_data)

# # print(income_df.columns)

# # chart_data = pd.DataFrame(
# #     income_df.columns[1:],
# #     columns=income_df.iloc[0]
# # )

# # # print(income_df.columns[1:])
# st.line_chart(chart_data)