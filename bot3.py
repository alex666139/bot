import pyowm
import telebot
owm = pyowm.OWM('03afb3cf29c26cfcc3b9a347b709d308', language = "ru")
token = '1047274592:AAEMt-3Fh0y-55Ao1lmp8qKDLay-sT-HGjk' # токен бота 
bot= telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет,я подскажу тебе какая сейчас погода),просто напиши название города! ")


@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']

	answer = " В городе " + message.text + " сейчас " + w.get_detailed_status()
	answer += " Температура сейчас в районе " + str(temp)+ "\n\n"


	if temp < -0:
		answer += "сейчас топ по зимнему:-)"
	elif temp < -10:
		answer += "ещё даже тепло)"
	elif temp < -20:
		answer += "холодно но жить можно("
	elif temp < -30:
		answer +=  "там слишком холодно сиди дома)"
	else:
		answer += "ну наверно там лето уже так что думай сам)"

	bot.send_message(message.chat.id, answer)


bot.polling()


