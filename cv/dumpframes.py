# coding: utf-8
# Last modified: 2014 Jan 17 03:53:24 PM
# xh

import os
from SimpleCV import VirtualCamera, Display, Color, Stream

video_name = "/home/xuhao/screenrecord/sample_1M.MP4"
out_dir = os.path.join(os.curdir, "temp")
vc = VirtualCamera(video_name, "video")
disp = Display((960, 600))
frame = 0
while (disp.isNotDone()):
    img = vc.getImage()
    #img.drawText("img Frame # " + str(frame), 15, 50, color=Color.WHITE, fontsize=60)
    img.save(disp)
    img_name = "img_%d.png" % frame
    img.save(os.path.join(out_dir, img_name))
    frame += 1

