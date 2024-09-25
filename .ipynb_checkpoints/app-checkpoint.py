import streamlit as st
from datetime import datetime, timedelta
from frankfurter import *
from currency import *




#====================================================================PAGE CONFIG
apptitle = 'Currency Conversion App'

st.set_page_config(page_title=apptitle, 
                   page_icon="💰")




# Show the title and the logo in the same line
col1, col2 = st.columns([3, 1]) # ratio between columns

with col1:
    st.title("Currency Conversion App")

with col2:
    st.image('logo.png', width=100) 


st.markdown("""
<h2 style='text-align: center; font-size: 20px'> 
    The Currency Conversion App uses the Frankfurter API to retrieve the conversion rates between two currency codes of in a certain date.
</h2>
            
<p style='text-align: center; font-size: 16px'>
    See the documentation on 
    <a href='https://github.com/rodzarayai/dsp_at2_13832516/blob/master/README.md' target='_blank'>GitHub</a>.
</p>
""", unsafe_allow_html=True)

st.header("", divider="gray")


#====================================================================CURRENCY LIST

# Get the list of available currencies from Frankfurter
currencies  = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if currencies is None:
    st.error('Failed to retrieve currency list', icon="🚨")
    
else: 

    
#====================================================================CAPTURE INPUTS

    # Add input fields for capturing amount, from and to currencies
    currency_list = [f"{code} - {name}" for code, name in currencies.items()]
    st.markdown(
    """
    <style>
    label {
        font-size: 40px;
    }
    </style>
    """, 
    unsafe_allow_html=True
    )
   
    #Amount as float
    amount = st.number_input('Enter the amount to be converted:', 1.0)
    
    #From code, considering the name of the currency for better understanding
    from_code = st.selectbox('From currency', currency_list)
    
    #From currency, for code usage
    from_currency = from_code.split('-')[0].strip()
    
    #To code, considering the name of the currency for better understanding
    to_code = st.selectbox('To currency', currency_list, index=1) #Start on the second position to avoid error 
    
    #To currency, for code usage
    to_currency = to_code.split('-')[0].strip()
    
    


#====================================================================LATEST BUTTON


    # Add a button to get and display the latest rate for selected currencies and amount
    latest_button = st.button('Get latest rate')
    if latest_button:
        try:
            latest_date, fx_rate = get_latest_rates(from_currency, to_currency, amount)
            print(fx_rate)
            
            fx_rate = round_rate(fx_rate)


            output_mssg = format_output(latest_date, from_currency, to_currency, fx_rate, amount, latest=True)
            
            st.write(output_mssg)
            
            #Print the last 30 days
            df_period = get_last_period(from_currency, to_currency, latest_date)
            #print(df_period)
            #print("calling plot")
            fig = make_conversion_chart(df_period, from_currency, to_currency)
            st.plotly_chart(fig)

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
            
            fx_rate = get_historical_rate(from_currency, to_currency, historical_date,  amount)            
            
            output_mssg = format_output(historical_date, from_currency, to_currency, fx_rate, amount, latest=False)
            
            st.write(output_mssg)
            
            #Print the last 30 days
            df_period = get_last_period(from_currency, to_currency, historical_date)
            #print(df_period)
            #print("calling plot")
            fig = make_conversion_chart(df_period, from_currency, to_currency)
            st.plotly_chart(fig)
            
        except:
            if amount == 0.0:
                st.error('Failed to convert. Check amount to convert should be more than 0.0', icon="🚨")
            elif from_code == to_code:
                st.error('Failed to convert. From currency must be different to To currency', icon="🚨")
            else:
                st.error('Failed to convert.', icon="🚨")
    


















