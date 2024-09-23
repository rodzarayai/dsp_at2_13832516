from api import get_url
import json
import pandas as pd


BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    dict
        dicttionary of  available currencies with their name or None in case of error

    """
    
    currencies_url = f"{BASE_URL}/currencies"
    status_code, data = get_url(currencies_url)
    if status_code == 200:
        #print(data)
        #return a dict with code and name. It is better for showing the names, since the codes can be unkown for the users
        return data
    else:
        print(f"Failed to retrieve currency list. Status code: {status_code}")
        return None
        
    

def get_latest_rates(from_currency, to_currency, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error

    """

    latest_url = f"{BASE_URL}/latest?amount={amount}&from={from_currency}&to={to_currency}"
    status_code, data = get_url(latest_url)
    if status_code == 200:
        # Flatten the data to include amount and base as columns
        fx_rate = float(list(data['rates'].values())[0])
        return data['date'], fx_rate
    else:
        print(f"Failed to retrieve data. Status code: {status_code}")
        return None
        
    
    
    

def get_historical_rate(from_currency, to_currency, from_date, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """
    
    url = f"{BASE_URL}/{from_date}?amount={amount}&from={from_currency}&to={to_currency}"
    
    status_code, data = get_url(url)
    if status_code == 200:
        data = response.json()
        # Flatten the data to include amount and base as columns
        fx_rate = float(list(data['rates'].values())[0])
        return fx_rate
    else:
        print(f"Failed to retrieve data. Status code: {status_code}")
        return None


#Get a conversion period. Should not be longer than 90 days
def get_last_period(from_currency, to_currency, date_from=None, date_to=None, amount=1.0):
    """
    Function to retrieve currency conversion data for the past 60 days by default, 
    or a custom date range if provided. Ensures the period is no longer than 90 days.

    Parameters
    ----------
    from_currency : str
        The currency code to convert from.
    to_currency : str
        The currency code to convert to.
    date_from : str, optional
        The starting date in 'YYYY-MM-DD' format. Defaults to None.
    date_to : str, optional
        The ending date in 'YYYY-MM-DD' format. Defaults to None.
    amount : float, optional
        The amount to convert. Default is 1.0.

    Returns
    -------
    DataFrame
        A DataFrame containing the conversion rates for the selected period.
    """
    
    # Get the latest date if no date_to is provided
    latest_date_str, fx_rate = get_latest_rates(convert_from, convert_to, amount)
    latest_date = datetime.strptime(latest_date_str, '%Y-%m-%d')

    if not date_from and not date_to: #If they are not given, the calculate 60 days    
        # Subtract 30 days from the latest date
        prior_60_date = latest_date - timedelta(days=30)
        date_from_str = prior_60_date.strftime('%Y-%m-%d')
        date_to_str = latest_date_str
    else:
        date_from_date = datetime.strptime(date_from, '%Y-%m-%d')
        date_to_date = datetime.strptime(date_to, '%Y-%m-%d')
        
        # Check if both dates are provided, if not, default to 30 days prior
        if not date_from_date:
            date_from_date = date_to_date - timedelta(days=30)
        if not date_to_date:
            date_to_date = date_from_date + timedelta(days=30)
        
        # Check that date_to_obj does not exceed the latest date
        if date_to_date > latest_date:
            date_to_date = latest_date
            
        # Calculate difference in days
        days_difference = (date_to_date - date_from_date).days
        
        # Ensure the period is not longer than 90 days
        if days_difference > 90:
            raise ValueError("The date range cannot be longer than 90 days")
        
        # Convert dates back to string
        date_from_str = date_from_date.strftime('%Y-%m-%d')
        date_to_str = date_to_date.strftime('%Y-%m-%d')

 
    url = f"https://api.frankfurter.app/{date_from_str}..{date_to_str}?amount={amount}?from={from_currency}&to={to_currency}"
    status_code, data = get_url(url)
    if status_code == 200:
        # Unpack rates in the format {date: rate}
        dates_rates = {date: list(rates.values())[0] for date, rates in data["rates"].items()}
        # Flatten the data to include amount and base as columns
        flat_data = {**{'start_date': data['start_date'],'amount': data['amount'], 'base': data['base'], 'converted_to': to_currency},**dates_rates}
        df = pd.DataFrame([flat_data])
        return df
    else:
        print(f"Failed to retrieve data. Status code: {status_code}")
        return None