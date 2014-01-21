# coding: utf-8
# Last modified: 2014 Jan 21 01:22:57 PM

import os
import time

DEVICE_SERIAL_NUMBER = "0123456789x2345" # dummy

def adb(command):
    waitForDevice()
    # get output
    return os.popen('adb -s %s %s' % (DEVICE_SERIAL_NUMBER, command))

def adbshell(command):
    return adb('shell %s' % command)

def waitForDevice():
    os.system("adb -s %s wait-for-device" % (DEVICE_SERIAL_NUMBER))

def adbNoSerial(command):
    # return output of command
    return os.popen('adb %s' % command)

def pushFile(sourcePath, destPath):
    adb("push %(source)s %(dest)s" % ({ "source" : sourcePath, "dest" : destPath }))

def root():
    response = adb("root").readline().strip()
    if response != "adbd is already running as root":
        time.sleep(10)

def pressBack():
    adbshell("input keyevent 4")

def pressHome():
    adbshell("input keyevent 3")

def pressPowerButton():
    adbshell("input keyevent 26")

def unlockScreen():
    adbshell("input keyevent 82")

def batteryLevel():
    powerlevel = adbshell("dumpsys battery")
    for i in powerlevel:
        if 'level' in i:
            return i

def getAdbDevices():
    devices = []

    output = adbNoSerial("devices")
    for line in output:
        dsn = line.split()
        if len(dsn) == 2:
            devices.append(dsn[0])
    return devices

def triggerSettings():
    # using activity manager
    adbshell("am start -n com.android.settings/.Settings")

if __name__ == '__main__':
    print getAdbDevices()
    pressPowerButton()
    unlockScreen()
    print batteryLevel()
    time.sleep(3)
    triggerSettings()
    time.sleep(2)
    pressHome()
