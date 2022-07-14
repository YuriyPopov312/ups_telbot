from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import telebot
from threading import Thread
from telebot import types

Device_Status = ""
UPS_Load = ""
Puntime_Remaining = ""
Internal_Temperature = ""
Input_Voltage = ""
Output_Voltage1 = ""
Input_Frequency = ""
Output_Frequency1 = ""
Battery_Charge = ""
Battery_Voltage1 = ""

Battery_Status = ""
Battery_Voltage2 = "" 
Output_Frequency2 = ""
Output_Voltage2 = ""
Output_Current = "" 
Total_Gross_Power = "" 
Total_Active_Power = ""
Source_Power = ""
Battery_load_level = ""
Battery_Capacity = ""
Battery_Life = "" 
Main_Output = ""

def main_func():
	while True:
		global Device_Status,UPS_Load,Puntime_Remaining,Internal_Temperature,Input_Voltage,Output_Voltage1,Input_Frequency,Output_Frequency1,Battery_Charge,Battery_Voltage1,Battery_Status,Battery_Voltage2,Output_Frequency2,Output_Voltage2,Output_Current,Total_Gross_Power,Total_Active_Power,Source_Power,Battery_load_level,Battery_Capacity,Battery_Life,Main_Output
		options1 = webdriver.ChromeOptions()
		options1.add_argument('--ignore-certificate-errors')
		options1.add_argument("headless")
		browser1 = webdriver.Chrome(executable_path="C:/chromedriver.exe", chrome_options=options1)
		browser1.get('**********')
		time.sleep(1)
		username_input1 = browser1.find_element(By.NAME,'j_username')
		username_input1.clear()
		username_input1.send_keys('**********')
		time.sleep(1)
		password_input1 = browser1.find_element(By.NAME,'j_password')
		password_input1.clear()
		password_input1.send_keys('**********')
		password_input1.send_keys(Keys.ENTER)
		time.sleep(1)
		dop3 = browser1.find_element(By.XPATH,'/html/body/div[3]/div/h2[2]')
		dop3.click()
		time.sleep(1)
		dop4 = browser1.find_element(By.XPATH,'/html/body/div[3]/div/h2[3]')
		dop4.click()

		Device_Status = browser1.find_element(By.ID,'value_DeviceStatus').text
		UPS_Load = browser1.find_element(By.ID,'value_RealPowerPct').text
		Puntime_Remaining = browser1.find_element(By.ID,'value_RuntimeRemaining').text
		Internal_Temperature = browser1.find_element(By.ID,'value_InternalTemp').text
		Input_Voltage = browser1.find_element(By.ID,'value_InputVoltage').text
		Output_Voltage1 = browser1.find_element(By.ID,'value_OutputVoltage').text
		Input_Frequency = browser1.find_element(By.ID,'value_InputFrequency').text
		Output_Frequency1 = browser1.find_element(By.ID,'value_OutputFrequency').text
		Battery_Charge = browser1.find_element(By.ID,'value_BatteryCharge').text
		Battery_Voltage1 = browser1.find_element(By.ID,'value_VoltageDC').text
		
		if Device_Status == "On Line":
			Device_Status = "Подключен к сети"
		elif Device_Status =="On Line, AVR Boost Active":
			Device_Status = "Подключен к сети, в режиме повышения входного напряжения"
		elif Device_Status =="On Line, AVR Trim Active":
			Device_Status = "Подключен к сети, в режиме понижения входного напряжения"
		else:
			Device_Status = "Отключен от сети"

		print('ИБП АИИСКУЭ:\n' + Device_Status+ '\n' + UPS_Load+ ' %\n' + Puntime_Remaining+ ' минут\n' + Internal_Temperature+ '\n' + Input_Voltage+ ' эВ\n'
		 + Output_Voltage1+ ' эВ\n' + Input_Frequency+ ' Гц\n' + Output_Frequency1+ ' Гц\n' + Battery_Charge+ ' %\n' + Battery_Voltage1+ ' Постоянное напряжение\n')

		browser1.close()
		browser1.quit()

		#___________________________________________________________________________________________________________________________________________________________
		options2 = webdriver.ChromeOptions() # Устанавливаем настройки для эмулируемого браузера
		options2.add_argument('--ignore-certificate-errors')
		options2.add_argument("headless") # Режим, при котором окно браузера будет работать в фоновом режиме
		browser2 = webdriver.Chrome(executable_path="C:/chromedriver.exe", chrome_options=options2)
		browser2.get('**********')
		time.sleep(1)   
		username_input2 = browser2.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/form/div[1]/div[1]/input')
		username_input2.clear()
		username_input2.send_keys('**********')
		time.sleep(1)
		password_input2 = browser2.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/form/div[2]/div[1]/input')
		password_input2.clear()
		password_input2.send_keys('**********')
		password_input2.send_keys(Keys.ENTER)
		time.sleep(1)

		Battery_Voltage2 = browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[1]/td[2]').text #xpath не полный взятый с копии сайта на рабочем столе
		Output_Frequency2 = browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[2]/td[2]').text
		Output_Voltage2 = browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[3]/td[2]').text
		Output_Current = browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[4]/td[2]').text
		Total_Gross_Power = browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[5]/td[2]').text
		Total_Active_Power = browser2.find_element(By.XPATH,'//*[@id="ext-gen129"]/fieldset[2]/table/tbody/tr[6]/td[2]').text
		Battery_Status = browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr/td[2]').text
		Source_Power = browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]').text
		Battery_load_level = browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[3]/td[2]/table/tbody/tr/td[2]').text
		Battery_Capacity = browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[4]/td[2]/table/tbody/tr/td[2]').text
		Battery_Life = browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[5]/td[2]').text
		Main_Output = browser2.find_element(By.XPATH,'//*[@id="ext-gen117"]/table[2]/tbody/tr[6]/td[2]/table/tbody/tr/td[2]').text
		
		if Main_Output == "On":
			Main_Output = "Подключен к сети"
		else:
			Main_Output = "Отключен от сети"

		print('ИБП СОТИАССО:\n' + Battery_Voltage2 + '\n' +  Output_Frequency2 + '\n' + Output_Voltage2 + '\n' + Output_Current + '\n'
		 + Total_Gross_Power + '\n' + Total_Active_Power + '\n' + Battery_Status + '\n' + Source_Power + '\n' + Battery_load_level + '\n'
		 + Battery_Capacity + '\n' + Battery_Life + '\n' + Main_Output)

		browser2.close()
		browser2.quit()
		#_______________________________________________________________________________________________________________
		time.sleep(60)

