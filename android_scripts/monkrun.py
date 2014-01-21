# coding: utf-8
# Last modified: 2014 Jan 21 01:33:48 PM

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from datetime import datetime
import os

''' run test and take screen shot
width = 1920
height = 1200
'''

work_dir = 'path/to/files'
img_dir = os.path.join(work_dir, 'imgs')
test_round = 1

device = MonkeyRunner.waitForConnection()
#device = MonkeyRunner.waitForConnection(timeout=10)

print dir(MonkeyRunner) # loadImageFromFile

def takeimg(img):
    simg = device.takeSnapshot()
    simg.writeToFile(os.path.join(img_dir, img), 'png')

def tap(cor):
    device.touch(cor[0], cor[1], MonkeyDevice.DOWN_AND_UP)

MonkeyRunner.sleep(2)

home = {
        "games_btn":[188,88],
        "content":[],
        }

games = {
        "store_btn":[1090,111],
        "back_btn":[0.96464646, 0.564516, 0.0272727, 0.0516129],
        "home_btn":[0.9625,0.915,0.0317708333333,0.0625],
        "title" :[],
        }

store = {
        "back_btn":[551, 1874],
        "title":[]
        }

t = 0

while t < test_round:
    d = datetime.now()
    run_name = 't_%d_' % t + d.strftime('%Y%m%d_%H%M%S')
    run_dir = os.path.join(img_dir, run_name)
    if not os.path.exists(run_dir):
        os.mkdir(run_dir)
    # press home button to launcher
    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    print device.getProperty('am.current.comp.class')
    img = os.path.join(run_dir, 'home.png')
    takeimg(img)
    MonkeyRunner.sleep(1)

    # home -> games
    tap(home['games_btn'])
    MonkeyRunner.sleep(4)
    print device.getProperty('am.current.comp.class')
    img = os.path.join(run_dir, 'games.png')
    takeimg(img)
    MonkeyRunner.sleep(1)

    # games -> store
    tap(games['store_btn'])
    MonkeyRunner.sleep(8)
    print device.getProperty('am.current.comp.class')
    img = os.path.join(run_dir, 'store.png')
    takeimg(img)
    MonkeyRunner.sleep(4)

    # store -> games
    #device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    tap(store['back_btn'])
    MonkeyRunner.sleep(4)
    print '-----------------'
    print device.getProperty('am.current.comp.class')
    print device.getProperty('am.current.comp.package')
    print '-----------------'
    MonkeyRunner.sleep(1)

    # games -> home
    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)
    print device.getProperty('am.current.comp.class')

    t += 1

