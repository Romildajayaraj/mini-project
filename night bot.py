import telebot
import time
from threading import Thread
from telebot import types

checkin_active = {}

# 🔐 Replace with your actual bot token
TOKEN = "7820504483:AAGDRWNQA6TXAmcZn7oStNXQOPkyUUFKTpU"
bot = telebot.TeleBot(TOKEN)

# Set command list for the Telegram menu
bot.set_my_commands([
    types.BotCommand("start", "Start the bot"),
    types.BotCommand("help", "List available commands"),
    types.BotCommand("sos", "Trigger emergency alert"),
    types.BotCommand("location", "Share simulated location"),
    types.BotCommand("stop", "Stop auto check-in")
])

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm Night Companion. Type /help to know what I can do.")
    user_id = message.chat.id
    if not checkin_active.get(user_id):
        Thread(target=auto_checkin, args=(user_id,), daemon=True).start()

# Auto check-in logic
def auto_checkin(user_id):
    checkin_active[user_id] = True
    while checkin_active.get(user_id, False):
        bot.send_message(user_id, "⏰ Just checking in! Are you okay? Reply YES or NO.")
        time.sleep(10)  # 10 minutes

# /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
                 "Available Commands:\n"
                 "/start – Start the bot\n"
                 "/help – Show this help message\n"
                 "/sos – Send emergency alert\n"
                 "/location – Share location\n"
                 "/stop – Stop auto check-in")

# /sos command
@bot.message_handler(commands=['sos'])
def send_alert(message):
    bot.reply_to(message, f"🚨 Emergency alert sent to {emergency_contact}")

# Dummy emergency contact
emergency_contact = "9677945201", "9944738020"

@bot.message_handler(commands=['location'])
def request_location(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    location_btn = types.KeyboardButton(text="📍 Share Location", request_location=True)
    markup.add(location_btn)
    bot.send_message(message.chat.id, "Please share your location:", reply_markup=markup)
 
# /stop command
@bot.message_handler(commands=['stop'])
def stop_checkin(message):
    user_id = message.chat.id
    checkin_active[user_id] = False
    bot.send_message(user_id, "✅ Auto check-in stopped. Stay safe!")

# General text handler
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text.lower()
    if text in ["scared", "lost", "alone", "thank you"]:
        bot.reply_to(message, "Don’t worry. You're not alone. I'm here to help.")
    elif text == "yes":
        bot.reply_to(message, "Glad you're safe 😊")
    elif text == "no":
        bot.reply_to(message, "Stay calm. If needed, type /sos.")
    else:
        bot.reply_to(message, "I'm here with you. Type /help to see commands.")

# Start bot
print("🤖 Night Companion bot is now running...")
bot.polling()
