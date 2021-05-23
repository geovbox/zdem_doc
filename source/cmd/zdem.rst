.. index:: ! zdem
.. _zdem:

zdem
====

:说明: ``zdem`` 主程序。

:使用方法:

``zdem [可选项] [script.py]`` 

 ``script.py`` 为 ``ASCII`` 码格式文件，例如　``zdem script.py``　，即可运行脚本 ``script.py`` 。

可选项
------

``-g`` , ``--grid`` SIZE 
    配合-s选项，设置应力应变计算时候，网格的大小，默认200.0
``-h`` , ``--hlep``
    显示帮助信息
``-j`` NUM
    并行计算开辟的线程数NUM，默认使用OMP_NUM_THREADS，
    如未设置OMP_NUM_THREADS，则使用全部CPU物理核心数并行计算。

``-s``, ``--strin-stres``  DataDir 
    计算应力应变
    从DataDir读取数据，将应力应变输出到DataDir/ss目录
``-v``, ``--version``
    打印版本信息

实例
----

``zdem -v``

::

    *************************************************************
        zdem 2.0(2021-04-19)  
        官网: www.geovbox.com 
        邮箱: sheng0619@163.com 
        Copyright © zdem, 2019/2021
    *************************************************************

``zdem -h``
    打印帮助文档
``zdem -j 8 script.py``　
    使用8个线程并行计算 ``script.py``
``zdem -s ./data``　
    读取 ``./data`` 中的数据计算应力应变 ，应力应变数据默认保存到了 ``./data/ss/data`` 中。参考应力应变  :ref:`no_add_del` 和 :ref:`add_del` 



