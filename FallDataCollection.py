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
def screenFlairCoordinateControl(coordIndex, rowIndex):
    coordinateArray = []

    for i in range(coordIndex + 1):
        targetPos = [int(rowIndex - i - ((rowIndex - coordIndex) / 2)), int(i + ((rowIndex - coordIndex) / 2))]
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
    
    for rowIndexRaw in range(LED_SCREEN_SIZE * -1 + 1, LED_SCREEN_SIZE):
        coordIndex = -1 * abs(rowIndexRaw) + (LED_SCREEN_SIZE - 1)
        rowIndex = rowIndexRaw + LED_SCREEN_SIZE - 1

        targetCoordinateArray = screenFlairCoordinateControl(coordIndex, rowIndex)
        screenFlairLEDControl(coordIndex, 0)

    # the first input of the coordinate control function takes an absolute value function y = -|x| + 7, which will output 7 descending to 0, then ascending to 7
    # second input will simply shift the raw index so output begins at 0, then increments up to 13

def initializeSensors():
    # sense.set_imu_config(False, True, True)

    print("All Sensors Activated")

def initializeSystem():
    screenFlairLED()
    initializeSensors()

    screenClear()
    setScreenText(GREETING_TEXT)



# Utility Functions
def setScreenText(screenText, textColor = DEFAULT_TEXT_COLOR, scrollSpeed = 0.05):
    # sense.show_message(screenText, text_colour = textColor, scroll_speed = scrollSpeed)
    print(screenText)

def screenClear():
    # sense.clear(255, 255, 255)
    print("Cleared Screen")



# Accelerometer Functions
def getAccelerometerData():
    accelerationRaw = 0
    gyroRaw = 0

    # accelerationRaw = sense.get_accelerometer_raw()
    # gyroRaw = sense.get

# Main Function
def main():
    initializeSystem()
    

main()