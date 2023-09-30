import os
from typing import Dict, List

import aiohttp
import asyncpg
import discord
import httpx
import redis
import requests
import websockets
from helpers.paginator import paginator
from aiohttp import ClientSession
from discord import Embed
from discord.ext import commands
from discord.ext.commands import (
    AutoShardedBot,
    Bot,
    Context,
)
from discord.ext.tasks import loop
from redis import StrictRedis
from requests import (
    ConnectionError,
    JSONDecodeError,
    get,
    post,
)

from helpers.config import (
    Auth,
    Color,
)


class Kanye(AutoShardedBot):
    def __init__(self: "Kanye", *agrs, **kwargs) -> None:
        super().__init__(
            command_prefix=Auth.prefix,
            help_command=None,
            intents=discord.Intents.all(),
            command_attrs=dict(hidden=True),
            strip_after_prefix=True,
            case_insensitive=True,
            max_messages=1000,
            activity=discord.Activity(
                type=discord.ActivityType.competing,
                name=" 󠁛󠀣󠀰󠀰󠀰󠀰󠀰󠀰󠀬󠀣󠀰󠀰󠀰󠀰󠀰󠀰󠁝",
            ),
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                roles=False,
                users=True,
                replied_user=False,
            ),
            owner_ids=Auth.owner_ids,
        )
        """
        Configuration
        """
        self.session: ClientSession = aiohttp.ClientSession
        self.redis = StrictRedis(
            host="localhost",
            port=6379,
            db=0,
        )

    async def __signature__(self: "Kanye") -> None:
        self.redis.set(
            name="discord",
            value="test",
        )

    def __run__(self: "Kanye") -> None:
        Kanye().run(
            token=Auth.token,
            reconnect=True,
        )

    async def get_context(self: "Kanye", message: discord.Message, *, cls=None) -> None:
        """
        Custom Context
        """
        return await super().get_context(message, cls=cls or Kanye.context)

    class context(Context):
        """
        Custom Context Class
        """

        async def approve(self: "Kanye.context", message: str) -> None:
            await self.send(
                embed=Embed(
                    color=Color.approve,
                    description=f"👍 {self.author.mention}: {message}",
                )
            )

        async def warn(self: "Kanye.context", message: str) -> None:
            await self.send(
                embed=Embed(
                    color=Color.warn,
                    description=f"🙅‍♂️ {self.author.mention}: {message}",
                )
            )

        async def error(self: "Kanye.context", message: str) -> None:
            await self.send(
                embed=Embed(
                    color=Color.warn,
                    description=f"👎 {self.author.mention}: {message}",
                )
            )

        async def normal(self: "Kanye.context", message: str) -> None:
            await self.send(
                embed=Embed(
                    color=Color.normal,
                    description=message,
                )
            )

        async def paginate(self: "Kanye.context", embeds: list, *args, **kwargs) -> None:
            await paginator(
                ctx=self,
                embeds=embeds,
            )


    async def on_ready(self: "Kanye") -> None:
        await self.load_extension("jishaku")
        for root, dirs, files in os.walk("workers"):
            for filename in files:
                if filename.endswith(".py"):
                    cog = os.path.join(root, filename)[:-3].replace(os.sep, ".")
                    try:
                        await self.load_extension(cog)
                        print(f"{cog} has been granted")
                    except:
                        pass

