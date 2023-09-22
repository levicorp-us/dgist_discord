import os
import lightbulb
import hikari

from main_bot import GUILD_ID, _token

bot = lightbulb.BotApp(
    token = _token,
    prefix="!",
    default_enabled_guilds=GUILD_ID,
    intents = hikari.Intents.ALL
)

# bot.load_extensions('extensions.example') # specific extensions available
bot.load_extensions_from('./extensions') # add extensions in the dir

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()
    
    bot.run()