# iot


https://theara-seng.github.io/Slides/iot/Webserver_control/#/10
LCD I2C
```bash
from machine import Pin, SoftI2C
from machine_i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.clear()
lcd.move_to(0, 0)         # first row
lcd.putstr("IoT course")
lcd.move_to(0, 1)         # second row
lcd.putstr("Welcome to AUPP")
```

Ultrasonic
```bash
from machine import Pin, time_pulse_us
import time

# Pin configuration
TRIG = Pin(27, Pin.OUT)
ECHO = Pin(26, Pin.IN)

def get_distance_cm():
    # Ensure trigger is LOW
    TRIG.value(0)
    time.sleep_us(2)

    # Send 10µs pulse
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    # Measure echo pulse duration
    duration = time_pulse_us(ECHO, 1, 30000)  # timeout = 30ms

    # Check for timeout
    if duration < 0:
        return None

    # Distance calculation (cm)
    distance = (duration * 0.0343) / 2
    return distance

# Main loop
while True:
    dist = get_distance_cm()
    if dist is not None:
        print("Distance: {:.2f} cm".format(dist))
    else:
        print("Out of range")

    time.sleep(1)
```

dht11
```bash
from machine import Pin
import dht
import time

sensor = dht.DHT11(Pin(33))

print("DHT11 Sensor Reading Started...")

while True:
    try:
        sensor.measure() 
        
        temperature = sensor.temperature()  # °C
        humidity = sensor.humidity()        # %
        
        print("Temperature: {} °C".format(temperature))
        print("Humidity: {} %".format(humidity))
        print("---------------------------")
        
    except OSError:
        print("Failed to read from DHT11 sensor")

    time.sleep(2)  # DHT11 needs at least 1 second delay
```


WS2812
```bash
from machine import Pin
import neopixel
import time

led = neopixel.NeoPixel(Pin(23), 16)

while True:

    led[0] = (255,0,0)  # RED
    led.write()
    time.sleep(1)

    led[1] = (0,255,0)  # GREEN
    led.write()
    time.sleep(1)

    led[2] = (0,0,255)  # BLUE
    led.write()
    time.sleep(1)
```