# -*- coding: utf-8 -*-
"""
    Receiver Module.
    Module with implementations of functions for reading sensor data from a COM port.   
"""

import datetime


def DatetimeToAgeNumber(date: str):
    dob = datetime.datetime.strptime(date, '%d/%m/%Y')
    today = datetime.date.today()

    return today.year - dob.year - ((today.month, today.day) < (dob .month, dob .day))


def ProcessSelectedAnalysisMethod(option: str, age: str):
    return {
        '1': 220-(0.7*int(age)),
        '2': 211-(0.64*int(age)),
        '3': 220 - int(age)
    }.get(option, 220-(0.7*int(age)))  # Tanaka method will be returned default if option is not found
