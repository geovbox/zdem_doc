# ZDEM 2.x 手册

[![Deploy](https://github.com/geovbox/zdem_doc/actions/workflows/deploy.yml/badge.svg)](https://github.com/geovbox/zdem_doc/actions/workflows/deploy.yml)
[![Documentation version](https://img.shields.io/badge/版本-v2.x-blue.svg)](https://docs.geovbox.com/2.x/)
![Repository size](https://img.shields.io/github/repo-size/geovbox/zdem_doc)
[![Sphinx](https://img.shields.io/badge/Powered%20by-Sphinx-orange.svg)](http://www.sphinx-doc.org/)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.zh)

[在线阅读](https://docs.geovbox.com/2.x/) |
[PDF 下载](https://docs.geovbox.com/2.x/zdem_doc.pdf) |
[文档源码](https://github.com/geovbox/zdem_doc) |
[ZDEM 官方网站](https://geovbox.com)



欢迎来到 [ZDEM](https://geovbox.com/) 的世界，`ZDEM` 是一个用于构造模拟的二维离散元软件。

本项目开始于2019年初，由[李长圣](https://geovbox.com/lichangsheng/)维护的 `ZDEM` 手册，即可以作为日常参考，也可以作为离散与的入门读物。希望通过阅读本手册，能够让用户尽快掌握 `ZDEM` 的使用方法。

## 相关链接

- 官网：https://geovbox.com/
- 手册：https://doc.geovbox.com/

## 编译生成文档

- 网页版
	```
	$ make html
	$ firefox build/html/index.html&
	````
- PDF版
	```
	$ make latexpdf
	$ evince build/latex/vbox_doc.pdf&
	```
- 详细过程见 https://github.com/geovbox/zdem_doc/wiki

## 版本说明

- 在线阅读： https://doc.geovbox.com

文档的维护可以通过如下方式：

#. 发送相关建议或投稿至 `sheng0619@163.com`

## 致谢

[gmt-china](https://github.com/gmt-china) 的开源项目 [GMT_docs](https://github.com/gmt-china/GMT_docs)，对本手册的编写起到了很大的帮助作用。

## 许可协议

本作品采用 [知识共享署名-非商业性使用 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc/4.0/) 进行许可。任何人都可以自由地分享、修改本作品，但必须遵循如下条件：

- 署名：必须提到原作者，提供指向此许可协议的链接，表明是否有做修改
- 非商业性使用：不能对本作品进行任何形式的商业性使用
