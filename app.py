import streamlit as st
import datetime
from frankfurter import *
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title

st.title("Currency convertor")
# Get the list of available currencies from Frankfurter

currencies  = get_currencies_list()
currency_codes = list(currencies.keys())

code = st.selectbox('Select a currency', currency_codes)

# If the list of available currencies is None, display an error message in Streamlit App

# Add input fields for capturing amount, from and to currencies

# Add a button to get and display the latest rate for selected currencies and amount

# Add a date selector (calendar)

# Add a button to get and display the historical rate for selected date, currencies and amount










