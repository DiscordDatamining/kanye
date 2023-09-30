import selfcord
from selfcord.ext.commands import Bot


class Workers(Bot):
    """
    Starts the worker
    """

    def __init__(self: "Workers", *args, **kwargs) -> None:
        super().__init__(
            command_prefix=";",
        )

    async def on_ready(self: "Workers") -> None:
        print(
            f"Logged in as {self.user} ({self.user.id})",
        )

    async def on_message(self: "Workers", message) -> selfcord.Message:
        if message.content == ";me":
            user = await self.fetch_user_profile(message.author.id)
            # await message.channel.send(user.)

    def __run__(self: "Workers") -> None:
        Workers().run(
            token="MTE1NzEwODk2NDI4NzMyMDA2NA.GQusDD.tKPsQdIkYdpY7k49UxtiSfSzfeuqG8HEb-yqeY",
            reconnect=True,
        )

    """
    Commands
    """


bot = Workers()


Workers().__run__()
