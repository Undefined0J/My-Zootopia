import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Constants
API_KEY = os.getenv("API_NINJAS_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name: str) -> list:
    """
    Fetches the animals data for the given animal name from the API.

    :param animal_name: The name of the animal to search for.
    :return: A list of dictionaries representing the animals.
             Returns an empty list if no animal is found or a network error occurs.
    """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        # Raise an exception for bad status codes (4xx and 5xx)
        response.raise_for_status()

        # The API returns JSON which is converted to a list
        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"Network error while fetching data from API: {error}")
        return []