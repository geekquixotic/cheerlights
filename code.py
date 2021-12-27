# Adafruit IO code from: https://learn.adafruit.com/mqtt-in-circuitpython/circuitpython-wifi-usage
# Neopixel code from: https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel
# Found correct neopixel pin via: https://learn.adafruit.com/assets/96736

## Get the Libraries
import time
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import board
import random
from rainbowio import colorwheel
import neopixel
from adafruit_led_animation.color import RED, GREEN, BLUE, CYAN, WHITE, OLD_LACE, PURPLE, MAGENTA, YELLOW, ORANGE, PINK, GOLD

## Define the Pixel Info
pixel_pin = board.IO33
num_pixels = 50
string=[] ## For keeping track of which color each pixel is now
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)

## Colors for the wreath loop
colorPicks=[
    RED,
    GREEN,
    GOLD,
    BLUE
]

## Colors for the cheerlights
cheerColors={
    'red': RED,
    'green': GREEN,
    'blue': BLUE,
    'cyan': CYAN,
    'white': WHITE,
    'oldlace': OLD_LACE,
    'purple': PURPLE,
    'magenta': MAGENTA,
    'yellow': YELLOW,
    'orange': ORANGE,
    'pink': PINK
}

# Add a secrets.py to your filesystem that has a dictionary called secrets with "ssid" and
# "password" keys with your WiFi credentials. DO NOT share that file or commit it into Git or other
# source control.
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

## The feed for the cheerlights on Adafruit
feed = "cheerlights/feeds/color"

## Connect to Wifi
print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])

## Light up the wreath with alternating colors.
for i in range(num_pixels):
    color=colorPicks[i%len(colorPicks)]
    pixels[i] = color
    string.append(color)

# Define callback methods which are called when events occur
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print("Connected to Adafruit IO! Listening for topic changes on %s" % feed)
    # Subscribe to all changes on the onoff_feed.
    client.subscribe(feed)

def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from Adafruit IO!")

def message(client, topic, message):
    # This method is called when a topic the client is subscribed to
    # has a new message.
    print("New message on topic {0}: {1}".format(topic, message))
    for i in range(num_pixels):
        pixels[i] = cheerColors[message]

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=secrets["broker"],
    port=secrets["port"],
    username=secrets["aio_username"],
    password=secrets["aio_key"],
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print("Connecting to Adafruit IO...")
mqtt_client.connect()

##
## Loop
##
while True:
    # Poll the message queue
    mqtt_client.loop()

    ## Pick a new light
    pixel=random.randint(0,num_pixels-1)

    ## Pick a color other than the one it is now
    options=colorPicks.copy()
    options.remove(string[pixel])
    color=random.choice(options)

    ## Set the pixel and store the choice
    pixels[pixel]=color
    string[pixel]=color

    print("Pixel {} to {}".format(pixel,color))
