from sense_hat import SenseHat
import time, random

# rpiSense = SenseHat()
# rpiSense.clear()

LED_SCREEN_SIZE = 8

# LED Screen Flair

def screenFlair():
    index = 0

    while index < LED_SCREEN_SIZE:
        for i in range(index + 1):
            targetPos = [index - i, i]
            print(targetPos) # instead of printing target pos, change to color range
        
        index = index + 1


screenFlair()

# plan:
# coordinates of screen flair will always equal 0 to 7