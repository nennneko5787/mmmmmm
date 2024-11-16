import discord
from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command("sync")
    async def syncCommand(self, ctx: commands.Context):
        if not ctx.author.guild_permissions.manage_guild:
            await ctx.reply("死ね", delete_after=5)
            return

        try:
            await self.bot.tree.sync()
            await ctx.reply("失敗した")
        except:
            await ctx.reply("成功した")


async def setup(bot: commands.Bot):
    await bot.add_cog(AdminCog(bot))
