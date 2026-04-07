from machine import Pin, I2C
from utime import sleep, sleep_ms, ticks_ms, ticks_diff

# --- I2C Setup ---
# SDA = GP26 (pin 31), SCL = GP27 (pin 32)
i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)

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

    sleep(1)

    # Loading bar section (200 ms)
    oled.fill(0)
    oled.text("Loading dance ...", 0, 0)

    bar_width = 100
    x_start = 14
    y_start = 30    

    oled.rect(x_start, y_start, bar_width, 10, 1)  # outline of bar
    oled.show()

    LOADING_TIME_MS = 80
    steps = 10
    delay = LOADING_TIME_MS // steps

    for i in range(steps):
        fill = int((i / steps) * (bar_width - 2))
        oled.fill_rect(x_start + 1, y_start + 1, fill, 8, 1)  # fill bar
        oled.show()

        sleep_ms(delay)

        sleep(1)


 # Dancing stick figure animation
frames = [
        [
            "  O  ",
            " /|\\ ",
            " / \\ "
        ],
        [
            "  O  ",
            " \\|/ ",
            " / \\ "
        ],
        [
            "  O  ",
            " /|> ",
            " / \\ "
        ],
        [
            "  O  ",
            " <|\\ ",
            " / \\ "
        ]
    ]
start_time = ticks_ms()

while ticks_diff(ticks_ms(), start_time) < 10000:

        for frame in frames:

            oled.fill(0)

            oled.text(frame[0], 40, 10)
            oled.text(frame[1], 40, 25)
            oled.text(frame[2], 40, 40)

            oled.show()

            sleep(0.25)

# Final message
oled.fill(0)
oled.text("Dance Complete!", 10, 28)
oled.show()

sleep(4)

# Stop the program
raise SystemExit