import redis
import requests
import selenium
from aiohttp import (
    ClientConnectionError,
    ClientSession,
)
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

    async def get_user(
        self: "InstagramModel",
        username: str,
        *args,
        **kwargs,
    ) -> None:
        try:
            async with ClientSession() as r:
                async with r.get(url=Auth.api.url.replace("{username}", username)) as e:
                    data = await e.json()
                    user_data = data["graphql"]["user"]
                    return user_data
        except JSONDecodeError:
            return None
