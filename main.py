from machine import Pin
from time import sleep

monsteraSensor = Pin(2, Pin.IN)

def read_sensor():
    if monsteraSensor.value() == 1:
        print("Monstera is thirsty")
    else:
        print("Monstera is happy")
        sleep(1)


while True:
    