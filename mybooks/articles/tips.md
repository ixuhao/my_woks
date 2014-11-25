# Tips

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

