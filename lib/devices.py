from machine import Pin, SoftI2C, time_pulse_us
from machine_i2c_lcd import I2cLcd
import neopixel
import dht
import time


# ---------------- LCD ----------------
class LCDDisplay:
    def __init__(self, sda=21, scl=22, addr=0x27):
        i2c = SoftI2C(sda=Pin(sda), scl=Pin(scl), freq=400000)
        self.lcd = I2cLcd(i2c, addr, 2, 16)

    def show(self, line1="", line2=""):
        self.lcd.clear()
        self.lcd.move_to(0, 0)
        self.lcd.putstr(line1[:16])
        self.lcd.move_to(0, 1)
        self.lcd.putstr(line2[:16])


# ---------------- Ultrasonic ----------------
class Ultrasonic:
    def __init__(self, trig=27, echo=26):
        self.trig = Pin(trig, Pin.OUT)
        self.echo = Pin(echo, Pin.IN)

    def distance(self):
        self.trig.value(0)
        time.sleep_us(2)

        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)

        duration = time_pulse_us(self.echo, 1, 30000)

        if duration < 0:
            return None

        return (duration * 0.0343) / 2


# ---------------- DHT11 ----------------
class DHT11Sensor:
    def __init__(self, pin=33):
        self.sensor = dht.DHT11(Pin(pin))

    def read(self):
        try:
            self.sensor.measure()
            return self.sensor.temperature(), self.sensor.humidity()
        except:
            return None, None


# ---------------- WS2812 ----------------
class RGB:
    def __init__(self, pin=23, n=16):
        self.led = neopixel.NeoPixel(Pin(pin), n)

    def clear(self):
        for i in range(len(self.led)):
            self.led[i] = (0, 0, 0)
        self.led.write()

    def set(self, i, color):
        self.led[i] = color
        self.led.write()


# ---------------- Buzzer ----------------
class Buzzer:
    def __init__(self, pin=4, enabled=True):
        self.buzzer = Pin(pin, Pin.OUT)
        self.enabled = enabled

    def beep(self, duration=0.2):
        if self.enabled:
            self.buzzer.on()
            time.sleep(duration)
            self.buzzer.off()

    def on(self):
        if self.enabled:
            self.buzzer.on()

    def off(self):
        self.buzzer.off()