from dotenv import load_dotenv
from os import getenv
from vkbottle.bot import Bot

load_dotenv()

TOKEN = getenv("VK_TOKEN")

bot = Bot(TOKEN)

from app.vk.handlers.start import labeler

bot.labeler.load(labeler)

if __name__ == "__main__":
    bot.run()
