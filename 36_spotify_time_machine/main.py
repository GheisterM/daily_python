import urllib.parse
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dotenv import load_dotenv
from os import environ
import urllib
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = environ.get("CLIENT_ID")
CLIENT_SECRET = environ.get("CLIENT_SECRET")
REDIRECT_URI = environ.get("REDIRECT_URI")
USERNAME = environ.get("USERNAME")


def is_date(date_str: str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return False
    else:
        return True


date = "2000-08-12"
while not is_date(date):
    date = input("Which date do you want to travel to? Type the date in the format YYYY-MM-DD: ")

response = requests.get(URL + date)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")

items = soup.select("li ul li")
items = [item for item in items
         if item.find(name="h3") is not None
         and item.find(name="span") is not None]
titles = [item.find(name="h3") for item in items]
titles = [title.get_text().strip() for title in titles]
artists = [item.find(name="span") for item in items]
artists = [artist.getText().strip() for artist in artists]

client = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="token.txt",
        username=USERNAME,
        show_dialog=True
    )
)
user_id = client.current_user()["id"]

tracks_uri = list[str]()
for i in range(len(titles)):
    query = f"track:{titles[i]} artist:{artists[i]}"
    track = client.search(q=query, limit=1, type="track")
    try:
        uri = track["tracks"]["items"][0]["uri"]
        tracks_uri.append(uri)
    except IndexError:
        pass

tracks_uri = tracks_uri[::-1]

playlist_name = date + " Billboard 100"
playlist = client.user_playlist_create(user_id, playlist_name, public=False)
playlist_id = playlist["id"]

client.playlist_add_items(playlist_id, tracks_uri)
