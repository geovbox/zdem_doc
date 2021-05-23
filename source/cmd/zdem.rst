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

``--addball`` 
    配合-s选项，应力应变计算过程中，有新颗粒加入体系（沉积）,默认关闭。
``--delball`` 
    配合-s选项，应力应变计算过程中，删除了颗粒（剥蚀），默认关闭。
``-g`` , ``--grid`` SIZE 
    配合-s选项，设置应力应变计算时候，网格的大小SIZE，默认200.0
``-h`` , ``--hlep``
    显示帮助信息
``-j`` NUM
    并行计算开辟的线程数NUM，默认使用OMP_NUM_THREADS，
    如未设置OMP_NUM_THREADS，则使用全部CPU物理核心数并行计算。
``--leftwallid`` ID
    配合-s选项，设置左边墙ID，该墙左边颗粒均会被删除。如果颗粒被挤出到左边墙之外，需要设置该参数。
``--rightwallid`` ID
    配合-s选项，设置右边墙ID，该墙右边颗粒均会被删除。如果颗粒被挤出到右边墙之外，需要设置该参数。
``-s``, ``--strin-stres``  DataDir 
    计算应力应变
    从DataDir读取数据，将应力应变输出到DataDir/ss目录
``-v``, ``--version``
    打印版本信息
``--xmove`` X
    配合-s选项，设置模型x方向偏移位移X，默认0.0。
``--ymove`` Y
    配合-s选项，设置模型y方向偏移位移Y，默认0.0。


实例
----

``zdem -h``
    打印帮助文档
``zdem -j 8 script.py``　
    使用8个线程并行计算 ``script.py``
``zdem -s ./data``　
    读取 ``./data`` 中的数据计算应力应变 ，应力应变数据默认保存到了 ``./data/ss/data`` 中。参考应力应变  :ref:`no_add_del` 和 :ref:`add_del` 
``zdem --xmove -1000.0 --ymove -1000.0 -s ./data``　
    将模型向左移动1000.0, 向下移动1000.0，之后，计算应力应变。


