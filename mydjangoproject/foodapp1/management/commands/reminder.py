from telebot import TeleBot
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'remind in telegram'

    def handle(self, *args, **kwargs):
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        recepient_id = os.getenv("TELEGRAM_RECEPIENT_ID")

        bot = TeleBot(bot_token)
        bot.send_message(recepient_id, 'Привет! Обнови данные о продуктах!')
