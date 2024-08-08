
import telebot
import os

Token = "7050512604:AAHXyxuimWSS3JxFwasxCae5jaNsIH8dl3I"

bot = telebot.TeleBot(Token)


@bot.message_handler(['start'])
def start(message):
    
    bot.reply_to(message, "fuck yourself")
    
@bot.message_handler(['help'])
def help(message):
    
    bot.reply_to(message, "what help can we provide like 1) services 2)customer calling")
    
@bot.message_handler(commands=['video'])
    
def send_video(message):
    # Replace 'VIDEO_LINK' with the actual link of the video you want to send
    video_link = 'https://www.youtube.com/watch?v=OzI9M74IfR0'
    bot.send_message(message.chat.id, f"Here is the video link: {video_link}")

bot.polling()
