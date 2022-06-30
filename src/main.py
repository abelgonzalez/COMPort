# -*- coding: utf-8 -*-
import os
import sys
import time
import serial
import struct
import binascii
import pyqtgraph as pg

from modules.report import *
from modules.receiver import *
from modules.visualization import *


def main():
    # BEGINNING OF EXECUTION

    # --> Global Variables
    PORT = "COM3"
    LINES_TO_READ = 10
    BAUDRATE = 9600
    BYTESIZE = serial.EIGHTBITS
    TIMEOUT = 1
    STOPBITS = serial.STOPBITS_ONE
    BUFFER_SIZE = 37
    ROOT_DIR = os.path.abspath(os.curdir)

    # Temperature parameters
    MIN_TEMP = 35
    MAX_TEMP = 37.5

    # HR parameters
    # Tanaka method FC max = 220 - (0,7x age)
    MIN_HR = 50
    MAX_HR = 203.20

    # Lists declaration
    listID = []
    listHR = []
    listBin = []
    listHex = []
    listGyroX = []
    listGyroY = []
    listGyroZ = []
    listRRInterval = []
    listTemperature = []
    listAccelerometerX = []
    listAccelerometerY = []
    listAccelerometerZ = []

    # --> Data sample
    PARTICIPANT_NAME = "Lucas"
    PARTICIPANT_BIRTH = 20/10/1996
    PARTICIPANT_AGE = 26

    # --> User's input
    print("Enter the participant's name. Ex: Lucas")
    PARTICIPANT_NAME = input("")

    print("Enter the participant's date of birth in DD/MM/YYYY format. Ex: 20/10/1996")
    PARTICIPANT_BIRTH = input("")

    print("Which HRmax analysis method do you want to use? Enter the number only. Ex: 1")
    print("1 - Tanaka (207 - 0,7 x age)")
    print("2 - Method 2 (211 - 0,64 x age)")
    print("3 - Method 3 (220 - age)")
    ANALISYS_METHOD = input("")

    print("Enter the port to connect and press Enter. Ex: COM3")
    PORT = input("")

    print("Note: 1 measurement = 2 seconds")
    print("Enter the quantity of measurements to capture and press Enter. Ex: 10")
    LINES_TO_READ = input("")

    # --> Pre-processing

    # Converting datetime to age
    PARTICIPANT_AGE = DatetimeToAgeNumber(PARTICIPANT_BIRTH)

    # Analysis method. Default: Tanaka method FC máxima = 220 - (0,7x age)
    try:
        MAX_HR = ProcessSelectedAnalysisMethod(
            ANALISYS_METHOD, PARTICIPANT_AGE)
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
            pass
        else:
            print(e)
            pass

    try:
        serialPort = serial.Serial(
            port=PORT, baudrate=BAUDRATE, bytesize=BYTESIZE, timeout=TIMEOUT, stopbits=STOPBITS
        )
        # Used to hold data coming over UART
        serialString = ""

        linesToReadStr = (int)(LINES_TO_READ)
        remainingLines = linesToReadStr
        index = 0

        print(serialPort)
        print('\n')
        print(
            ">>>>>> To stop the capture at any time, press Ctrl+C <<<<<<")
        print('\n')

        # Visualization init
        graphHR = pg.plot()
        graphTemp = pg.plot()

        setPyQtGraph(graphHR, "Live HR Stream from " + str(PORT),
                     "Beats per minute", "Time (one plot = 1 sec)",
                     MAX_HR, MIN_HR, int(LINES_TO_READ)*2)

        setPyQtGraph(graphTemp, "Live Temperature Stream from " + str(PORT),
                     "Temp (celcius)", "Time (one plot = 1 sec)",
                     MAX_TEMP, MIN_TEMP, int(LINES_TO_READ)*2)

        # DATA STREAM
        while (remainingLines > 0):
            # Wait until there is data waiting in the serial buffer
            if serialPort.in_waiting > 0:

                # Read data out of the buffer until a carraige return / new line is found
                serialString = serialPort.read(BUFFER_SIZE).hex()

                try:
                    lines = serialString.replace('\n', ' ')
                    lines = serialString.replace(' ', '')

                    binaryStr = binascii.unhexlify(lines)
                    hexadecimalStr = binaryStr.hex()

                    print("Measurement " + str(index) +
                          " of " + str(linesToReadStr))

                    listBin.append(binaryStr)
                    listHex.append(hexadecimalStr)

                    lineStr = []

                    for i in range(len(hexadecimalStr) // 2):
                        lineStr.append('{0}'.format(
                            hexadecimalStr[i * 2:i * 2 + 2]))

                    listID.append(index)

                    byteArray = bytearray.fromhex(lineStr[2])
                    listHR.append(int.from_bytes(byteArray, "big"))
                    hrValue = str(listHR[index - 1])
                    print("HR: " + hrValue)

                    byteArray = bytearray.fromhex(lineStr[3] + lineStr[4])
                    listRRInterval.append(
                        int.from_bytes(byteArray, "little"))
                    rrIntervalValue = str(listRRInterval[index - 1])
                    print("RRInterval: " + rrIntervalValue)

                    byteArray = bytearray.fromhex(
                        lineStr[5] + lineStr[6] + lineStr[7] + lineStr[8])
                    listTemperature.append(
                        struct.unpack('<f', byteArray)[0])
                    temperatureValue = str(listTemperature[index - 1])
                    print("Temperature: " + temperatureValue)

                    byteArray = bytearray.fromhex(
                        lineStr[9] + lineStr[10] + lineStr[11] + lineStr[12])
                    listAccelerometerX.append(
                        struct.unpack('<f', byteArray)[0])
                    accelerometerXValue = str(
                        listAccelerometerX[index - 1])
                    print("AccelerometerX: " + accelerometerXValue)

                    byteArray = bytearray.fromhex(
                        lineStr[13] + lineStr[14] + lineStr[15] + lineStr[16])
                    listAccelerometerY.append(
                        struct.unpack('<f', byteArray)[0])
                    accelerometerYValue = str(
                        listAccelerometerY[index - 1])
                    print("AccelerometerY: " + accelerometerYValue)

                    byteArray = bytearray.fromhex(
                        lineStr[17] + lineStr[18] + lineStr[19] + lineStr[20])
                    listAccelerometerZ.append(
                        struct.unpack('<f', byteArray)[0])
                    accelerometerZValue = str(
                        listAccelerometerZ[index - 1])
                    print("AccelerometerZ: " + accelerometerZValue)

                    byteArray = bytearray.fromhex(
                        lineStr[21] + lineStr[22] + lineStr[23] + lineStr[24])
                    listGyroX.append(struct.unpack('<f', byteArray)[0])
                    gyroXValue = str(listGyroX[index - 1])
                    print("GyroX: " + gyroXValue)

                    byteArray = bytearray.fromhex(
                        lineStr[25] + lineStr[26] + lineStr[27] + lineStr[28])
                    listGyroY.append(struct.unpack('<f', byteArray)[0])
                    gyroYValue = str(listGyroY[index - 1])
                    print("GyroY: " + gyroYValue)

                    byteArray = bytearray.fromhex(
                        lineStr[29] + lineStr[30] + lineStr[31] + lineStr[32])
                    listGyroZ.append(struct.unpack('<f', byteArray)[0])
                    gyroZValue = str(listGyroZ[index - 1])
                    print("GyroZ: " + gyroZValue)

                    # Plots graph HR and Temperature, per second.
                    updatePyQtGraph(graphHR, listID, listHR)
                    updatePyQtGraph(graphTemp, listID, listTemperature)

                    remainingLines -= 1
                    index += 1
                    print('\n')

                except:
                    pass

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
            pass
        else:
            print(e)
            pass

    except:
        # In case of the user press Ctrl+C, we will generate all files anyway.
        pass

    # ----> Report module execution
    # Export files
    timestr = time.strftime("%Y%m%d-%H%M%S")
    metada_time = timestr+'_' + \
        str(PARTICIPANT_NAME) + '_' + str(PARTICIPANT_AGE) + '_'
    exportDir = ROOT_DIR + "/src/output/"

    # Check whether the specified path exists or not
    CheckExportPath(exportDir)

    GenerateBin(exportDir, listBin, metada_time)
    GenerateHex(exportDir, listHex, metada_time)
    GenerateXlsx(exportDir, listID, listHR, listRRInterval, listTemperature,
                 listAccelerometerX, listAccelerometerY, listAccelerometerZ,
                 listGyroX, listGyroY, listGyroZ, metada_time)

    # END OF EXECUTION
    print(sys.argv)
    input("Press Enter to close.")


if __name__ == "__main__":
    main()
