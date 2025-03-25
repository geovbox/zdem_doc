古隆起
======

这里是一个 ``古隆起`` 设置的实例，将古隆起的 x,y,spin（角速度）固定。

 ``ex6`` 目录中文件有
 
- `lsf.sh <lsf.sh>`_
- `palaeohigh.py <palaeohigh.py>`_
- `init_xyr.dat <init_xyr.dat>`_



## 进入 `ex6` 目录，在终端或 `xshell` 中运行 ::

   $ bsub < lsf.sh   # 提交计算
   $ bjobs           # 查看计算是否提交成功


``lsf.sh`` 中内容如下：

.. literalinclude:: lsf.sh

``palaeohigh.py`` 中内容如下：

.. literalinclude:: palaeohigh.py

计算结束后，将得到以下结果：


.. only:: html

   .. figure:: palaeohigh.gif
      :width: 60%
      :align: center


.. figure:: 00.jpg
  :width: 60%
  :align: center

.. figure:: 05.jpg
  :width: 60%
  :align: center

.. figure:: 10.jpg
  :width: 60%
  :align: center

  **单位(km)**






