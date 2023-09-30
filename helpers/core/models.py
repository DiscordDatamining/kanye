import redis
import requests
import selenium
from json import JSONDecodeError
from requests import get, post
from helpers.kanye import Kanye
from helpers.config import Auth


class InstagramModel:
    """
    Instagram Models
    """

    def __init__(self: "InstagramModel", *args, **kwargs) -> None:
        ...

    def get_user(
        self: "InstagramModel",
        username: str,
        *args,
        **kwargs,
    ) -> None:
        try:
            r = get(url=Auth.api.url.replace("{username}", username))
            if r.status_code == 404:
                return None
            user_data = r.json()["graphql"]["user"]
            return user_data
        except JSONDecodeError:
            return None
