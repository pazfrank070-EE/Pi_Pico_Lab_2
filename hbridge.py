from machine import Pin
from time import sleep

# Definir pines
IN1 = Pin(10, Pin.OUT)
IN2 = Pin(11, Pin.OUT)
IN3 = Pin(12, Pin.OUT)
IN4 = Pin(13, Pin.OUT)

# Funciones motor 1
def motor1_forward():
    IN1.value(1)
    IN2.value(0)

def motor1_backward():
    IN1.value(0)
    IN2.value(1)

def motor1_stop():
    IN1.value(0)
    IN2.value(0)

# Funciones motor 2
def motor2_forward():
    IN3.value(1)
    IN4.value(0)

def motor2_backward():
    IN3.value(0)
    IN4.value(1)

def motor2_stop():
    IN3.value(0)
    IN4.value(0)

# Prueba básica
while True:
    print("Avanzando")
    motor1_forward()
    motor2_forward()
    sleep(2)

    print("Detener")
    motor1_stop()
    motor2_stop()
    sleep(1)

    print("Retrocediendo")
    motor1_backward()
    motor2_backward()
    sleep(2)

    print("Detener")
    motor1_stop()
    motor2_stop()
    sleep(2)