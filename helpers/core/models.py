import redis
import requests
import selenium
from requests import get, post

from helpers.config import Auth


class InstagramModel:
    """
    Instagram Models
    """

    def __init__(self: "InstagramModel", *args, **kwargs) -> None:
        InstagramModel()

    def get_user(
        self: "InstagramModel",
        username: str,
        *args,
        **kwargs,
    ) -> None:
        r = get(url=Auth.api.url.replace("{username}", username))
        return r.json()["graphql"]["user"]
