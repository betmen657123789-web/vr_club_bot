from dotenv import load_dotenv
from os import getenv
from vkbottle.bot import Bot
from app.vk.handlers.start import labeler as start_labeler
from app.vk.handlers.status import labeler as status_labeler
from app.vk.handlers.about import labeler as about_labeler
from app.vk.handlers.booking import labeler as booking_labeler
from app.vk.handlers.faq import labeler as faq_labeler
from app.vk.handlers.prices import labeler as prices_labeler

load_dotenv()

TOKEN = getenv("VK_TOKEN")

bot = Bot(TOKEN)
from app.vk.handlers.start import labeler as start_labeler
from app.vk.handlers.status import labeler as status_labeler

bot.labeler.load(start_labeler)
bot.labeler.load(status_labeler)
bot.labeler.load(start_labeler)
bot.labeler.load(status_labeler)
bot.labeler.load(about_labeler)
bot.labeler.load(booking_labeler)
bot.labeler.load(faq_labeler)
bot.labeler.load(prices_labeler)

from app.vk.handlers.start import labeler


bot.labeler.load(labeler)

if __name__ == "__main__":
    bot.run_forever()
