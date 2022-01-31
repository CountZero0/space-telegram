import argparse
import os
from random import choice
import time

from environs import Env
import telegram


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image-dir', help='Path to images folder', default='./images')
    return parser.parse_args()


def send_images_to_telegram(token, chat_id, interval):
    bot = telegram.Bot(token=token)
    while True:
        photo = choice(os.listdir('images'))
        with open(f'images/{photo}', 'rb') as image:
            bot.send_photo(chat_id=chat_id, photo=image)
        time.sleep(interval)


if __name__ == '__main__':
    env = Env()
    env.read_env()

    tg_bot_token = env.str('TG_BOT_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    posting_interval = env.int('POSTING_INTERVAL')

    send_images_to_telegram(tg_bot_token, tg_chat_id, posting_interval)
