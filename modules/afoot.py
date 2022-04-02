import modules.client
from telethon import events
from telethon import version
from platform import python_version

client = modules.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.afoot'))
async def runafoot(event):
    await event.delete()
    ridogramuserdetails = await event.get_sender()
    messagelocation = event.to_id
    ridogramimage = "https://telegra.ph/file/b861edafb332c473a847d.jpg"
    await client.send_file(messagelocation, ridogramimage, caption=f"Dear {ridogramuserdetails.first_name},\nI'm glad to announce that Snake Rido is able to assist you.\n\n╭─⊸ Rido Version: 0.9.1\n├─⊸ Python Version: {python_version()}\n╰─⊸ Telethon Version: {version.__version__}\n\nThank You Join @SnakeUserBot,\nRidoTeam")
