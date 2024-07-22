from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
SAVE_PATH = "35_top_100_movies/movies.txt"

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
headings = soup.find_all(name="h3", class_="title")
movies = [heading.getText() for heading in headings]
movies = movies[::-1]

with open(SAVE_PATH, mode="w") as file:
    file_content = "\n".join(movies)
    file.write(file_content)
