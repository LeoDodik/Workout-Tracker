import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "s123s312"
TOKEN = "kss123s2"
NEW_TOKEN = "ks21122s13"

# Creating a user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}



# Posting data to the graph
pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today = datetime.now()



graph_pixel_post = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"

}

pixel_put_request = {
    "newToken": NEW_TOKEN
}

delete_endpoint = f"/v1/users{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)