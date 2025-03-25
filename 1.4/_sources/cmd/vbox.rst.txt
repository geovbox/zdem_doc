.. index:: ! vbox

vbox
====

:说明: ``VBOX`` 主程序。

:使用方法:

``vbox [可选项] [script.py]`` 

其中，　``script.py`` 为脚本名，如　``vbox script.py``　，运行脚本 ``script.py`` , ``cmd.txt`` 为 ``ASCII`` 码格式文件。

可选项
------

``-g`` , ``--grid`` SIZE (完善中...)
    配合-s选项，设置应力应变计算时候，网格的大小，默认200.0
``-h`` , --hlep
    显示帮助信息
``-j`` NUM
    并行计算开辟的线程数NUM，默认使用OMP_NUM_THREADS，
    如未设置OMP_NUM_THREADS，则使用全部CPU物理核心数并行计算。

``-s``, ``--strin-stres``  DataDir  (完善中...)
    计算应力应变
    从DataDir读取数据，将应力应变输出到DataDir/ss目录
``-v``, ``--version``
    打印版本信息

:实例:

``vbox -v``

::

    *************************************************************
        Virtual SandBox(2D) version 1.4(2020-03-19) 教育版 
        官网: www.geovbox.com 
        邮箱: sheng0619@163.com 
        Copyright © 南京大学, 2014/2019
        Copyright © VBOX, 2019/2020
    *************************************************************

``vbox -h``

``vbox -j 8 script.py``　使用8个线程并行计算

``vbox -s ./data``　读取 ``./data`` 中的数据计算应力应变



