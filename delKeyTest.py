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

# Get data from the API
newKey = get_data_from_api("http://localhost/../newKey?auth=Password123!")
print(newKey)
delKey = get_data_from_api("http://localhost/../delKey?auth=Password123!&del="+newKey['New Key'])
data = get_data_from_api("http://localhost?key="+newKey['New Key'])

if data:
    print("Received data from the API:")
    print(data)
    print("Failed to delete key")
