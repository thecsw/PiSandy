import RPi.GPIO as GPIO

# RGB code
BLUE = 21
GREEN = 20
RED = 16

# GPIO setup
log_message('Setting up GPIO for current output...', True)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Outputc
log_message('Setting up GPIO color output...', True)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

# Displaying one color
def OUTPUT (COLOR):
    GPIO.output(BLUE, False)
    GPIO.output(GREEN, False)
    GPIO.output(RED, False)
    GPIO.output(COLOR, True)
    return

# Displaying multiple colors
def MULTOUTPUT (COLOR, COLORS):
    GPIO.output(BLUE, False)
    GPIO.output(GREEN, False)
    GPIO.output(RED, False)
    GPIO.output(COLOR, True)
    GPIO.output(COLORS, True)
    return

# Control led bulb colors depending on the temperature (Celcuis)
def warning (thermo):
    #log_message('Configuring the light bulb...', False)
    averround = round(mean(thermo), 2)
    if averround < 30:
	if averround > 26:
            MULTOUTPUT(RED, GREEN)
	    return
        OUTPUT(GREEN)
	return
    OUTPUT(RED)
    return
