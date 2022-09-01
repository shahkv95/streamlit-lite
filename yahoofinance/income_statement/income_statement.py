import pandas as pd

def get_income_statement(income_soup):

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
