from .adamondra import AdamOndra


def setup(bot):
    bot.add_cog(AdamOndra(bot))