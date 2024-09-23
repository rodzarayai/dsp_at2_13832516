import requests

def get_url(url: str):
    """
    Function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """
    try:
        # Make the GET request
        response = requests.get(url)
        
        # Check for a successful response (status code 200)
        if response.status_code == 200:
            data = response.json()
            return response.status_code, data
        else:
            # If status code is not 200, return the status code and error message
            return response.status_code, f"Error: {response.status_code} - {response.reason}"
    
    #Handle other errors during request
    except requests.RequestException as e:
        return 1000, f"Error: {str(e)}" #set 1000 as other error 

