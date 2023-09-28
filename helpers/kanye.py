import aiohttp
import asyncpg
import discord
import redis
import websockets

from discord.ext import commands, ipc
from discord.ext.commands import AutoShardedBot
from discord.ext.tasks import loop

from .config import Auth


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
        )
