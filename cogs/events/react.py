import discord
from discord.ext import commands
import asyncio

class React(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        for owner in self.bot.owner_ids:
            if f"<@{owner}>" in message.content:
                try:
                    if owner == 1142053791781355561:
                        
                        emojis = [
                            "<a:aowner:1408876949115502664>",
                            "<:club_ban:1408877097224765480>",
                            "<:land_yildiz:1408877235271634967>",
                            "<a:a_rose:1408877320260948080>",
                            "<:land_yildiz:1408877235271634967>",
                            "<a:aalert:1408877558585622739>",
                            "<:sq_HeadMod:1408877878673805433>",
                            "<:Dc_RedCrownEsports:1408877974513520659>",
                            "<a:aGIFD:1408878060001820746>",
                            "<a:aGIFD:1408878060001820746>",
                            "<a:amax__A:1408878294299967571>",
                            "<:Heeriye:1408878430820241468>",
                            "<:heart_em:1408878523514355843>",
                            "<a:aStar:1408878603088822453>",
                            "<a:aking:1408878714959429813>",
                            "<:headmod:1408878821947478178>",
                            "<a:asg_rd:1408878919268175903>",
                            "<a:aRedHeart:1408879013459525722>",
                            " <a:astar:1408879145072722121>"
                        ]
                        for emoji in emojis:
                            await message.add_reaction(emoji)
                    else:
                        
                        await message.add_reaction("<a:aowner:1408876949115502664>")
                except discord.errors.RateLimited as e:
                    await asyncio.sleep(e.retry_after)
                    await message.add_reaction("<a:aowner:1408876949115502664>")
                except Exception as e:
                    print(f"An unexpected error occurred Auto react owner mention: {e}")
