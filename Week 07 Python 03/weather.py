import requests
import pycountry
from pprint import pprint

API_KEY = "f706f3671d08ae2abef33c87ca9b6294"

def get_country_code(country_name):
    """
    Takes a country name as input and returns the corresponding two-letter country code.
    """
    country_name = country_name.lower()
    
    # Map shorthand country names to full country names
    shorthand_names = {
        "uk": "united kingdom",
        "gb": "great britain",
        "usa": "united states of america",
        "uae": "united arab emirates",
        "hk": "hong kong",
        "prc": "people's republic of china",
        "s.korea": "south korea",
        "s korea": "south korea"
    }
    if country_name in shorthand_names:
        country_name = shorthand_names[country_name]
    
    try:
        country_code = pycountry.countries.search_fuzzy(country_name)[0].alpha_2
        return country_code.lower()
    except LookupError:
        print(f"Could not find country code for {country_name}")
        return ""

city = input('Enter city: ')
country = input('Enter country: ')

country_code = get_country_code(country)

if not country_code:
    print("Please enter a valid country name or code")
else:
    base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city},{country_code}&units=metric"

    weather_data = requests.get(base_url).json()

    pprint(weather_data)