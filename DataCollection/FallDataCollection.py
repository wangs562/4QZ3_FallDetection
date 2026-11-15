from sense_hat import SenseHat
from datetime import datetime
import time, random, csv, math

rpiSense = SenseHat()
rpiSense.clear()

LED_SCREEN_SIZE = 8

GREETING_TEXT = "FALL DETECTION SYSTEM - SAM WANG - IBEHS 4QZ3"

DEFAULT_SCROLL_SPEED = 0.03
DEFAULT_TEXT_COLOR = (255, 255, 255)
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



# Screen Flair Functions
def screenFlairCoordinateControl(coordIndex, rowIndex):
    coordinateArray = []

    for i in range(coordIndex + 1):
        targetPos = [int(rowIndex - i - ((rowIndex - coordIndex) / 2)), int(i + ((rowIndex - coordIndex) / 2))]
        coordinateArray.append(targetPos)

    return coordinateArray

def screenFlairLEDControl(targRowIndex, coordArray):
    targetColor = COLOR_ARRAY[targRowIndex]

    for coord in coordArray:
        rpiSense.set_pixel(coord[0], coord[1], targetColor)
        time.sleep(0.05)

def screenFlairLED(startPos = 0):
    rowIndex = startPos
    
    for rowIndexRaw in range(LED_SCREEN_SIZE * -1 + 1, LED_SCREEN_SIZE):
        coordIndex = -1 * abs(rowIndexRaw) + (LED_SCREEN_SIZE - 1)  # the first input of the coordinate control function takes an absolute value function y = -|x| + 7, which will output 7 descending to 0, then ascending to 7
        rowIndex = rowIndexRaw + LED_SCREEN_SIZE - 1                # second input will simply shift the raw index so output begins at 0, then increments up to 13

        targetCoordinateArray = screenFlairCoordinateControl(coordIndex, rowIndex)
        screenFlairLEDControl(coordIndex, targetCoordinateArray)


# Initialization Functions
def initializeSensors():
    rpiSense.set_imu_config(False, True, True)

def initializeSystem():
    screenFlairLED()
    initializeSensors()

    screenClear()
    setScreenText(GREETING_TEXT)



# Utility Functions
def setScreenText(screenText, textColor = DEFAULT_TEXT_COLOR, scrollSpeed = DEFAULT_SCROLL_SPEED):
    rpiSense.show_message(screenText, text_colour = textColor, scroll_speed = scrollSpeed)
    print(screenText)

def screenClear():
    rpiSense.clear(255, 255, 255)
    print("Cleared Screen")



# Accelerometer/Gyroscope Functions
def getAccelerometerData():
    accelerationRaw = rpiSense.get_accelerometer_raw()

    # test data! delete later :)
    # accelerationRaw = {'x': (random.randint(0, 100)) / 100,'y': (random.randint(0, 100)) / 100,'z': (random.randint(0, 100)) / 100}

    Ax = accelerationRaw['x']
    Ay = accelerationRaw['y']
    Az = accelerationRaw['z']

    AMag = math.sqrt(Ax**2 + Ay**2 + Az**2)

    return [Ax, Ay, Az, AMag]

def getGyroOrientationData():
    oriRaw = rpiSense.get_orientation()
    
    # test data! delete later :)
    # oriRaw = {'pitch': (random.randint(0, 100)) / 100,'roll': (random.randint(0, 100)) / 100,'yaw': (random.randint(0, 100)) / 100}
    
    return [oriRaw['pitch'], oriRaw['roll'], oriRaw['yaw']]

def getGyroAngVelData():
    angVelRaw = rpiSense.get_gyroscope_raw()
        
    # test data! delete later :)
    # angVelRaw = {'x': (random.randint(0, 100)) / 100,'y': (random.randint(0, 100)) / 100,'z': (random.randint(0, 100)) / 100}
        
    return [angVelRaw['x'], angVelRaw['y'], angVelRaw['z']]



# Joystick Functions
def getJSPos(csvArray):
    csvA = csvArray

    for event in rpiSense.stick.get_events():
        csvA = dataCollectionSelector(event.direction, event.action, csvA)

    return csvA



# Data Collection Logic Functions
def dataCollectionSelector(jsDirection, jsAction, csvArray):
    csvA = csvArray

    if jsAction == "pressed":
        if csvArray == []:
            if jsDirection == "up":
                csvA = initializeCSV("Lying")

            elif jsDirection == "left":
                csvA = initializeCSV("Sitting")

            elif jsDirection == "right":
                csvA = initializeCSV("Standing")

        elif jsDirection == "down" and csvArray != []:
            closeCSV(csvArray)
            csvA = []

    return csvA



# Data Storage Functions
def initializeCSV(activityType):
    fileName = "log_" + activityType + "_" + datetime.now().strftime ("%Y-%m-%d_%H-%M-%S") + "_data.csv"

    dataFile = open(fileName, "w", newline = '')
    writer = csv.writer(dataFile)
    writer.writerow(["Activity", "Time", "Ax", "Ay", "Az", "Amag", "Pitch", "Roll", "Yaw", "AVx", "AVy", "AVz"])

    csvArray = [fileName, dataFile, writer, activityType]

    return csvArray

def closeCSV(csvArray):
    csvArray[1].close()

def writeDataColumn(accelUnit, oriUnit, AVUnit, csvArray):
    csvArray[2].writerow([
        csvArray[3],
        datetime.now().isoformat(), 
        accelUnit[0], accelUnit[1], accelUnit[2], accelUnit[3],
        oriUnit[0], oriUnit[1], oriUnit[2],
        AVUnit[0], AVUnit[1], AVUnit[2]
    ])

    csvArray[1].flush()



# Main Function
def main():
    initializeSystem()

    csvFileArray = []

    while True:
        csvFileArray = getJSPos(csvFileArray)
        time.sleep(0.05)

        if csvFileArray != []:
            accelData = getAccelerometerData()
            oriData = getGyroOrientationData()
            angVelData = getGyroAngVelData()

            writeDataColumn(accelData, oriData, angVelData, csvFileArray)


main()