# Tips

## ipython

[refer to it](http://www.windowsazure.cn/zh-cn/develop/python/tutorials/ipython-notebook/)

1. create profile

    ipython profile create nbserver

2. edit ~/.config/ipython/profile\_nbserver/ipython\_notebook\_config.py

2.1 password

    python -c "import IPython;print IPython.lib.passwd()"

2.2 certificated pem file

    openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem

3. run

    ipython notebook --profile=nbserver

## Git

git rm --cached <file>

git remote -v

git remote update xxx

## Ubuntu behind proxy

Configure software proxy settings in ubuntu after change my password.

* thunderbird
* System Setting -> network -> network proxy
* .bashrc
* .gitconfig
* /etc/apt/apt.conf

    Acquire::http::proxy "http://user:password@proxy.server:port";
    Acquire::https::proxy "http://user:password@uer:password@proxy.server:port";

  refer to [proxy authentication not working for HTTPS sources](https://bugs.launchpad.net/ubuntu/+source/apt/+bug/1087512)

* .npmrc

    $ npm config set key value

    > proxy=http://user:password@proxy.server:port/
    > http_proxy=http://user:password@proxy.server:port

    $ sudo npm update npm -g

* .curlrc

    > proxy=http://user:password@proxy.server:port/

* pip

still not work

```bash
$ pip search package --proxy "user:password@proxt.server:port"
```

## mplayer

mplayer

```bash
#!/bin/bash
mplayer -playlist ~/playlist.txt -loop 0
```

## android

screenshot

```bash
#!/bin/bash
adb shell screencap -p | sed 's/\r$//' > $1
```

press power

```bash
adb shell input keyevent 26
```

## ssh

ssh some server, bad practise.:P

```bash
#!/bin/bash
# ssh name1@192.168.100.131
read -p "Connect to (name1, name2, name3): " yn

if [ "$yn" == "name1" ]; then
    ssh name1@192.168.100.153
elif [ "$yn" == "name2" ]; then
    ssh name2@192.168.100.197
#elif [ "$yn" == "NO" ] || [ "$yn" == "no" ]; then
#    echo "Oh, interrupt!"
elif [ "$yn" == "name3" ]; then
    ssh name3@192.168.100.199
else
    echo "Don't know what your choice is"
    exit 0
fi
```

