from django.core.management.base import BaseCommand
from django.conf import settings
from foodapp1 import views
from foodapp1.models import Location, Type, Basket, Product, Purchase, ProductService
from telebot import TeleBot
from telebot import types
import os


# Объявление переменной бота
# bot = TeleBot(settings.TOKEN)
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  # markup.__delattr__()
  item1 = types.KeyboardButton('Список продуктов')
  markup.add(item1)
  bot.send_message(message.chat.id, "Привет, собираешься за продуктами?", reply_markup=markup)
  # bot.send_message(message.chat.id, "Привет, собираешься за продуктами?")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

  message.text = message.text.lower()
  if "список" in message.text  or message.text == "/get_list":
    products_list = Product.objects.filter(necessity=True)
    purchases_list = Purchase.objects.all()
    purchases_names_list = []
    for purchase in purchases_list:
        purchases_names_list.append(purchase.name.name)
    for product in products_list:
        if product.name not in purchases_names_list:
            product_name = Product.objects.get(name=product.name)
            product_number = 1
            product_comment = ""
            try:
                if Basket.objects.get(name=product_name, number=product_number, comment=product_comment):
                    continue
            except Exception:
                Basket.objects.create(name=product_name, number=product_number, comment=product_comment)
    all_basket_products = Basket.objects.all()
    message_list = ''
    for basket_product in all_basket_products:
      product_str = f"- {basket_product.name.name} {basket_product.number}шт {'['+basket_product.comment+']' if basket_product.comment else '' }\n"
      message_list += product_str
      
    bot.send_message(message.from_user.id, message_list)

  elif "привет" in message.text or message.text == "/hello":
    bot.send_message(message.chat.id, "Привет, собираешься за продуктами, дружок?")
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши: Список")
  else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def remind(message):
  bot.send_message(message.chat.id, "Пора пополнить список продуктов!")
  

class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        print("Starting TG bot ...")
        bot.polling(none_stop=True, interval=0)
