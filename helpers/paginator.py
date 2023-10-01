import discord
import asyncio


async def paginator(ctx, embeds):
    page = 0
    max_pages = len(embeds) - 1

    message = await ctx.send(embed=embeds[page])

    reactions = [
        "⏪",
        "⬅️",
        "➡️",
        "⏩",
        "🔍",
    ]

    for reaction in reactions:
        await message.add_reaction(reaction)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reactions

    while True:
        try:
            reaction, user = await ctx.bot.wait_for(
                "reaction_add", timeout=60, check=check
            )

            if str(reaction.emoji) == "➡️" and page < max_pages:
                page += 1
            elif str(reaction.emoji) == "⬅️" and page > 0:
                page -= 1
            elif str(reaction.emoji) == "🔍":
                await ctx.normal(
                    f"🔎 {ctx.author.mention}, What page would you like to go to?"
                )
                response = await ctx.bot.wait_for(
                    "message", timeout=30, check=lambda m: m.author == ctx.author
                )

                try:
                    target_page = int(response.content)
                    if 0 <= target_page <= max_pages:
                        page = target_page
                    else:
                        await ctx.error(
                            f"Invalid page number. Please enter a number between 0 and {max_pages}."
                        )
                except ValueError:
                    await ctx.error(f"Please enter a valid number.")

            elif str(reaction.emoji) == "⏪":
                page = 0
            elif str(reaction.emoji) == "⏩":
                page = max_pages

            await message.edit(embed=embeds[page])
            await message.remove_reaction(reaction, ctx.author)

        except asyncio.TimeoutError:
            break
