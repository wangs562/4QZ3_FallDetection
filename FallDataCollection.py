from sense_hat import SenseHat
import time, random

# rpiSense = SenseHat()
# rpiSense.clear()

LED_SCREEN_SIZE = 8

GREETING_TEXT = "FALL DETECTION SYSTEM - SAM WANG - IBEHS 4QZ3"

DEFAULT_TEXT_COLOR = (0, 0, 0)
COLOR_ARRAY = [
    (255, 0, 0),
    (255, 182, 0),
    (109, 255, 0),
    (0, 255, 73),
    (0, 255, 255),
    (0, 73, 255),
    (109, 0, 255),
    (255, 0, 255)
]

# Initialization Functions
def screenFlairCoordinateControl(positionCoord):
    coordinateArray = []

    for i in range(positionCoord + 1):
        targetPos = [positionCoord - i, i]
        coordinateArray.append(targetPos)

    print(coordinateArray)
    return coordinateArray

def screenFlairLEDControl(targRowIndex, direction = 0):

    if (direction == 0):
        targetColor = COLOR_ARRAY[targRowIndex]
    elif (direction == 1):
        targetColor = COLOR_ARRAY[targRowIndex]

    for coord in range(targRowIndex):
        # rpiSense.set_pixel(x, y, targetColor)
        time.sleep(0.1)

def screenFlairLED(startPos = 0):
    rowIndex = startPos
    
    for rowIndex in range(LED_SCREEN_SIZE):
        targetCoordinateArray = screenFlairCoordinateControl(rowIndex)
        screenFlairLEDControl(rowIndex, 0)

    for rowIndex in range(LED_SCREEN_SIZE - 2, -1, -1):
        screenFlairCoordinateControl(rowIndex)
        screenFlairLEDControl(rowIndex, 1)

def initializeSystem():
    screenFlairLED()

    screenClear()
    setScreenText(GREETING_TEXT)



# Utility Functions
def setScreenText(screenText, textColor = DEFAULT_TEXT_COLOR, scrollSpeed = 0.05):
    # sense.show_message(screenText, text_colour = textColor, scroll_speed = scrollSpeed)
    print(screenText)

def screenClear():
    # sense.clear(255, 255, 255)
    print("Cleared Screen")



# Main Function
def main():
    initializeSystem()
    

main()