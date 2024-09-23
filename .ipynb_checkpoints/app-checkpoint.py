import streamlit as st
import datetime
from frankfurter import *
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title

st.title("Currency Converter")
# Get the list of available currencies from Frankfurter

currencies  = get_currencies_list()

if currencies is None:
    st.error('Failed to retrieve currency list', icon="🚨")
    
else: 

    currency_list = [f"{code} - {name}" for code, name in currencies.items()]



    amount = st.number_input('Enter the amount to be converted:')

    from_code = st.selectbox('From currency', currency_list)
    from_currency = from_code.split('-')[0].strip()
    
    to_code = st.selectbox('To currency', currency_list)
    to_currency = to_code.split('-')[0].strip()
    
    latest_button = st.button('Get latest rate')
    if latest_button:
        try:
            latest_date, fx_rate = get_latest_rates(from_currency, to_currency, amount)
            print(fx_rate)
            reverse_rate = reverse_rate(fx_rate)
            fx_rate = round_rate(fx_rate)

            base_rate = fx_rate / amount 
                
            base_rate = round_rate(base_rate)
            
            
            st.write(f'As of {latest_date}, The latest available conversion rate from {from_currency} to {to_currency} was {base_rate}.')
            st.write(f'Therefore, {amount} in {from_currency} correspond to {fx_rate} in {to_currency}.The inverse rate was {reverse_rate}')
        except:
            st.error('Failed to convert. Check amount to convert should be more than 0.0', icon="🚨")
    
    
    historical_date = st.date_input('Select a date for historical rates')
    historical_button = st.button('Get conversion rate')
    
    if historical_button:
        try:
            fx_rate = get_historical_rate(from_currency, to_currency, historical_date, amount)
            reverse_rate = reverse_rate(fx_rate)
            fx_rate = round_rate(fx_rate)
            base_rate = fx_rate / amount 
            base_rate = round_rate(base_rate)
            
            
            st.write(f'As of {historical_date}, the conversion rate from {from_currency} to {to_currency} was {base_rate}.')
            st.write(f'Therefore, {amount} in {from_currency} correspond to {fx_rate} in {to_currency}.The inverse rate was {reverse_rate}')
        except:
            st.error('Failed to convert. Check amount to convert should be more than 0.0', icon="🚨")
    


# If the list of available currencies is None, display an error message in Streamlit App

# Add input fields for capturing amount, from and to currencies

# Add a button to get and display the latest rate for selected currencies and amount

# Add a date selector (calendar)

# Add a button to get and display the historical rate for selected date, currencies and amount










