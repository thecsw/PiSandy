
# Handling the messages
def handle(msg):
    user_id = msg['chat']['id']
    log_message('/n    Initializing user id - [{}]...'.format(user_id), False)
    msg_id = msg['message_id']
    log_message('    Initializing message id - [{}]...'.format(msg_id), False)
    name = msg['chat']['first_name'].encode('utf-8')
    log_message('    Initializing user\'s name - [{}]...'.format(name), False)
    try:
        lastname = msg['chat']['last_name'].encode('utf-8')
        log_message('    Initializing user\'s lastname - [{}]...'.format(lastname), False)
    except:
	print("The user - [{}] doesn't have lastname".format(user_id))
    command = msg['text'].encode('utf-8').lower()
    log_message('    Initializing command - [{}]...'.format(command), False)
    #print ('[ {} ] {} : {}'.format(user_id, name, command))
    #START
    if command == '/start':
        try:
            thread.start_new_thread(sms, (user_id, 'Thank you for activating the bot!\n\
This bot is under construction, sometimes it can be offline.\n\
Please type /help to get a list of commands.\n\
Again thanks for trying out the bot and\n\
Have a nice day!' ))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
        except:
            print('Exception caught!')
        return

    #HUMIDITY
    if command == '/gethumidity':
        try:
            #humidity = pround(sense.get_humidity())
            thread.start_new_thread(sms, (user_id, 'Humidity : {} ± {}%rH'.format(round(sense.get_humidity(), 2), round(stdev(hum_mes), 2))))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
        except:
            print('Exception caught!')
    	return

    #DEW POINT
    if command == '/getdew':
        try:
            dew = dewgamma()
            thread.start_new_thread(sms, (user_id, 'Dew Point : {} ± 0.1°C'.format(round(dew, 2))))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
        except:
	   print('Exception caught!')
	return

    #PRESSURE
    if command == '/getpressure':
        try:
            #pressure = pround(sense.get_pressure())
            thread.start_new_thread(sms, (user_id, 'Pressure : {} ± {} Millibars'.format(round(sense.get_pressure(), 2), round(stdev(pres_mes), 2))))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
        except:
            print('Exception caught!')
        return

    #HELP
    if command == '/help':
        try:
            thread.start_new_thread(sms ,(user_id, '''Command list
/get to get data from all sensors
/gettemp to get mean temperature
/gethumidity to get humidity level
/getpressure to get pressure level
/getdew to get the dew point
/help to get this help screen
/time to get current time (local)'''))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
	except:
            print('Exception caught!')
        return

    #TIME
    if command == '/time':
        try:
            #now = datetime.now()
            thread.start_new_thread(sms, (user_id, 'Time - {}:{}'.format(datetime.now().hour, datetime.now().minute)))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
        except:
            print('Exception caught!')
        return

    #RESETDUMMT
    if command == '/reset':
        try:
            thread.start_new_thread(sms, (user_id, 'Dont you dare! Ill call SkyNet!'))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
        except:
            print('Exception caught!')
        return

    #RESETBOT
    if command == '/resetbot':
        try:
            cb.reset()
            thread.start_new_thread(sms, (user_id, 'Bot has been reseted successfully!'))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
        except:
            print('Exception caught!')
        return

    #FULL DATA
    if command == '/get':
        try:
            thread.start_new_thread(temp, (user_id, thermo))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
    	except:
            print('Exception caught!')
        return

    #TEMPERATURE
    if command == '/gettemp':
        try:
            thread.start_new_thread(sms, (user_id, 'Temperature :\n\
Celcius - {} ± {}°C\n\
Fahrenheit - {} ± {}°F\n\
Kelvin - {} ± {}K'.format(round(mean(thermo), 1),
                          round(stdev(thermo), 2),
                          round(mean(thermo)*1.8+32, 1),
                          round(stdev(thermof), 2),
                          round(mean(thermo), 1)+273,
                          round(stdev(thermo), 2))))
            log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
        except:
            print('Exception caught!')
        return

    #BOT RESPONSE
    try:
        response = cb.say(command).encode('utf-8')
        thread.start_new_thread(reply, (user_id, msg_id, response))
        print ('SandyPI: {}'.format(response))
        log_message('Sending request ({}) answer from [{}]{}...'.format(command, user_id, name), False)
    except:
        print('Exception caught!')

    #SAVE TO FILE
    with open('SPI.txt', 'a') as file:
        #now = datetime.now()
        file.write('[{}:{}] {} : {}\n'.format(datetime.now().hour, datetime.now().minute, name, command))
        file.write('[{}:{}] SandyPI: {}\n'.format(datetime.now().hour, datetime.now().minute, response))
