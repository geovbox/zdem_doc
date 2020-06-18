.. index:: ! vbox2jpg

vbox2jpg
========


.. note::

   同 ``vboxplot`` 

:说明: 读取VBOX生成的 ``all_*.dat`` 文件绘制如 ``jpg`` 格式的图片

:实例:

::

    vbox2jpg --dir=./data --ymin=0.0 --xmin=0.0 --xmove=-1000.0 --ymove=-1000.0 --linewidth=0.8 --fontsize=8 --xmax=50000.0 --ymax=10000.0 --dpi=600 --pagesize=14 --topshow=false --rightshow=false


必选选项
--------

``--dir=<dir>``
    指定 ``all_*.dat`` 数据所在目录，``<dir>`` 为 ``all_*.dat`` 所在目录。例如``./data``


可选选项
--------

``--xmax=<float>``
    设置绘图坐标x轴最大值

``--ymax=<float>``
    设置绘图坐标Y轴最大值
    
``--xmin=<float>``
    绘图X最小值，默认0.0

``--ymin=<float>``
    绘图Y最小值，默认0.0

``--xmove=<float>``
    坐标沿x轴偏移量，默认0.0

``--ymove=<float>``
    坐标沿y轴偏移量，默认0.0

``--major_locator=<float>``
    主坐标刻度间隔，默认10000.0
    
``--minor_locator=<float>``
    次坐标刻度间隔，默认1000.0
    
``--fontsize=<int>``
    坐标刻度字体大小，默认9
    
``--max_workers=<float>``
    并行进程数，默认24

``--dpi=<int>``
    图片分辨率，默认600

``--linewidth=<float>``
    线条粗细，默认0.8

``--pagesize=<int>``
    图片大小，单位cm，默认14

``--leftshow=<bool>``
    显示坐标轴左线框，取值true/false，默认true

``--rightshow=<bool>``
    显示坐标轴左线框，取值true/false，默认true

``--bottomshow=<bool>``
    显示坐标轴左线框，取值true/false，默认true

``--topshow=<bool>``
    显示坐标轴左线框，取值true/false，默认true

``--wallshow=<bool>``
    显示wall墙，取值true/false，默认true

- 实例 ``vbox2jpg --dir=./data``
    读取目录 ``./data`` 中的计算数据 ``all_*.dat`` ，并生成 ``jpg`` 格式的图片，保存到 ``./data`` 中。

- 实例 ``vbox2jpg --dir=./data --xmax=40000.0 --ymax=10000.0`` 
    读取目录 ``./data`` 中的计算数据 ``all_*.dat`` ，并生成 ``jpg`` 格式的图片，保存到 ``./data`` 中。图片X轴最大值为40000.0, y轴最大值为10000.0





