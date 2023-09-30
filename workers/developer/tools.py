import discord
from discord.ext.commands import (
    Cog,
    command,
    group,
)
from helpers.kanye import Kanye


async def Developer(Cog):
    """
    Developer Tasks
    """

    def __init__(self: "Developer", bot: Kanye, *args, **kwargs) -> None:
        self.bot: Kanye = bot

    @group(
        name="globalhardban",
        description="global ip bans a user from kanye.",
        aliases=[
            "ghb",
            "gb",
            "globalban",
        ],
    )
    async def globalban(
        self: "Developer", *, user: discord.User | discord.Member
    ) -> None:
        for x in self.bot.guilds:
            for u in x.members:
                if u.id == user.id:
                    try:
                        await u.ban()
                    except Exception as e:
                        pass


async def setup(bot):
    await bot.add_cog(Developer(bot))
