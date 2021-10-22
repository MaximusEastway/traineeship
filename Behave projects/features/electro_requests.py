import requests


def website_up(url: str = "http://dingdata.nl/batterij"):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        print(f"An error has occures when trying to reach the URL: {url}")

def batterij_request(parameters: dict):
    """Use Requests to receive JSON file from the 'batterij' API.

    Args:
        parameters (dict): Parameters to send to the API

    Returns:
        dict: JSON based dictionary response from API
    """

    # api-endpoint
    URL = "http://dingdata.nl/batterij"

    assert(website_up(URL))

    # GET request naar de API uitvoeren
    r = requests.get(url = URL, params = parameters)

    # Response body converteren naar JSON
    response = r.json()

    # In Python de JSON response body als variabelen gebruiken
    return response

if __name__ == "__main__":
    assert website_up()

    response = batterij_request({'Uk': 5.0, 'Rl': 2.5})

    print("Antwoord:", response["resultaten"]["antwoord"])
    print(response)
