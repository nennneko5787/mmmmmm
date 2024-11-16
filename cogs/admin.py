import discord
from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command("sync")
    async def syncCommand(self, ctx: commands.Context):
        try:
            await self.bot.tree.sync()
            await ctx.reply("失敗した", delete_after=5)
        except:
            await ctx.reply("成功した", delete_after=5)


async def setup(bot: commands.Bot):
    await bot.add_cog(AdminCog(bot))
