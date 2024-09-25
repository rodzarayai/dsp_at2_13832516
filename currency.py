import plotly.express as px
import pandas as pd

def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    
    return round(rate, 4)
    

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    if rate > 0:
        return round((1.0 / rate),4)
    
    else:
        return 0.0000
    
    
    
    
def format_output(date, from_currency, to_currency, rate,  amount, latest=True):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    #Reverse rate
    inverse_rate = reverse_rate(rate)
    
    #Reverse rate
    
    base_rate = rate / amount 
    print(base_rate)
    base_rate = round_rate(base_rate) #format
    print(base_rate)
                                
    if latest:
        output_mssg = f"As of {date}, the latest available conversion rate from {from_currency} to {to_currency} was {base_rate}.\nTherefore, {amount} in {from_currency} correspond to {rate} in {to_currency}. The inverse rate was {inverse_rate}."
    
    else:
        output_mssg = f"As of {date}, the conversion rate from {from_currency} to {to_currency} was {base_rate}.\nTherefore, {amount} in {from_currency} correspond to {rate} in {to_currency}. The inverse rate was {inverse_rate}."
    
    
    return output_mssg


def make_conversion_chart(df,from_currency, to_currency):
    """
    Function to create an interactive line chart using Plotly, showing currency conversion
    rates over a specified period.

    Parameters
    ----------
    from_currency : str
        The currency code to convert from.
    to_currency : str
        The currency code to convert to.
    historical_date : str
        The end date for the historical period.
    amount : float
        The amount to convert.

    Returns
    -------
    fig : 
        A plotly interactive figure with conversion rates over time.
    """
    # Get the period data (dates and rates)
  
    print('1')
    # Extract only the date columns
    date_columns = df.columns.difference(['start_date', 'amount', 'base', 'converted_to'])
    df_rates = df.melt(var_name='date', value_name='rate', value_vars=date_columns)
    #print(date_columns)
    #print(df_rates)
    # Convert the 'date' column to datetime
    df_rates['date'] = pd.to_datetime(df_rates['date'])
    #print(df_rates)
    #print(df_rates.info())
    # Create the interactive line chart using Plotly
    fig = px.line(
            df_rates, 
            x='date', 
            y='rate', 
            title=f'Conversion Rate from {from_currency} to {to_currency} Over Time',
            labels={'rate': f'Conversion Rate ({to_currency})', 'date': 'Date'},
            markers=True
        )
    return fig

    

