from devices import LCDDisplay, Ultrasonic, DHT11Sensor, RGB, Buzzer
import time

# Create objects
lcd = LCDDisplay()
ultra = Ultrasonic()
dht = DHT11Sensor()
rgb = RGB()
buzzer = Buzzer()

# Startup
lcd.show("IoT course", "Welcome AUPP")
time.sleep(2)

while True:
    dist = ultra.distance()
    temp, hum = dht.read()

    # ---------------- Serial Output ----------------
    print("Distance:", dist)
    print("Temperature:", temp, "C")
    print("Humidity:", hum, "%")
    print("------------------------")

    # ---------------- LCD ----------------
    line1 = "Dist:{:.1f}cm".format(dist) if dist else "No Distance"
    line2 = "T:{} H:{}".format(temp, hum) if temp else "DHT Error"
    lcd.show(line1, line2)

    # ---------------- LED + BUZZER ----------------
    rgb.clear()

    if dist is None:
        rgb.set(0, (255, 255, 0))  # Yellow
    elif dist < 10:
        rgb.set(0, (255, 0, 0))    # Red
        buzzer.beep(0.5)
    elif dist < 30:
        rgb.set(1, (0, 255, 0))    # Green
        buzzer.beep(0.2)
    else:
        rgb.set(2, (0, 0, 255))    # Blue

    time.sleep(2)