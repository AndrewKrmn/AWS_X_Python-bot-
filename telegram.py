import telebot
from telebot import types
import subprocess
TOKEN = "6638546286:AAFzOf97GmLtdT3AqKcAOpU46qOgWBaRJQM"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Створити Контейнер")
    item2 = types.KeyboardButton("Запустити Контейнер")
    item3 = types.KeyboardButton("Зупинити Контейнер")
    item4 = types.KeyboardButton("Запустити(після зупинки) Контейнер")
    item5 = types.KeyboardButton("Видалити Контейнер")
    markup.add(item1, item2, item3,item4,item5)
    bot.send_message(
        message.chat.id, "Вибери операцію на AWS Instance:", reply_markup=markup
    )
@bot.message_handler(func=lambda message: message.text == "Створити Контейнер")
def create_cont(message):
    commands = "touch Dockerfile"
    kaka = subprocess.run(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    commands1 = "echo FROM httpd:latest >> Dockerfile && echo EXPOSE 80 >> Dockerfile && docker build -t telebot_python:v1 ."
    kaka1 = subprocess.run(commands1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    response_message = ("Контейнер успішно створено!\n",
    "Команда видала:\n" + kaka1.stdout +
    "\nПомилка:\n" + kaka1.stderr +
    "\nВихідний код: " + str(kaka1.returncode))
    bot.send_message(message.chat.id,response_message)
@bot.message_handler(func=lambda message: message.text == "Запустити Контейнер")
def run_cont(message):
    commands1 = "docker run -d -p 80:80 --name my-apache telebot_python:v1"
    kaka1 = subprocess.run(commands1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    response_message = ("Контейнер успішно запущено!\n",
    "Команда видала:\n" + kaka1.stdout +
    "\nПомилка:\n" + kaka1.stderr +
    "\nВихідний код: " + str(kaka1.returncode))
    bot.send_message(message.chat.id,response_message)
@bot.message_handler(func=lambda message: message.text == "Зупинити Контейнер")
def stop_cont(message):
    commands1 = "docker stop my-apache"
    kaka1 = subprocess.run(commands1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    response_message = ("Контейнер успішно зупинено!\n",
    "Команда видала:\n" + kaka1.stdout +
    "\nПомилка:\n" + kaka1.stderr +
    "\nВихідний код: " + str(kaka1.returncode))
    bot.send_message(message.chat.id,response_message)
@bot.message_handler(func=lambda message: message.text == "Запустити(після зупинки) Контейнер")
def again_cont(message):
    commands1 = "docker start my-apache"
    kaka1 = subprocess.run(commands1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    response_message = ("Контейнер успішно запущено знову!\n",
    "Команда видала:\n" + kaka1.stdout +
    "\nПомилка:\n" + kaka1.stderr +
    "\nВихідний код: " + str(kaka1.returncode))
    bot.send_message(message.chat.id,response_message)
@bot.message_handler(func=lambda message: message.text == "Видалити Контейнер")
def del_cont(message):
    commands1 = "docker rm -f my-apache"
    kaka1 = subprocess.run(commands1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    response_message = ("Контейнер успішно видалено!\n",
    "Команда видала:\n" + kaka1.stdout +
    "\nПомилка:\n" + kaka1.stderr +
    "\nВихідний код: " + str(kaka1.returncode))
    bot.send_message(message.chat.id,response_message)




bot.infinity_polling()
