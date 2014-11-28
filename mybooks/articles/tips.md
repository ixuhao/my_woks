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

    acquire::http::proxy "http://hao_xu:Qwer!234@proxy.neusoft.com:8080";

* .npmrc

    $ npm config set key value

    > proxy=http://hao_xu:Qwer!234@proxy.neusoft.com:8080/
    > http_proxy=http://hao_xu:Qwer!234@proxy.neusoft.com:8080

* pip

still not work

```bash
$ pip search package --proxy "user:password@proxt.server:port"
```
