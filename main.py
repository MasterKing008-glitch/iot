from devices import LCDDisplay, Ultrasonic, DHT11Sensor, RGB
import time

# Create objects
lcd = LCDDisplay()
ultra = Ultrasonic()
dht = DHT11Sensor()
rgb = RGB()

# Startup message
lcd.show("IoT course", "Welcome AUPP")
time.sleep(2)

while True:
    dist = ultra.distance()
    temp, hum = dht.read()

    # Print
    print("Distance:", dist)
    print("Temp:", temp, "C")
    print("Hum:", hum, "%")
    print("----------------")

    # LCD display
    line1 = "Dist:{:.1f}cm".format(dist) if dist else "No Dist"
    line2 = "T:{} H:{}".format(temp, hum) if temp else "DHT Error"
    lcd.show(line1, line2)

    # LED logic
    rgb.clear()
    if dist is None:
        rgb.set(0, (255, 255, 0))  # yellow
    elif dist < 10:
        rgb.set(0, (255, 0, 0))    # red
    elif dist < 30:
        rgb.set(1, (0, 255, 0))    # green
    else:
        rgb.set(2, (0, 0, 255))    # blue

    time.sleep(2)