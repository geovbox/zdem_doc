.. _push_add_del:

实例
====

1. ``sbatch jobs1.sh`` 提交，将完成6.2.2 :ref:`ss_process` 1和2
2. **此步最关键!** 新建datass文件夹，将需要处理的dat复制到datass文件夹，完成6.2.2  :ref:`ss_process` 3。
完成此步后，目录结构：

::

    |-- ex1
        |-- job1.sh
        |-- job2.sh
        |-- push_add_del.py
        |-- data
            |--  all_0000000000_ini.dat
            |--  all_0000001000.dat    
            |--  ...    
            |--  all_0000005000.dat    
            |--  all_0000005000_ini.dat
            |--  all_0000006000.dat    
            |--  all_0000006000_ini.dat
            |--  all_0000016000.dat    
            |--  all_0000026000.dat    
            |--  all_0000036000.dat    
            |--  all_0000036000_ini.dat
            |--  all_0000046000.dat    
            |--  all_0000056000.dat    
            |--  all_0000056000_ini.dat
            |--  all_0000056100.dat    
            |--  ...
            |--  all_0000057900.dat    
            |--  all_0000058000.dat    
            |--  all_0000058000_ini.dat
            |--  all_0000068000.dat    
            |--  all_0000078000.dat    
            |--  all_0000088000.dat    
            |--  all_0000098000.dat    
            |--  all_0000108000.dat    
        |-- datass
            |-- all_0000006000_ini.dat
            |-- all_0000026000.dat
            |-- all_0000036000_ini.dat
            |-- all_0000056000.dat
            |-- all_0000058000_ini.dat
            |-- all_0000078000.dat
            |-- all_0000108000.dat
3. ``sbatch jobs2.sh`` 提交，将完成上节  :ref:`ss_process` 4和5


.. figure:: strainstressShear250.png
  :width: 60%
  :align: center
  
.. figure:: all0000108000.jpg
  :width: 60%
  :align: center

  **处理结果示意图**

文件内容：

``job1.sh``

.. literalinclude::  job1.sh

``job2.sh``

.. literalinclude::  job2.sh

``push_add_del.py``

.. literalinclude::  push_add_del.py

