import selfcord
from selfcord.ext.commands import Bot


class Workers(selfcord.Client):
    """
    Starts the worker
    """

    def __init__(self: "Workers", *args, **kwargs) -> None:
        super().__init__()

    async def on_ready(self: "Workers") -> None:
        print(
            f"Logged in as {self.user} ({self.user.id})",
        )

    def __run__(self: "Workers") -> None:
        Workers().run(
            token="MTE1NzEwODk2NDI4NzMyMDA2NA.GL6rnF.V_pwwsEXop52UfSfOcuJ9QH7TP-Liz27ygLFOY",
            reconnect=True,
        )


bot = Workers()


# Workers().__run__()
