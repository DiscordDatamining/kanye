import json
import requests
from helpers.config import Auth
from requests import (
    post,
    get,
    put,
    ConnectionError,
    JSONDecodeError,
)


class Worker:
    """
    Worker account to automatically join the guild using 0auth
    """

    def __init__(
        self: "Worker", guild_id: int, worker_id: int, *args, **kwargs
    ) -> None:
        self.redirect: str = "http://127.0.0.1:8000"
        self.endpoint: str = "https://canary.discord.com/api/v9"
        self.workerID: int = worker_id
        self.guild: int = guild_id
        self.config = json.load(
            open(
                file="helpers/tokens.json",
                encoding="UTF-8",
            )
        )
        self.token: str = self.config.get("Worker")

    def __add_worker__(
        self: "Worker",
    ) -> None:
        r = put(
            url=f"{self.endpoint}/guilds/{self.guild}/members/{self.workerID}",
            json={
                "access_token": self.token,
            },
            headers={
                "Authorization": f"Bot {Auth.token}",
                "Content-Type": "application/json",
            },
        )
        if r.status_code in (201, 200, 204):
            if not "joined" in r.text:
                return {"kanye_add_error": "Couldn't add worker account to the server."}
            return {
                "status": "success",
                "worker": f"Added worker account in {self.guild}.",
            }
