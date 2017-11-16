#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# Setting up encoding to display the celcius symbol
import os
import glob
import time
#Delays
import telepot
#Telegram API
import cleverbot
#from pprint import pprint
#import codecs

#p = u"абвгдежзийкл"
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
#Enabling the GPIO pins on raspberry pi

with open('SPI.txt', 'a') as file:
    file.write('SandyPI. Cleverbot converstion. User names are missing\n')
 
bot = telepot.Bot('439816740:AAGUv-uFga0Vf7XX9-yTPADabX6Eiuf_Bwg')
#Entering bots Telegram API key
bot.getMe()
#Initializing

cb = cleverbot.Cleverbot('6c3f005ec8f79dd543c7cca772a75fa9', timeout=60)


def read_temp_raw(ORDER):
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[ORDER]
    device_file = device_folder + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(NUMBER):
    lines = read_temp_raw(NUMBER)
    while lines[0].strip()[-3:] != 'YES':
        #time.sleep(0.2)
        lines = read_temp_raw(NUMBER)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

delay = 1;

def temp(chat_id):
    bot.sendMessage(chat_id, 'Connecting to host...')
    time.sleep(delay)
    bot.sendMessage(chat_id, 'Sending request...')
    time.sleep(delay)
    bot.sendMessage(chat_id, 'Receiving some weird numbers...')
    time.sleep(delay)
    bot.sendMessage(chat_id, 'Trying to resolve...')
    time.sleep(delay)
    bot.sendMessage(chat_id, 'Uploading results...')
           
    bot.sendMessage(chat_id, 'First -      {} ℃\nSecond - {} ℃\nThird -     {} ℃\nFourth -  {} ℃\nFifth -      {} ℃'.format(read_temp(0), read_temp(2), read_temp(4), read_temp(3), read_temp(1)))
    bot.sendMessage(chat_id, 'This bot is showing temperature from my room using raspberry pi and 5 DS18B20 temperature sensors')

def sms(chat_id, str):
    bot.sendMessage(chat_id, str)

def handle(msg):
#	chat_id = msg['chat']['id']
        chat_id = msg['from']['id']
	name = msg['chat']['first_name']
	lastname = msg['chat']['last_name']
	command = msg['text']
	response = cb.say(command)
#	print ('USER: %s\n' % command)
	print ('{} {}: {}'.format(name, lastname, command))
#        print ('SandyPI: {}'.format(response))

#        sms(chat_id, 'Hi')
        
	if command == '/temp':
            temp(chat_id) 
        if command == '/help':
            sms(chat_id, 'This bot is showing temperature from my room using raspberry pi and 5 DS18B20 temperature sensors\nType /temp to get temperatures\nType /help to get this help screen')            
        if command != '/help' and command != '/temp':      
            sms(chat_id, response)
            #print ('BOT: %s\n' % response)
            print ('SandyPI: {}'.format(response))
        
        with open('SPI.txt', 'a') as file:
            #file.write('USER: %s\n' % command)
            #file.write('BOT: %s\n' % response)
            file.write('{} {}: {}\n'.format(name, lastname, command))
            file.write('SandyPI: {}\n'.format(response))

#        with codecs.open("tets.txt", "a", "utf-16") as stream:   # or utf-8
#        stream.write('USER: {}\n'.format(command))
#        stream.write('USER: %s\n' % command)

bot.message_loop(handle)

while 1:
        time.sleep(10)


#print(read_temp(0))
#print(read_temp(2))
#print(read_temp(4))
#print(read_temp(3))
#print(read_temp(1))
#bot.sendMessage(296211623, 'First - {}C\nSecond - {}C\nThird - {}C\nFourth - {}C\nFifth - {}C'.format(read_temp(0), read_temp(2), read_temp(4), read_temp(3), read_temp(1)))
