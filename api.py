import requests

def get_data_from_api(endpoint):
    url = f"https://api.frankfurter.app/{endpoint}"
    response = requests.get(url)
    return response.json()
