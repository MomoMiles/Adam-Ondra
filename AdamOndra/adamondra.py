from redbot.core import checks, Config
from redbot.core.i18n import Translator, cog_i18n
import discord
from redbot.core import commands
from redbot.core.utils import mod
import asyncio
import datetime

class adamondra(commands.Cog):
    """The Adam Ondra Cog"""

    def __init__(self, bot):
        self.bot = bot
        default_member = {
            "Name": None,
            "Age": None,
            "Location": None,
            "About": None,
            "Gender": None,
            "PB": None,
            "Reddit": None,
            "Other": None,
            "Avatar": None
        }
        default_guild = {
            "db": []
        }

        self.config = Config.get_conf(self, identifier=42)
        self.config.register_guild(**default_guild)
        self.config.register_member(**default_member)

    @commands.command(name="signup")
    @commands.guild_only()
    async def signup(self, ctx):
        """Signup as a climber!"""

        server = ctx.guild
        user = ctx.author
        db = await self.config.guild(server).db()
        if user.id not in db:
            db.append(user.id)
            await self.config.guild(server).db.set(db)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:", value="You have officially created your climbing profile for **{}**, {}.".format(server.name, user.mention))
            await ctx.send(embed=data)
        else: 
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Opps, it seems like you already have a climbing profile, {}.".format(user.mention))
            await ctx.send(embed=data)

    @commands.command(name="unsignup")
    @commands.guild_only()
    async def unsignup(self, ctx):
        "Removes account"
        server = ctx.guild
        user = ctx.author
        db = await self.config.guild(server).db()
        if user.id in db:
            db.delete(user.id)
        else:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:Warning",value="Oops, seems like you're trying to delete an account you don't have.")
            await.ctx.send(embed=data)


