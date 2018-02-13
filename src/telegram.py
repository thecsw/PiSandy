
# Send message from bot
log_message('Initializing method for sending messages via telegram...', True)
def sms(ID, str):
    bot.sendChatAction(ID, 'typing')
    bot.sendMessage(ID, str)

# Reply to messages
log_message('Initializing method for replying to users\' messages...', True)
def reply(ID, msgID, str):
    bot.sendChatAction(ID, 'typing')
    time.sleep(len(str)/5)
    bot.sendMessage(ID, str, None, None, None, msgID)

# Send meessage with delay
log_message('Initializing method for sending messages via telegram with delay...', True)
def sms_delay(sec, ID, strg):
    bot.sendChatAction(ID, 'typing')
    sleep(DELAY)
    sms(ID, strg)
