#Install and import the requests module (if available) and use it to fetch data from "https://api.github.com" .
# Solution==>

import requests
response = requests.get("https://api.github.com")  # Send a GET request to the specified URL

print(response.json())  # Print the JSON content of the response
