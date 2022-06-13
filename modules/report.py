# -*- coding: utf-8 -*-
"""
    Report module.
    Module with implementations of functions to save the data read at the end of the measurement.
"""
import os
import pandas as pd


def GenerateBin(export_dir: str, listBin: list, strMetadata: str):
    """
    Generates a binary file with the captured data.

    Parameters:
    listBin (list): String list object with data.

    Returns:
    Binary file with the processed data.
    """
    file_name = export_dir + r'/'+strMetadata+'capture_bin.bin'

    with open(file_name, 'wb') as f:
        for item in listBin:
            f.write(item)


def GenerateHex(export_dir: str, listHex: list, strMetadata: str):
    """
    Generates a text file with the captured data.

    Parameters:
    listHex (list): String list object with the data.

    Returns:
    Text file with the data processed in hexadecimal.
    """
    file_name = export_dir + r'/'+strMetadata+'capture_hex.txt'

    with open(file_name, 'w') as f:
        for item in listHex:
            f.write("%s\n" % item)


def GenerateXlsx(export_dir: str, id: list, hr: list, rrInterval: list, temperature: list,
                 accelerometerX: list, accelerometerY: list, accelerometerZ: list,
                 gyroX: list, gyroY: list, gyroZ: list, strMetadata: str):
    """
    Generate an Excel document from a dataframe with the captured data.

    Parameters:
    id (list): String list object with the data referring to the Id.
    hr (list): String list object with data referring to HR.
    rrInterval (list): String list object with the data referring to the RR interval.
    temperature (list): String list object with the data referring to Temperature.
    accelerometerX (list): String list object with data referring to the Accelerometer on the X axis.
    accelerometerY (list): String list object with data referring to the Accelerometer on the Y axis.
    accelerometerZ (list): String list object with data referring to the Accelerometer on the Z axis.
    gyroX (list): String list object with the data referring to the Gyro on the X axis.
    gyroY (list): String list object with data referring to the Gyro on the Y axis.
    gyroZ (list): String list object with data referring to the Gyro on the Z axis.

    Returns:
    File in xlsx with the processed data.
    """
    dataFrame = pd.DataFrame()

    dataFrame['ID'] = id
    dataFrame['HR'] = hr
    dataFrame['RRInterval'] = rrInterval
    dataFrame['Temperature'] = temperature
    dataFrame['AccelerometerX'] = accelerometerX
    dataFrame['AccelerometerY'] = accelerometerY
    dataFrame['AccelerometerZ'] = accelerometerZ
    dataFrame['GyroX'] = gyroX
    dataFrame['GyroY'] = gyroY
    dataFrame['GyroZ'] = gyroZ

    file_name = export_dir + r'/'+strMetadata+'capture_xlsx.xlsx'

    dataFrame.to_excel(file_name, index=False)


def CheckExportPath(dir: str):
    # Check whether the specified path exists or not
    isExist = os.path.exists(dir)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dir)
