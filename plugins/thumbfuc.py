from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb
from helper.txt import mr, AUTH_USERS

@Client.on_message(filters.private & filters.command(['viewthumb']) & filters.user(AUTH_USERS))
async def viewthumb(client,message):
    thumb = find(int(message.chat.id))[0]
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("**You dont have any custom Thumbnail**") 
		
@Client.on_message(filters.private & filters.command(['delthumb']) & filters.user(AUTH_USERS))
async def removethumb(client,message):
    delthumb(int(message.chat.id))
    await message.reply_text("**Custom Thumbnail Deleted Successfully**")
	
@Client.on_message(filters.private & filters.photo & filters.user(AUTH_USERS))
async def addthumbs(client,message):
    file_id = str(message.photo.file_id)
    addthumb(message.chat.id , file_id)
    await message.reply_text("**Your Custom Thumbnail Saved Successfully** ✅")
	
