import discord
from discord.ext import commands


class JoinCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(member: discord.Member):
        embed = discord.Embed(
            title=f"ようこそ{member.guild.name}へ",
            description=f"ようこそ！{member.mention} さんは{len(member.guild.members)}人目の参加者です",
            colour=discord.Colour.gold(),
        ).set_thumbnail(url=member.display_avatar)
        await member.guild.get_channel(1307298953586544681).send(
            member.mention, embed=embed
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(JoinCog(bot))
