import discord
from discord.ext import commands
from discord import app_commands


class EmbedModal(discord.ui.Modal, title="埋め込みを編集"):
    def __init__(self, *, channel: discord.TextChannel, *, user: discord.Member | None):
        super().__init__()

        self.channel = channel
        self.user = user
        self._title = discord.ui.TextInput(
            label="タイトル", placeholder="こんにちは！", required=False
        )
        self.add_item(self._title)

        self.content = discord.ui.TextInput(
            label="内容", placeholder="こんにちは！キチガイども！", required=False
        )
        self.add_item(self.content)

        self.color = discord.ui.TextInput(
            label="色",
            default="#5865F2",
            placeholder="カラーコードは自分で調べてください",
            required=True,
        )
        self.add_item(self.color)

        self.footer = discord.ui.TextInput(
            label="フッター", placeholder="省略可", required=False
        )
        self.add_item(self.footer)

        self.footerIcon = discord.ui.TextInput(
            label="フッターのアイコン", placeholder="省略可", required=False
        )
        self.add_item(self.footer)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        if not interaction.user.guild_permissions.manage_guild:
            await interaction.response.send_message(
                "こんにちは！キチガイども！", ephemeral=True
            )
            return

        embed = discord.Embed(
            title=self._title.value,
            description=self.content.value,
            colour=discord.Colour.from_str(self.color),
        )
        if self.user:
            embed.set_author(
                name=self.user.display_name, icon_url=self.user.display_avatar
            )

        await self.channel.send(embed=embed)
        await interaction.response.send_message("ok")


class EmbedCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="embed", description="埋め込みをチャンネルに送れます")
    async def embedCommand(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel = None,
        user: discord.Member = None,
    ):
        if not channel:
            channel = interaction.channel
        await interaction.response.send_modal(EmbedModal(channel=channel, user=user))


async def setup(bot: commands.Bot):
    await bot.add_cog(EmbedCog(bot))
