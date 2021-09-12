from discord.ext import commands

class Moderation(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='clear', brief='Purge a channel of messages')
  @commands.has_permissions(administrator=True)
  async def clear(self, ctx, amount=5):
    await ctx.channel.send("Clearing {0} messages!".format(amount))
    await ctx.channel.purge(limit=amount+1)

  