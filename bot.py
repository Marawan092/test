from pyrogram import Client, filters
Bot = Client ('Bot')
import redis
red = redis.StrictRedis(decode_responses=True) 


admin = [5571985743,2091654958]
token = "5469397024:AAFBNnPsgYyyOZgyxkoyO8a77M3O6kWeDX8"
bot = pyrogram.Pyrogram(token)
sudo = 5571985743

@bot.on_message(filers.command('انشاء الرابط'))
def start(bot, msg) :
chat_id = msg.chat.id
Text = msg.text.split(None, 1)[1]
red.hset("link",chat_id, text)
msg.reply(f"saved: (text)")

@bot.on_message(filers.command('الرابط'))
def startt(bot, msg) :
chat_id = msg.chat.id
link= red.hget("link",chat_id)
msg.reply(f"{'مفيش رابط' if link ==None else link}")

@bot.on_message(filers.command('مسح الرابط'))
def starttt(bot, msg) :
chat_id = msg.chat.id
link= red.hdel("link",chat_id)
msg.reply(تم مسح الرابط)

bot.run()
