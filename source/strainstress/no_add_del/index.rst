.. _no_add_del:

无沉积剥蚀
==========

如果没有沉积和剥蚀过程， ``sbatch jobs.sh`` 提交，应力应变将输出到 ``ex5_detachment/data/ss``。

这里采用 ``构造模拟`` 中的 :ref:`detachment` 示例


目录结构：

::

    | -- ex5_detachment
        | -- detachment.py
        | -- init_xyr.dat
        | -- job.sh

- ``detachment.py`` 见 :ref:`detachment`
- ``init_xyr.dat`` 见 :ref:`detachment`
- ``job.sh`` 内容如下：

    .. literalinclude::  job.sh

其中， 

- ``time`` 记录该行命令的运行时间，输出到 ``%j.err``
- ``zdem2jpg --dir=./data`` 生成jpg, 详解见 :ref:`zdem2jpg` 。
- ``zdem -s ./data`` 计算应力应变, 详解见 :ref:`zdem` 。
- ``zdemss --dir ./data`` 绘制应力应变， 详解见 :ref:`zdemss` 。



.. warning::

    本示例采用 Slurm 作业调度系统提交计算。 注意 ``job.sh`` 的行结尾符需采用 Unix 的 ``\n`` 格式，否则将产生如下错误信息：
    
    ::
    
        sbatch: error: Batch script contains DOS line breaks (\r\n)
        sbatch: error: instead of expected UNIX line breaks (\n).
    
    ``job.sh`` 中命令解析 及 如何修改 ``job.sh`` 的行结尾符 见 `第00课 并行超算云上使用ZDEM <https://www.bilibili.com/video/BV1m7411M7rz?p=1>`_ 的 10:15


.. figure:: strainstress300.jpg
  :width: 60%
  :align: center
  
.. figure:: all0000100000.jpg
  :width: 60%
  :align: center

  **处理结果示意图**

