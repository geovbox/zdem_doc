.. index:: ! vbox2jpg

vbox2jpg
========


.. note::

   同 ``vboxplot`` 

:说明: 读取VBOX生成的 ``all_*.dat`` 文件绘制如 ``jpg`` ``pdf`` 等格式的图片


必选选项
--------

``--dir=<dir>``
    指定 ``all_*.dat`` 数据所在目录，``<dir>`` 为 ``all_*.dat`` 所在目录。


可选选项
--------

``--xmax=<float>``
    设置绘图坐标x轴最大值

``--ymax=<float>``
    设置绘图坐标Y轴最大值


    
- 实例 ``vbox2jpg --dir=./data``
    读取目录 ``./data`` 中的计算数据 ``all_*.dat`` ，并生成 ``jpg`` 格式的图片，保存到 ``./data`` 中。

- 实例 ``vbox2jpg --dir=./data --xmax=40000.0 --ymax=10000.0`` 
    读取目录 ``./data`` 中的计算数据 ``all_*.dat`` ，并生成 ``jpg`` 格式的图片，保存到 ``./data`` 中。图片X轴最大值为40000.0, y轴最大值为10000.0





