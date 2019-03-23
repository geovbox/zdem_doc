简介
====

- VBOX是什么

    ``VBOX`` ，全称 ``Virtual sandBOX`` ，即虚拟沙箱软件，是一个用于构造变形研究的二维离散元软件。始于2014年，采用C语言编写，并用OpenMP完成了并行设计，已获软件著作权。主要面向构造模拟，用来补充构造物理沙箱实验在应力应变及材料选取上的局限性，为构造变形研究提供一种新的方法。

- VBOX的历史

    - 2015年，李长圣开发了VBOX的最原始版本VBOX 1.0；
    - 2018年8月10日，VBOX 1.3发布；
    - 目前最新版本 VBOX |VBOX_latest_release|
      发布于 |VBOX_latest_release_date|\ 。


- VBOX开发者

    VBOX源码由 `李长圣 <https://geovbox.com/about/lichangsheng/>`_ 开发并负责维护。

.. figure:: /images/LiChangSheng.png
   :width: 20%
   :align: center

   VBOX的维护者


- VBOX的特点

    为什么选择VBOX作为构造模拟呢？因为VBOX有如下特点：

    #. 免费

       VBOX是免费软件，托管在南京大学高性能计算中心，任何人均可使用。


    #. 使用门槛低

       命令参数采用PFC4.0类似参数，并配有丰富的测试、休止角、三轴、构造模拟等相关实例。


    #. 面向构造变形研究

       针对构造中的速度不连续面等编写了相应的模块，让构造模拟更方便。


    #. 高性能

       采用C语言，基于OpenMP完成并行设计。


    #. 跨平台

       支持linux和windows操作系统，官方提供ubuntu14.04 和 windows7, windows10 支持。

    #. 模块化

       VBOX遵循模块化设计思想，将不同的接触力学模型划分到不同的模块中。
       当前支持固体晶格模型，线弹模型及赫兹模型。
       这样的模块化设计有很多优点：

       - 只需要少量的模块
       - 各个模块之间相互独立且代码量少，易于更新和维护


    #. 支持多种格式的高精度矢量图和位图

       VBOX支持多种高精度的矢量图片格式和位图图片格式。

       - VTK格式：`ParaView <https://www.paraview.org/>`_ 支持，可以直接观看制作动画，修改配色等其他操作
       - 矢量图片格式，如PDF、PS、EPS和SVG，具有任意放大缩小而不失真的特性，可直接投稿到学术期刊
       - 位图图片格式，如BMP、JPG、PNG、PPM和TIFF格式，可用于日常的文档及演示

- VBOX替代品

    在构造模拟方面，还有一些软件也可以实现类似的功能，可以作为VBOX的替代品。

    #. PFC2D: `PFC2D <https://www.itascacg.com/software/pfc>`_
    #. Yade: `手册 <https://yade-dem.org/doc/>`_ | `代码下载 <https://launchpad.net/yade/>`_
    #. MatDEM: `MatDEM <http://matdem.com>`_
    #. DICE2D: `DICE2D <http://www.dembox.org>`_

.. TODO::

    介绍更多VBOX替代品，如 TRUBAL, RICEBAL等。
