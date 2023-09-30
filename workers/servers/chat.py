from discord.ext.commands import (
    Context,
    Cog,
    command,
    group,
)
from helpers.kanye import Kanye


class Chat(Cog):
    """
    Chat commands for guilds.
    """

    def __init__(self: "Chat", bot: Kanye, *args, **kwargs) -> None:
        self.bot: Kanye = bot
