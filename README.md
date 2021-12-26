# Cheerlights Wreath

Want to control the lights behind me while I work? Send a Tweet with the hashtag of _#cheerlights_ and one of the following colors:

- red
- green
- blue
- cyan
- white
- oldlace
- purple
- magenta
- yellow
- orange
- pink

And within a few moments, the lights behind me will change to that color.

Examples:
> Time to paint the town red with #cheerlights

> I'm feeling blue today #cheerlights

Or simply,
> #cheerlights green

## Backstory

> [Cheerlights](https://cheerlights.com) is an “Internet of Things” project created by Hans Scharler(http://www.nothans.com/) in 2011 that allows people’s lights all across the world to synchronize to one color set by Twitter. This is a way to connect physical things with social networking experiences.

Source: https://cheerlights.com/about/

To celebrate the tenth anniverary of Cheerlights, I have created my own implementation using circuitpython and a strand of "Neopixels."

## Hardware
* [A Wemos D1 Mini](https://circuitpython.org/board/lolin_s2_mini/) running Circuit Python
* [Four-channel logic level converter by Siqma Robotics](https://store.siqma.com/txb0104-level-converter.html)
* [A strand of 50 WS2811 addressable LEDs from Alitove](https://www.amazon.com/gp/product/B06XD72LYM)
* An old Christmas wreath in our garage

After testing the wiring on a solderless breadboard, I wired up a permaboard using headers for the microcontroller and level shifter for later re-use.

## Firmware
The current code is a bit of a mess. While the Wemos D1 Mini is supported by CircuitPython, it is not as well documented as Adafuit's own boards with built-in WiFi capability. So I had to hack together a few other sample code bases for now.

I pulled samples in from:

* https://learn.adafruit.com/mqtt-in-circuitpython/circuitpython-wifi-usage
* https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel
* https://learn.adafruit.com/assets/96736
