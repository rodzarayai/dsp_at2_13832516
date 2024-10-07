# <Currency Conversion App>

## Author
Name: **Rodrigo Araya**
    
Student ID: **13832516**
    
Web App: https://currencyconverter-dsp-13832516.streamlit.app/

## Description
The Currency Conversion App uses the Frankfurter API to retrieve the conversion rates between two currency codes on a certain date. The user can choose between the latest available rate and any historical date in the past ten years. The app provides a user-friendly interface using Streamlit and includes visualizations of exchange rates for the last 30 days for any selected date.
    
### Challenges:
    
* Be constrained to all functions having an imposed ouput. Many functions are subject to enhancements, but a simple and standard format must be maintained, which limits development possibilities.

* Implementing error handling for API responses and making the user experience smooth when dealing with unexpected errors (e.g., Set different currencies (from and to) by default in order to avoid error messages).
    
* Find the proper way to extract the daily rates and transform the ouput into a dataframe ensuring the format and consistency required for plotting exchange rate trends over a 30-day period.

    
### Future Implementations:
    
* Ability to convert into multiple currencies, and implementing comparison graphs to show multiple currencies against one another over selected periods.
    
* Ability to download results as ***xlsx*** or ***csv*** files.
    

## How to Setup
To set up the development environment for the Currency Conversion App, follow these steps:

1. Clone the repository:
    
        git clone https://github.com/rodzarayai/dsp_at2_13832516.git

2. Install dependencies:
    
        pip install -r requirements.txt

The requirements and packages used are explained below

3. Run the application:
    
        streamlit run app.py
    
    Alternative, the user can access to the public website in https://currencyconverter-dsp-13832516.streamlit.app/
    
🐍 Python: Version: 3.9.12

📦 Packages used:
    
    * pandas: 2.0.1
    * streamlit: 1.28.1
    * requests: 2.31.0
    * plotly: 5.9.0



## How to Run the Program
1. Start the App:
    
    Locally:
    
        streamlit run app.py
    
    Website:
    
        https://currencyconverter-dsp-13832516.streamlit.app/
    
2. Input Options:

    * Choose the from currency and to currency.
    * Enter the amount you wish to convert.
    * Select the conversion date—either the latest available rate or a specific historical date.

3. Results:

    The app will display the conversion rate, the converted amount, and additional information like the inverse conversion rate.
    You can also visualize the conversion trends over time using the interactive graph.

## Project Structure

app.py: This is the main Streamlit script. It handles user inputs, manages the UI, and displays results using the streamlit library.
    
api.py: This script contains a function (get_url) for making API calls to external services like Frankfurter to fetch currency conversion data. 
    
frankfurter.py: This file includes functions to interact with the Frankfurter API, including calling the relevant endpoints and extracting currency exchange rates.
    
currency.py: Contains functions for formatting the conversion rates and results to be displayed in the Streamlit app. It also manages utility functions like calculating inverse rates and rounding numbers.
    
images/ (Optional): A folder to store any relevant images used in the app (e.g., background images or logos).

## Citations
<Mention authors and provide links code you source externally>
