import telegram
import time

bot = telegram.Bot(' ! ADD-TELEGRAM-TOKEN ! ')


def send_temp(temperatur):
	text_to_send = 'Aktuelle Temperatur '+str(temperatur)+ '*C'
	bot.send_message(chat_id=' ! ADDCHATID ! ', text=text_to_send) 

def get_temp():
	file = open('/path/to/w1_slave')
	filecontent = file.read()
	file.close()

	stringvalue = filecontent.split('\n')[1].split(' ')[9]
	temper = float(stringvalue[2:])/1000
	return(temper)

def start_alarm():
	print ('ALARM!')
	text_to_send = 'ALARM! Temp. auf '+str(temperatur)+ '*C'
	bot.send_message(chat_id=' ! ADDCHATID ! ', text=text_to_send)


counter = 0
sleeptimer = 60
alarm_temp = float(0.75)


while True:

	time.sleep(sleeptimer)
	temperatur = get_temp()

	if temperatur <= alarm_temp:
		sleeptimer = 5
		start_alarm()

	else:
		sleeptimer = 60
		counter = counter + 1

		if counter >= 60:
			print ("Sending Message! with Temperatur", temperatur)
			send_temp(temperatur)
			counter = 0

		else:
			print ("n0thing to do Temp is:", temperatur)
