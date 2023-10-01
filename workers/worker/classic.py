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


class Classic(Cog):
    """
    Worker cog (Classic)
    """

    def __init__(self: "Classic", bot: Kanye, *args, **kwargs) -> None:
        self.bot: Kanye = bot

    class buttons:
        ...

    @command(
        name="help",
        description="See help information about a command.",
        aliases=["h"],
    )
    async def help(
        self: "Classic",
        ctx: Context,
        *,
        cmd: str = None,
    ) -> None:
        """
        Use the ,help `(command)` to view information on a command.
        If you're stuck on a command or it isnt showing, please [`Check here`](https://discord.gg/dui).
        """
        if not cmd:
            return await ctx.normal(
                "Click [here](https://kanye.creepy.sh/) to visit my discord."
            )

        command_or_group = self.bot.get_command(cmd)

        if not command_or_group:
            return await ctx.warn(
                f"No command or group called *[`{cmd}`](https://kanye.creepy.sh)* was found in my utilities."
            )

        if isinstance(command_or_group, Group):
            subcommands = command_or_group.commands
            if subcommands:
                embeds = []
                for subcommand in subcommands:
                    embed = Embed(
                        color=0x2B2D31,
                        title=f"Subcommand: {subcommand.name}",
                        description=f"aliases: {', '.join(subcommand.aliases) if subcommand.aliases else 'no aliases provided'}"
                        + (
                            "\n"
                            f"{subcommand.description or '*no description provided*'}\n"
                            f"\n{f'*{subcommand.help}*' or '*no help menu provided*'}"
                        ),
                    )
                    embeds.append(embed)

                await ctx.paginate(embeds=embeds)
            else:
                embed = Embed(
                    color=0x2B2D31,
                    title=f"Group: {command_or_group.name}",
                    description=f"aliases: {', '.join(command_or_group.aliases) if command_or_group.aliases else 'no aliases provided'}"
                    + (
                        "\n"
                        f"{command_or_group.description or '*no description provided*'}\n"
                        f"\n{f'*{command_or_group.help}*' or '*no help menu provided*'}"
                    ),
                )
                await ctx.send(embed=embed)
        elif isinstance(command_or_group, Command):
            embed = Embed(
                color=0x2B2D31,
                title=f"Command: {command_or_group.name}",
                description=f"aliases: {', '.join(command_or_group.aliases) if command_or_group.aliases else 'no aliases provided'}"
                + (
                    "\n"
                    f"{command_or_group.description or '*no help menu provided*'}\n"
                    f"\n{f'*{command_or_group.help}*' or '*no help menu provided*'}"
                ),
            )
            await ctx.send(embed=embed)

    @group(
        name="worker",
        description="Initialize the worker account.",
        invoke_without_command=True,
    )
    async def worker(
        self: "Classic",
        ctx: Context,
    ) -> None:
        ...

    @worker.command(
        name="join",
        description="Adds the worker account to the guild.",
    )
    @has_permissions(manage_guild=True)
    async def join(
        self: "Classic",
        ctx: Context,
    ) -> None:
        """
        Automatically adds the worker account to the guild.
        The worker account tracks:
            Members, Profile Connections,
            Spotify, Reactions, Messages,
            Channel Activity & 3 Others.
        """
        for x in ctx.guild.members:
            if x.id == 1157108964287320064:
                return await ctx.error(
                    "Worker account is already here!",
                )
        reactions = [
            "⏩",
            "3️⃣",
            "2️⃣",
            "1️⃣",
        ]
        for reaction in reactions:
            await ctx.message.add_reaction(reaction)
        message = await ctx.send(
            embed=Embed(
                title="Worker Task Started.",
                description="*Please wait while the worker account joins the guild.*",
                color=0x2B2D31,
            )
        )
        data = Worker(
            guild_id=ctx.guild.id,
            worker_id=1157108964287320064,
        ).__add_worker__()
        await message.edit(
            embed=Embed(
                title="Worker Account Joined.",
                description="The worker account joined successfully, you can use more commands with it by doing `!help`\n\n"
                + (
                    "Please note that this is a beta feature and bugs may happen..\nplease be gentle with it.\n"
                    f"**Worker Account Information**: <@1157108964287320064> (`1157108964287320064`)."
                ),
                color=0x2B2D31,
            )
        )


async def setup(bot):
    await bot.add_cog(Classic(bot))
