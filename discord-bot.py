import discord
from re import compile
from re import match
from re import sub
from discord.ext import commands
from json import load

bot = commands.Bot(command_prefix='?')


def check_pattern(msg):
    pattern = compile('^\[\[(.+?)\]\]$')
    if pattern.match(msg) is not None:
        return sub(pattern, r'\1', msg)


def search_json(itemname):
    with open('UniqueItemsList.json', 'r') as itemlist:
        for item in load(itemlist):
            if item['name'] == itemname:
                return item


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(message):
    itemname = check_pattern(message.content)
    if itemname:
        item = search_json(itemname)
        embed = discord.Embed(title=item['name'], colour=11493413)
        if item['hasBasemods']:
            mods = '\n'.join(item['basemod'])
            embed.add_field(name='Implicit mods', value=mods, inline=False)
        mods = '\n'.join(item['affixmods'])
        embed.add_field(name='Affix mods', value=mods, inline=False)
        embed.set_image(url=item['itemimage'])
        await message.channel.send(embed=embed)


if __name__ == '__main__':
    bot.run('NDQ1OTQzMDczMTE4MjI0Mzg1.DdyE9A._XONveg0VaAEAobnYWYylGxrLSs')