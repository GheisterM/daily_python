import requests
from os import environ
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

PX_USER = environ.get("PIXELA_USER")
PX_TOKEN = environ.get("PIXELA_TOKEN")
PX_GRAPH = environ.get("PIXELA_GRAPH")

PIXELA_ENDPOINT = "https://pixe.la/"
PROFILE_ENDPOINT = f"{PIXELA_ENDPOINT}@{PX_USER}"
CREATE_USER_ENDPOINT = f"{PIXELA_ENDPOINT}v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}v1/users/{PX_USER}/graphs/{PX_GRAPH}"
CREATE_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}v1/users/{PX_USER}/graphs"
ADD_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}v1/users/{PX_USER}/graphs/{PX_GRAPH}"
HEADERS = {
    "X-USER-TOKEN": PX_TOKEN,
}


def is_type(var, t):
    """Function to test if a var can be safely cast into a type 't'"""
    try:
        t(var)
    except ValueError:
        return False
    else:
        return True


user_exists = requests.get(PROFILE_ENDPOINT)
if user_exists.status_code != 200:
    user_data = {
        "token": PX_TOKEN,
        "username": PX_USER,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    user_response = requests.post(CREATE_USER_ENDPOINT, json=user_data)
    user_response.raise_for_status()

graph_exists = requests.get(GRAPH_ENDPOINT)
if graph_exists.status_code != 200:
    graph_data = {
        "id": PX_GRAPH,
        "name": "Job Applications",
        "unit": "CV",
        "type": "int",
        "color": "ajisai",
    }
    graph_response = requests.post(
        CREATE_GRAPH_ENDPOINT,
        json=graph_data,
        headers=HEADERS
    )
    graph_response.raise_for_status()

yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y%m%d")

amount = ""

while not is_type(amount, int):
    amount = input("How many CV you sent yesterday?: ")

pixel_data = {
    "date": yesterday_str,
    "quantity": amount
}
pixel_response = requests.post(
    ADD_PIXEL_ENDPOINT,
    json=pixel_data,
    headers=HEADERS
)

if pixel_response.status_code == 200:
    print("Data successfully recorded")
else:
    print(f"Sorry! There was an error ({pixel_response.status_code})")
