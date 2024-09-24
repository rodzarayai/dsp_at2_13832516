import streamlit as st
import datetime
from frankfurter import *
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title("Currency Converter")

# Get the list of available currencies from Frankfurter
currencies  = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if currencies is None:
    st.error('Failed to retrieve currency list', icon="🚨")
    
else: 

    
#====================================================================CAPTURE INPUTS

    # Add input fields for capturing amount, from and to currencies
    currency_list = [f"{code} - {name}" for code, name in currencies.items()]
   
    #Amount as float
    amount = st.number_input('Enter the amount to be converted:')
    
    #From code, considering the name of the currency for better understanding
    from_code = st.selectbox('From currency', currency_list)
    
    #From currency, for code usage
    from_currency = from_code.split('-')[0].strip()
    
    #To code, considering the name of the currency for better understanding
    to_code = st.selectbox('To currency', currency_list)
    
    #To currency, for code usage
    to_currency = to_code.split('-')[0].strip()
    
    


#====================================================================LATEST BUTTON


    # Add a button to get and display the latest rate for selected currencies and amount
    latest_button = st.button('Get latest rate')
    if latest_button:
        try:
            latest_date, fx_rate = get_latest_rates(from_currency, to_currency, amount)
            #print(fx_rate)
            inverse_rate = reverse_rate(fx_rate)
            
            fx_rate = round_rate(fx_rate)

            base_rate = fx_rate / amount 
                
            base_rate = round_rate(base_rate)
            
            
            output_mssg = format_output(latest_date, from_currency, to_currency, base_rate, inverse_rate, amount, fx_rate, latest=True)
            
            st.write(output_mssg)

        except:
            if amount == 0.0:
                st.error('Failed to convert. Check amount to convert should be more than 0.0', icon="🚨")
            elif from_code == to_code:
                st.error('Failed to convert. From currency must be different to To currency', icon="🚨")
            else:
                st.error('Failed to convert.', icon="🚨")

#====================================================================HISTORICAL BUTTON
    
    # Add a date selector (calendar)
    historical_date = st.date_input('Select a date for historical rates')
    
    # Add a button to get and display the historical rate for selected date, currencies and amount
    historical_button = st.button('Get conversion rate')
    
    if historical_button:
        try:
            fx_rate = get_historical_rate(from_currency, to_currency, historical_date, amount)
            inverse_rate = reverse_rate(fx_rate)
            fx_rate = round_rate(fx_rate)
            base_rate = fx_rate / amount 
            base_rate = round_rate(base_rate)
            
            
            output_mssg = format_output(historical_date, from_currency, to_currency, base_rate, inverse_rate, amount,fx_rate, latest=False)
            st.write(output_mssg)
            
            #
            df_period = get_last_period(from_currency, to_currency, None, historical_date, amount)
            print(df_period)
            display_conversion_chart()
            
        except:
            if amount == 0.0:
                st.error('Failed to convert. Check amount to convert should be more than 0.0', icon="🚨")
            elif from_code == to_code:
                st.error('Failed to convert. From currency must be different to To currency', icon="🚨")
            else:
                st.error('Failed to convert.', icon="🚨")
    





















