# <Currency Conversion App>

## Author
Name: *Rodrigo Araya*
    
Student ID: *13832516*
    
Web App: https://currencyconverter-dsp-13832516.streamlit.app/

## Description
The Currency Conversion App uses the Frankfurter API to retrieve the conversion rates between two currency codes on a certain date. The user can choose between the latest available rate and any historical date in the past ten years. The app provides a user-friendly interface using Streamlit and includes visualizations of exchange rates for the last 30 days for any selected date.
    
### Challenges:

* Implementing error handling for API responses and making the user experience smooth when dealing with unexpected errors (e.g., Set an initial amount to xchange and diffferent curriencies).

    
### Future Implementations:

## How to Setup
To set up the development environment for the Currency Conversion App, follow these steps:

1. Clone the repository:
    
    git clone https://github.com/your-repo-link/currency-conversion-app.git

2. Install dependencies:
    
    pip install -r requirements.txt

The requirements and packages used are explained below

3. Run the application:
    
    streamlit run app.py
    
    Alternative, the user can access to the public web site in https://currencyconverter-dsp-13832516.streamlit.app/
    
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
    Web-site
        https://currencyconverter-dsp-13832516.streamlit.app/
2. Input Options:

    * Choose the from currency and to currency.
    * Enter the amount you wish to convert.
    * Select the conversion date—either the latest available rate or a specific historical date.

3. Results:

The app will display the conversion rate, the converted amount, and additional information like the inverse conversion rate.
You can also visualize the conversion trends over time using the interactive graph.

## Project Structure
<List all folders and files of this project and provide quick description for each of them>

## Citations
<Mention authors and provide links code you source externally>
