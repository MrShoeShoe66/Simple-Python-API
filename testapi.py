import urllib.request
import urllib.error
import json

def get_data_from_api(url):
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()
            return json.loads(data)
    except urllib.error.URLError as e:
        print("Error occurred:", e)
        return None

# Ask the user for the API URL
api_url = input("Enter the API URL: ")

# Get data from the API
data = get_data_from_api(api_url)

if data:
    print("Received data from the API:")
    print(data)
