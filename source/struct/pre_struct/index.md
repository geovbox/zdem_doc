---
title: 先存断层设置
date: 2019-01-20
categories:
    - 示例
tags:
    - 断层
authors:
    - 李长圣
images:
    - 2.png
commands:
    - range
    - P4
---

{{% notice info %}}
数据下载：[pre_struct.py](/example/pre_struct/pre_struct.py)
[pre_struct.gif](/example/pre_struct/pre_struct.gif)
{{% /notice %}}


这里是一个 `断层` 设置的实例，一般地，将断层设置为没有粘结，类似松散石英砂，摩擦系数则可以设置为 0.0。

## 在终端或 `xshell` 中运行 `vboxdaily pre_struct.py` 
 [syn_erosion.py.py](/example/pre_struct/pre_struct.py) 中内容如下：

{{< include-code "pre_struct.py" bash >}}

得到的演化过程如下：

<h5></h5>
{{< figure src="/example/pre_struct/pre_struct.gif" title="" width="600px" >}}

{{< figure src="/example/pre_struct/0.png" title="" width="600px" >}}
{{< figure src="/example/pre_struct/1.png" title="" width="600px" >}}
{{< figure src="/example/pre_struct/2.png" title="" width="600px" >}}

<center><h5>单位 (km)<br><br>构造演化过程</h5></center>



