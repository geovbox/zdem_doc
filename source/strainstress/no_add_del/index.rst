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

最后两行， 

- ``zdem -s ./data`` 计算应力应变
- ``zdemss --dir ./data`` 绘制应力应变。

.. warning::

    注意job.sh的行结尾符需采用 Unix 的 ``\n`` 格式，否则将产生如下错误信息：
    
    ::
    
        sbatch: error: Batch script contains DOS line breaks (\r\n)
        sbatch: error: instead of expected UNIX line breaks (\n).
    
    修改 ``job.sh`` 的行结尾符 见 `第00课 并行超算云上使用ZDEM <https://www.bilibili.com/video/BV1m7411M7rz?p=1>`_ 的 10:15

.. figure:: strainstress300.jpg
  :width: 60%
  :align: center
  
.. figure:: all0000100000.jpg
  :width: 60%
  :align: center

  **处理结果示意图**


