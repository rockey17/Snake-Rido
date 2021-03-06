from telethon import events
import modules.client
from telethon.tl.functions.users import GetFullUserRequest
from os import remove

client = modules.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.dls'))
async def rundls(event):
    await event.delete()
    getinformation = await event.get_reply_message()
    targetid = getinformation.sender_id
    targetdetails = await client(GetFullUserRequest(targetid))
    messagelocation = event.to_id
    client.parse_mode = "html"
    try:
        userimage = await client.download_profile_photo(f"@{targetdetails.users[0].username}")
        await client.send_file(messagelocation, userimage, caption=f"š¤ Firstname: {targetdetails.users[0].first_name}\nš¤ Lastname: {targetdetails.users[0].last_name}\nš Username: @{targetdetails.users[0].username}\nš User ID: {targetdetails.users[0].id}\nāļø Phone Number: {targetdetails.users[0].phone}\nš User Link: <a href='tg://user?id={targetid}'>Profile</a>\nš Bio: {targetdetails.full_user.about}\nš Data Center ID: {targetdetails.users[0].photo.dc_id}\nš¤ Bot: {targetdetails.users[0].bot}\nš„ Mutual Groups: {targetdetails.full_user.common_chats_count}\nš« Blocked: {targetdetails.full_user.blocked}")
        remove(userimage)
    except:
        pass