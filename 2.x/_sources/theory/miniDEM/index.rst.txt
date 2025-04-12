最小的离散元程序
================


[Zhao2015]_ 用 45 行MATLAB的离散元代码模拟了伽利略的比萨斜塔试验，其前处理、求解器和后处理代码 `Code 7.1`_ :

**代码 7.1 伽利略的比萨斜塔试验（MATLAB)**

.. _Code 7.1:
.. literalinclude::  fall.m

比萨斜塔离散元模拟试验中，钢球和木球高度随时间的变化结果见 `Fig 7.1`_ ，可见钢球和木球是
同时落地的。 

.. _Fig 7.1:
.. figure:: fall.png
  :width: 60%
  :align: center

  **球高度随时间的变化，比萨斜塔离散元模拟试验。** 
  
.. _Fig 7.2:
.. figure:: DEMcyc.png
  :width: 60%
  :align: center
  
  **球高度随时间的变化，比萨斜塔离散元模拟试验。** 
  
离散元的求解实际上是迭代计算颗粒位移和受力， 可以概括为两部分，
如 `Fig 7.2`_ 所示。第一步，已知的颗粒所受合力和合力矩，由牛顿第二定律更新每个颗粒的位
置（如代码 `Code 7.1`_ 中，24~31 行） ；第二步，找到相互接触的颗粒，应用接触力学模型（即力-位
移法则，或者称本构模型。如代码 `Code 7.1`_  中，F_Ball_Steel=-G*M_Ball_Steel，该实例中，没有
颗粒相互作用，颗粒仅受重力作用，实际这里需要计算颗粒间的相互作用力）计算颗粒间的
接触力，进而得到所有颗粒受到的合力与合力矩。反复执行这两个步骤，直到计算结束。

.. [Zhao2015] Zhao G-F (2015) High performance computing and the discrete element model: opportunity and challenge. Elsevier, 
