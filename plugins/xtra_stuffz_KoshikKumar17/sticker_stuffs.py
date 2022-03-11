# (c) @KoshikKumar17
import os , glob
from os import error
import pyrogram
import time
import math
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document

DLDICT = "./DOWNLOADS/"

@Koshik.on_message(filters.private & filters.command(["getsticker"]))
async def getstickerasfile(bot, message):  
    px = await message.reply_text("**Checking Sticker...🕵️**")
    await px.edit("**Validating sticker...😁**")
    if message.reply_to_message.sticker is False:
        await px.edit("**Not a Sticker File!!🥺**")
    else :
          if message.reply_to_message is None: 
               px =  await px.edit("**Reply to a Sticker File!...🙇🏻‍♂️**")       
          else :
               if message.reply_to_message.sticker.is_animated:
                   try :     
                        tx = await message.reply_text("**Downloading...🤒**")
                        file_path = DLDICT + f"{message.chat.id}.tgs"
                        await message.ropleply_to_message.download(file_path)  
                        await tx.edit("**Successfully Downloaded...✅**") 
                    #   zip_path= ZipFile.write("") if you want as zip
                        await tx.edit("**Uploading...🤧**")
                        start = time.time()
                        await message.reply_document(file_path,caption="**@KoshikKumar17**")
                        await tx.delete()   
                        os.remove(file_path)
                    #   os.remove(zip_path)
                   except Exception as error:
                        print(error)
 
               elif message.reply_to_message.sticker.is_animated is False:        
                   try : 
                       tx = await message.reply_text("**Downloading...🤒**")
                       file_path = DLDICT + f"{message.chat.id}.png"
                       await message.reply_to_message.download(file_path)   
                       await tx.edit("**Successfully Downloaded...✅**")
                       await tx.edit("**Uploading...🤧**")
                       start = time.time()
                       await message.reply_document(file_path,caption="**@KoshikKumar17**")
                       await tx.delete()   
                       os.remove(file_path)
                   except Exception as error:
                       print(error)

@Koshik.on_message(filters.private & filters.command(["clearcache"]))
async def clearcache(bot, message):   
    # Found some Files showing error while Uploading, So a method to Remove it !!  
    txt = await message.reply_text("**Checking Cache.......🕵️**")
    await txt.edit("**Clearing Cache.......🗑️**")
    dir = DLDICT
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist :
           i =1
           os.remove(f)
           i=i+1
    await txt.edit("**🙋🏻‍♂️Cleared** "+ str(i) + "File(s)") 
    await txt.delete()
    
@Koshik.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**😀The Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n **😃The Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`\n\n**@KoshikKumar17**", quote=True)
    else: 
       await message.reply("**Oops !! Not a sticker file...🤕**")


@Koshik.on_message(filters.private & filters.command(["findsticker"]))
async def findsticker(bot, message):  
  try:
       if message.reply_to_message: 
          txt = await message.reply_text("**Validating Sticker ID.....🤒**")
          stickerid = str(message.reply_to_message.text)
          chat_id = str(message.chat.id)
          await txt.delete()
          await bot.send_sticker(chat_id,f"{stickerid}")
       else:
          await message.reply_text("**Please reply to a ID to get its STICKER.**")
  except Exception as error:
        txt = await message.reply_text("**Not a Valid Sticker ID.**")
