ReadMe
======

# Introduction

Here are my daily notes.

Read List:

[Docker终极指南](http://my.oschina.net/u/1788105/blog/366701)

[Docker最新安全性能调整分析](http://dockerone.com/article/243)

[docker高级应用之动态扩展容器空间大小](http://dl528888.blog.51cto.com/2382721/1606170)

http://jpetazzo.github.io/2014/01/29/docker-device-mapper-resize/

[有了 Docker，用 JavaScript 框架开发的 Web 站点也能很好地支持网络爬虫的内容抓取](http://dockerone.com/article/279)

[Running gitlist (or gitweb) with Gitolite](https://www.marcus-povey.co.uk/2013/10/03/running-gitlist-or-gitweb-with-gitolite/)

[Spark Local Cloud on Raspberry Pi](https://www.gitbook.com/book/kennethlimcp/spark-local-cloud-on-raspberry-pi/details)

# Working

[cvtest/simplecv warp.ipynb](./files/simplecv_warp.ipynb)

# Markdown

http://wowubuntu.com/markdown

# rsync

http://wiki.ubuntu.com.cn/UbuntuHelp:Rsync/zh

http://www.unixtutorial.org/2008/09/how-to-synchronize-directories-with-rsync/

```bash
ubuntu$ rsync -avz --stats  /tmp/dir1/ /tmp/dir2
```

http://ubuntuforums.org/showthread.php?t=1632562

```bash
#!/bin/bash
#check if the dir exists
if [ -d /media/USB2  ]
then
rsync -acv --delete /home/randy/Documents/ /media/USB2/testbackup/
else
echo "USB2 is not connected, exiting..."
fi
```

[Linux系统下如何使用rsync进行数据同步](http://www.oschina.net/question/12_7446)

http://wiki.ubuntu.com.cn/UbuntuHelp:Unison

# Reading List

* USB Reverse Tethering

http://forum.xda-developers.com/showthread.php?t=2287494

http://community.linuxmint.com/tutorial/view/1524

http://www.wikihow.com/Reverse-Tether-an-Android-Phone

http://tech4bros.com/android-reverse-tethering-how-to-connect-pc-internet-to-android-mobile/

* 苹果优山美地 JavaScript 自动化实例

http://blog.jobbole.com/80002/

http://developer.telerik.com/featured/nativescript-a-technical-overview/

* pyramid

[pyramidoc中文官方文档](http://pyramidoc.lofter.com/)

* python

[Python: Tips, Tricks and Idioms - Part 2 - Decorators and context Managers](https://codefisher.org/catch/blog/2015/02/10/python-decorators-and-context-managers/)

[Asynchronous Python and Databases](http://techspot.zzzeek.org/2015/02/15/asynchronous-python-and-databases/)

[asyncio](https://docs.python.org/3/library/asyncio.html)

[aiohttp doc](http://aiohttp.readthedocs.org/en/latest/index.html)

[API-Hour](https://github.com/Eyepea/API-Hour)

* tools

[wrk: Modern HTTP benchmarking tool](https://github.com/wg/wrk)

[wrk2: a HTTP benchmarking tool based mostly on wrk](https://github.com/giltene/wrk2)

[zope2 virtual hosting](http://docs.zope.org/zope2/zope2book/VirtualHosting.html)

[Plone virtual hosting](http://docs.plone.org/manage/deploying/production/ubuntu_production.html#step-5-set-up-virtual-hosting)

[docker-plone](https://github.com/gauthierc/Docker/blob/master/Plone/Dockerfile)

[HAProxy: ebtree](http://tech.uc.cn/?p=1031)

[千万级并发HAproxy均衡负载系统介绍](http://www.oschina.net/question/17_8785)

[pyrsslocal: Rss Reader link greader](http://www.xavierdupre.fr/app/pyrsslocal/helpsphinx/index.html)

# Testing

* Android Security

[Android Activtity Security](http://drops.wooyun.org/tips/3936)

[一次app抓包引发的Android分析记录](http://drops.wooyun.org/tips/2871)

[关于zANTI和dsploit两款安卓安全工具的对比](http://drops.wooyun.org/mobile/2503)

[android测试环境搭建](http://drops.wooyun.org/tips/2624)

[Burp Suite使用介绍](http://drops.wooyun.org/tools/1548)

# CV

[Geometric Image Transformations](http://docs.opencv.org/modules/imgproc/doc/geometric_transformations.html)

[SimpleCV TransformPerspective](http://www.simplecv.org/docs/SimpleCV.html#i/SimpleCV.ImageClass.Image/transformPerspective)

[Building a Pokedex in Python: Getting Started](http://www.pyimagesearch.com/2014/03/10/building-pokedex-python-getting-started-step-1-6/)

[4 Point OpenCV getPerspective Transform Example](http://www.tuicool.com/articles/UNRzQbq)

[warping brien](http://uberhip.com/python/image-processing/opencv/2014/10/26/warping-brien/)

# docker

http://www.dockerpool.com/books

set proxy for daemon in /etc/default/docker

# haha

[tangyouyou](http://ww1.sinaimg.cn/bmiddle/61add42ajw1en35qmme5kg209604qhdx.gif)

# raspberry pi

[pi personal cloud](http://www.itproportal.com/2014/08/02/how-to-transform-the-raspberry-pi-into-your-personal-cloud-for-secure-file-access-anywhere/)

tonido is a service in USA, so.... 

owncloud, cozy, nimbus, BitTorrent Sync

http://jack.minardi.org/raspberry_pi/replace-dropbox-with-bittorrent-sync-and-a-raspberry-pi/

http://www.hongkiat.com/blog/free-tools-to-build-personal-cloud/

[40+ Cool Ideas for your Raspberry PI Project](http://pingbin.com/2012/12/30-cool-ideas-raspberry-pi-project/)

# 20141212

## How to choose some items from a list - calculate money...

Today, I get 823 and have to get 600 from these numers.

```python
import itertools

# taxi tickets
a = [80, 80, 80, 78, 77, 72, 65, 63, 63, 58, 54, 53]

# the number to collect
target = 600

s = sum(a) - target

n = 3 # obivious

# use combinations_with_replacement to get a list
result = list(itertools.combinations_with_replacement(a, n))

b = []

for i in result:
    b.append(abs(s - sum(i)))

for k, i in enumerate(b):
    if i == 0: # there it is.
        print k, result[k]
```
