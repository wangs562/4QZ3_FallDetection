from sense_hat import SenseHat
import time, random

# rpiSense = SenseHat()
# rpiSense.clear()

LED_SCREEN_SIZE = 8

# LED Screen Flair

def screenFlairLED():
    index = 0

    for index in range(LED_SCREEN_SIZE):
        for i in range(index + 1):
            targetPos = [index - i, i]
            print(targetPos) # instead of printing target pos, change to color range

    for index in range(LED_SCREEN_SIZE - 1, -1, -1):
            for i in range(index + 1):
                targetPos = [index - i, i]
                print(targetPos) # instead of printing target pos, change to color range

def initializeSystem():
    screenFlairLED()

def main():
    initializeSystem()

main()
    

# plan:
# coordinates of screen flair will always equal 0 to 7