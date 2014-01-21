# coding: utf-8
# Last modified: 2014 Jan 21 01:25:43 PM
# easily extended with logging, threading, etc.

import os
import subprocess
import time

class ADB(object):
    adb = 'adb'
    serial = None

    def __init__(self, path='', serial=None):

        if serial is not None:
            self.serial = serial
            self.adb = '%s -s %s' % (self.adb, serial)
        self.worker = Worker()

    def shell(self, cmd=None):
        """
        """
        if cmd is None:
            return -1
        r = self.worker.run('%s shell %s' % (self.adb, cmd))
        if r[0] != 0:
            print "shell error <%s>" % r[1]
        return r

    def pressPowerButton(self):
        return self.shell("input keyevent 26")

    def unlockScreen(self):
        return self.shell("input keyevent 82")

    def batteryLevel(self):
        return self.shell("dumpsys battery")[1]

class Worker(object):

    def __init__(self):
        self.stdout = None
        self.stderr = None

    def run(self, cmd):
        self.cmd = cmd
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        shell=True)
        self.stdout, self.stderr = proc.communicate()

        return proc.returncode, self.stdout, self.stderr


if __name__ == '__main__':
    #worker = Worker()
    #print worker.run('pwd')
    DEVICE_SERIAL_NUMBER = "0123456789x2345"
    device = ADB(DEVICE_SERIAL_NUMBER)
    print device.serial
    #device.pressPowerButton()
    #device.unlockScreen()
    print device.batteryLevel()
