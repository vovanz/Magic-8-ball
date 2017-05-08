#!/usr/bin/env python3
import asyncio
import json
from random import randint, choice

from aiotg import Bot, Chat

from config import TG_TOKEN, WAIT_SECONDS_MIN, WAIT_SECONDS_MAX, ANSWERS

bot = Bot(api_token=TG_TOKEN)

empty_markup = {
    'keyboard': []
}
empty_markup_json = json.dumps(empty_markup)

markup = {
    'keyboard': [[
        {
            'text': 'Shake'
        }
    ]],
    'one_time_keyboard': True
}
markup_json = json.dumps(markup)


@bot.command('ping')
def ping(chat: Chat, match):
    return chat.reply('pong', markup=markup)


@bot.command('/start.*')
def start(chat: Chat, match):
    return chat.send_text(
        'Shake the ball to know your destiny',
        reply_markup=json.dumps(markup),
    )


@bot.command('Shake')
async def shake(chat: Chat, match):
    await chat.send_text('So...', reply_markup=empty_markup_json)
    await asyncio.sleep(randint(WAIT_SECONDS_MIN, WAIT_SECONDS_MAX))
    await chat.send_text(choice(ANSWERS), reply_markup=markup_json)


if __name__ == "__main__":
    bot.run()
