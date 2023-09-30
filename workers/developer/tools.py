from discord import Embed
from workers.worker.manager import Worker
from discord.ext.commands import (
    Cog,
    group,
    command,
    Context,
    has_permissions,
    Command,
    Group,
)
import asyncio
from helpers.kanye import Kanye


class Developer(Cog):
    """
    Developer Tasks
    """

    def __init__(self: "Developer", bot: Kanye, *args, **kwargs) -> None:
        self.bot: Kanye = bot


async def setup(bot: Kanye):
    await bot.add_cog(Developer(bot))
