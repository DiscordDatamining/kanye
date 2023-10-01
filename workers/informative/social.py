from discord.ext.commands import (
    Cog,
    command,
    group,
    Context,
)
from discord import Embed
from helpers.core.models import InstagramModel
from helpers.kanye import Kanye
from helpers.config import Color


class Socials(Cog):
    """
    Socials cog
    """

    def __init__(self: "Socials", bot: Kanye, *args, **kwargs) -> None:
        self.bot: Kanye = bot

    @group(
        name="instagram",
        description="Get info on a user.",
        aliases=[
            "ig",
            "insta",
            "gram",
        ],
        invoke_without_command=True,
    )
    async def instagram(self: "Socials", ctx: Context, username: str) -> None:
        """
        Gets user information on a instagram user.
        Use ,instagram <username> (flags)
        """
        async with ctx.typing():
            data = self.bot.cache.get(f"instagram_user_info:{username}")
            if data:
                user = data
                await ctx.send(
                    embed=Embed(
                        color=Color.normal,
                        title=(
                            f"{user['full_name'] if user['full_name'] else user['username']} ({user['username']})"
                        ),
                        url=f"https://instagram.com/{username}",
                    )
                    .add_field(
                        name="**Posts**",
                        value=(f"{user['edge_owner_to_timeline_media']['count']:,}"),
                    )
                    .add_field(
                        name="**Mutual**",
                        value=(f"{user['edge_mutual_followed_by']['count']:,}"),
                    )
                    .add_field(
                        name="**Followers**",
                        value=(f"{user['edge_followed_by']['count']:,}"),
                    )
                    .add_field(
                        name="**Following**",
                        value=(f"{user['edge_follow']['count']:,}"),
                        inline=True,
                    )
                    .set_thumbnail(url=user["profile_pic_url_hd"])
                )
            else:
                user = InstagramModel().get_user(
                    username=username,
                )
                if user is None:
                    return await ctx.error(
                        "That **user** does not exist on instagram.",
                    )
                self.bot.cache[f"instagram_user_info:{username}"] = user
                await ctx.send(
                    embed=Embed(
                        color=Color.normal,
                        title=(
                            f"{user['full_name'] if user['full_name'] else user['username']} ({user['username']})"
                        ),
                        url=f"https://instagram.com/{username}",
                    )
                    .add_field(
                        name="**Posts**",
                        value=(f"{user['edge_owner_to_timeline_media']['count']:,}"),
                    )
                    .add_field(
                        name="**Mutual**",
                        value=(f"{user['edge_mutual_followed_by']['count']:,}"),
                    )
                    .add_field(
                        name="**Followers**",
                        value=(f"{user['edge_followed_by']['count']:,}"),
                    )
                    .add_field(
                        name="**Following**",
                        value=(f"{user['edge_follow']['count']:,}"),
                        inline=True,
                    )
                    .set_thumbnail(url=user["profile_pic_url_hd"])
                )

    @instagram.command(
        name="posts",
        description="Gets a user's recent post or posts.",
        aliases=["p"],
    )
    async def posts(
        self: "Socials",
        ctx: Context,
        username: str,
    ) -> None:
        """
        fetch and display the most recent posts made by a user.
        Amount -> This parameter specifies the number of posts to retrieve.
        """


async def setup(bot):
    await bot.add_cog(Socials(bot))
