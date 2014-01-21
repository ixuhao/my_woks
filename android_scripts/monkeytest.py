# coding: utf-8
# Last modified: 2014 Jan 21 01:28:31 PM
# by xu hao


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import os

class monkeytest(object):

    def __init__(self, serial=None):
        self.serial = serial
        self.device = MonkeyRunner.waitForConnection(timeout=10, deviceId=serial)
        self.devicetype = 'default' # default device type

    def getDirs(self):
        self.work_dir = 'path/to/files'
        self.imgs = os.path.join('screens', self.devicetype)
        self.screens = os.path.join(self.work_dir, self.imgs)

    def tap(self, coor):
        self.device.touch(coor[0], coor[1], MonkeyDevice.DOWN_AND_UP)

    def rest(self, sec):
        MonkeyRunner.sleep(sec)

    def wakeup(self):
        self.device.wake()

    def unlockScreen(self):
        self.device.shell("input keyevent 82")

    def runcmd(self, cmd):
        return self.device.shell(cmd)

    def screenshot(self, img):
        self.img = self.device.takeSnapshot()
        self.img.writeToFile(os.path.join(self.imgs, img), 'png')

    def compImg(self, name, perc=0.8):
        img = name + '.png'
        self.template = MonkeyRunner.loadImageFromFile(os.path.join(self.screens, img))
        self.img = self.device.takeSnapshot()
        return self.img.sameAs(self.template, perc)

    def compSubImg(self, subname, rect, perc=0.8):
        subimg = subname + '.png'
        self.template = MonkeyRunner.loadImageFromFile(os.path.join(self.screens, subimg))
        self.img = self.device.takeSnapshot()
        self.sub = self.img.getSubImage(rect)
        return self.sub.sameAs(self.template, perc)

if __name__ == '__main__':
    DEVICE_SERIAL_NUMBER = "0123456789x2345"
    ad = monkeytest(DEVICE_SERIAL_NUMBER)
    ad.getDirs() # set up working dirs
    ad.wakeup()
    ad.rest(2)
    ad.unlockScreen()

    # test start-to-final, just go into settings.
    #ad.runcmd("am start -n com.android.settings/.Settings") # is another way
    ad.device.startActivity(component="com.android.settings/.Settings")
    ad.rest(2)

    # dumpsys: mFocusedActivity
    print ad.runcmd("dumpsys activity activities | grep mFocusedActivity")

    # comparing screens
    if ad.compImg('settings'):
        print "Pass, get Settings."
    else:
        print "Fail."

    settings_title = (21, 52, 123, 54) # default
    # rect tuple is a short cut for testing, better use cv.
    if ad.compSubImg("settings_title", settings_title):
        print "Pass, Find Settings' title."
    else:
        print "Failed."
    # do not forget unittest :)
