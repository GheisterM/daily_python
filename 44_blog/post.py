import requests

BLOGS_URL = 'https://api.npoint.io/c790b4d5cab58020d391'


class Post:

    def __init__(self) -> None:
        blogs_req = requests.get(BLOGS_URL)
        blogs_req.raise_for_status()
        self.all_posts: list[dict] = blogs_req.json()

    def get_blog(self, index):
        for post in self.all_posts:
            if post['id'] == index:
                return post
