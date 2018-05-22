from discord.utils import find
from sys import modules

def initialize(bot):
    pass

def get_helpstr():
    return """
              kiss  <user> | Sends that user a kiss!
              clear <amt>  | Clears the channel of messages (admin req)
              github       | Posts the github link of android18.
              avatar <user>| Posts the user's avatar (or current user)
           """
async def on_kiss(android18, args, msg):
    emoji = ':kissing_heart:'
    user = msg.author
    if len(args) > 1:
        user = find(lambda m: m.mention == args[1], msg.server.members)

    await android18.send_message(msg.channel, 'Here is your kiss {} {}'.format(user.mention, emoji))

async def on_clear(android18, args, msg):
    if not msg.author.server_permissions.administrator: return
    await android18.purge_from(msg.channel, limit=int(args[1]))

async def on_git(android18, args, msg):
    await android18.send_message(msg.channel, '`My github is located at: `https://github.com/Theoretical/android18')

async def on_avatar(android18, args, msg):
    user = msg.author
    if len(args) > 1:
        user = find(lambda m: m.mention == args[1], msg.server.members)

    await android18.send_message(msg.channel, '`{} avatar is: `{}'.format(user.name, user.avatar_url))

async def on_message(android18, msg, msg_obj):
    callback_func = 'on_' + msg[0]

    if hasattr(modules[__name__], callback_func):
        await getattr(modules[__name__], callback_func)(android18, msg, msg_obj)
        return True
    return False
