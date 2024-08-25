#!/usr/bin/python.
import os
import asyncio
import uuid
from Database.db import insert_user, get_uuid
from telebot.async_telebot import AsyncTeleBot

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
BOT_TOKEN = os.environ.get('BOT_TOKEN')
SERVER_URL = os.environ.get('SERVER_URL')

if (BOT_TOKEN is None):
    exit("Error: BOT_TOKEN is not set")

bot = AsyncTeleBot(BOT_TOKEN)

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am a bot resultant of an assignment for intern at "AageBot".\n\nUse \'/create\' command to create a UUID from your Telegram ID.\n\nYou can validate the user Id by using the /link command.\n\nUse \'/link\' command to get your link.\n\nUse \'/echo\' command to echo your message.\n\n This bot is created by Abhishek Singh Kushwaha. For more details, visit https://ask-03-portfolio.vercel.app/'
    await bot.reply_to(message, text)

@bot.message_handler(commands=['create'])
async def create(message):
    user_id = message.from_user.id
    if (get_uuid(user_id) is not None):
        return await bot.reply_to(message, f'You have already generated a link. Your link: {SERVER_URL}/link/{get_uuid(user_id)}')
    
    unique_id = str(uuid.uuid4())
    insert_user(unique_id, user_id)
    
    link = f'{SERVER_URL}/link/{unique_id}'
    await bot.reply_to(message, f'Your link: {link}')

@bot.message_handler(commands=['link'])
async def link(message):
    await bot.reply_to(message, f'Your link: {SERVER_URL}/link/{get_uuid(message.from_user.id)}')

@bot.message_handler(commands=['echo'])
async def echo_message(message):
    await bot.reply_to(message, message.text[6:])


asyncio.run(bot.polling())