import discord
from discord import Embed
from workers.worker.manager import Worker
from discord.ext.commands import (
    Cog,
    group,
    command,
    Context,
    has_permissions,
    Command,
    is_owner,
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

    @command(
        name="globaluserban",
        description="Global bans a user from kanye.",
        aliases=[
            "gban",
            "globalban",
            "fuckover",
            "bye",
            "boom",
        ],
    )
    @is_owner()
    async def globalban(
        self: "Developer", ctx: Context, user: discord.User | discord.Member
    ) -> None:
        """
        Developer command only.
        """
        try:
            for u in self.bot.guilds:
                for x in u.members:
                    if x.id == user.id:
                        await x.ban(reason="Don't unban | Potential Raider.")
            await ctx.send("👍")
        except Exception as e:
            print(f"Failed to ban, {e}")


async def setup(bot: Kanye):
    await bot.add_cog(Developer(bot))
