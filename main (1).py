from machine import Pin, I2C
from utime import sleep

# --- I2C Setup ---
# SDA = GP26 (pin 31), SCL = GP27 (pin 32)
i2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000)

# Scan for I2C devices first
devices = i2c.scan()
print("I2C devices found:", [hex(d) for d in devices])

if not devices:
    print()
    print("ERROR: No I2C devices detected!")
    print()
    print("Troubleshooting checklist:")
    print("  1. Check wiring:")
    print("     VCC -> 3V3 (pin 36)")
    print("     GND -> GND (pin 38)")
    print("     SDA -> GP26 (pin 31)")
    print("     SCL -> GP27 (pin 32)")
    print("  2. Make sure connections are solid (not loose)")
    print("  3. Some displays use 5V, try VCC -> VBUS (pin 40)")
    print("  4. Check if SDA/SCL labels are swapped on your board")
else:
    from sh1106 import SH1106_I2C

    addr = devices[0]
    print("Using device at address:", hex(addr))

    # --- OLED Setup (128x64 SH1106) ---
    oled = SH1106_I2C(128, 64, i2c, addr=addr)

    # --- Display demo ---
    oled.fill(0)                          # clear screen
    oled.text("Hello!", 0, 0)             # line 1
    oled.text("Pico 2W + SH1106", 0, 16)  # line 2
    oled.text("I2C LCD Ready", 0, 32)     # line 3
    oled.show()

    print("Display initialized!")