bot = telebot.TeleBot("**********")
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("СОТИАССО")
	item2=types.KeyboardButton("АИИСКУЭ")
	markup.add(item1)
	markup.add(item2)
	bot.send_message(m.chat.id, 'Доброго времени суток, данный бот разработан для мониторинга текущих параметров источников бесперебойного питания на ЯТЭЦ-1.\nДля получения иформации нажмите на одну из систем (АИИСКУЭ или СОТИАССО)',  reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_answer(message):
	global Device_Status,UPS_Load,Puntime_Remaining,Internal_Temperature,Input_Voltage,Output_Voltage1,Input_Frequency,Output_Frequency1,Battery_Charge,Battery_Voltage1,Battery_Status,Battery_Voltage2,Output_Frequency2,Output_Voltage2,Output_Current,Total_Gross_Power,Total_Active_Power,Source_Power,Battery_load_level,Battery_Capacity,Battery_Life,Main_Output
	if message.text.strip() == "СОТИАССО":# or message.text == "сотиассо":
		answer = str('ИБП СОТИАССО:\n' + Main_Output + '\n' + "Выходная частота: " + Output_Frequency2 + '\n' + "Выходное напряжение: " + Output_Voltage2 + '\n' + "Выходной ток: " + Output_Current + '\n'
		+ "Общая полная мощность: " + Total_Gross_Power + '\n' + "Общая активная мощность: " + Total_Active_Power + '\n' + "Состояние батареи: " + Battery_Status + '\n' + "Источник питания: " + Source_Power + '\n' + "Уровень нагрузки: " + Battery_load_level + '\n'
		+ "Емкость батареи: " + Battery_Capacity + '\n' + "Время работы от батареи: " + Battery_Life + '\n' + "Напряжение батареи: " + Battery_Voltage2)
	elif message.text.strip() == "АИИСКУЭ":# or message.text == "аиискуэ":
		answer = str('ИБП АИИСКУЭ:\n' + Device_Status+ '\n' + "Уровень нагрузки: " + UPS_Load+ ' %\n' + "Время работы от батарей: " + Puntime_Remaining + ' минут\n' + "Температура: " + Internal_Temperature+ '\n' + "Входное напряжение: "  + Input_Voltage+ ' эВ\n'
		+ "Выходное напряжение: " + Output_Voltage1+ ' эВ\n' + "Частота входного напряжения: " + Input_Frequency+ ' Гц\n' + "Частота выходного напряжения: " + Output_Frequency1+ ' Гц\n' + "Заряд батарей: " + Battery_Charge + ' %\n' + "Вольтаж постоянного тока: " + Battery_Voltage1 + ' В\n')
	else:
		answer = "Убедитесь в правильности ввода названия системы, к которой относится источник бесперебойного питания (СОТИАССО или АИИСКУЭ)."
	bot.send_message(message.chat.id, answer)

if __name__ == '__main__':
	th1 = Thread(target=main_func)
	th1.start()
	th2 = Thread(target=bot.infinity_polling)
	th2.start()