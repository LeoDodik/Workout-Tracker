from datetime import datetime
import requests
import base64

# Placeholder values for API keys and sensitive data
SHEETY_URL = "https://api.sheety.co/YOUR_SHEET_ID/workouts"  # Replace with your SHEETY URL
APP_ID = "YOUR_APP_ID"  # Replace with your Nutritionix App ID
API_KEY = "YOUR_API_KEY"  # Replace with your Nutritionix API Key

# Headers for Nutritionix API
headers_one = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Get exercise input from the user
exercise_input = input("What have you done today? ")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": exercise_input,
}

# Send request to Nutritionix API
response = requests.post(exercise_endpoint, json=parameters, headers=headers_one)
result = response.json()

# Get current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Prepare data to be sent to Sheety
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# Placeholder values for SHEETY authentication
auth_username = "YOUR_USERNAME"  # Replace with your SHEETY username
auth_password = "YOUR_PASSWORD"  # Replace with your SHEETY password

# Authentication with Basic Authentication
auth_string = f"{auth_username}:{auth_password}"
auth_bytes = auth_string.encode('ascii')
base64_bytes = base64.b64encode(auth_bytes)
base64_auth_string = base64_bytes.decode('ascii')
headers_auth = {
    "Authorization": "Basic " + base64_auth_string
}

# Send data to SHEETY
if response.status_code == 200:
    sheet_response = requests.post(SHEETY_URL, json=sheet_inputs, headers=headers_auth)
    print(sheet_response.text)
else:
    print("Request failed with status code:", response.status_code)

# Print sheet_response if necessary (keep in mind it may raise an error if request failed)
