import requests
import json
api_url = "https://restcountries.com/v3.1/all"
with open("api_countries_untrimmed.txt", "w", encoding="utf-8") as f:
    response = requests.get(api_url)
    print(response)
    written_response = response.text
    f.write(written_response)


