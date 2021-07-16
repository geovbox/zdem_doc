与物理模拟对比实验
==================

.. only:: html

   .. figure:: dem_am.gif
      :width: 60%
      :align: center
      
      **单位(cm)**

.. note::
    ~10万颗粒，~13万时步，16核并行(Intel Xeon E5-2650)，耗时 ~3小时 完成计算。

构建了一个典型离散元数值模拟(DEM)试验，对比与构造物理模拟(AM)和差异与相似点。

DEM与AM模拟结果较为一致，基本反映了AM中石英砂的变形行为。AM中材料选取有限（如硅胶、粘土、微玻璃珠等），而DEM材料选取范围大，但其模拟结果依赖参数选取。AM和DEM作为两种独立的方法，有很好的互补性 [Li2021]_ 。

数值模拟分两步进行：

1. ``gen.py``  生成颗粒，沉积，构建初始模型。 
2. ``push.py`` 给定颜色、粘结参数，挤压。 

**表 1  颗粒微观参数表.** [Li2021]_


+----------------+------------------------------+-------------------------------+------------------------------------+------------------+------------+-----------------------------------+-----------------------------+
| :math:`d(mm)`  | :math:`k(N \cdot m^{−1})`    | :math:`ρ(kg·\cdot m^{−2})`    | :math:`g(m·\cdot s^{−2})`          | :math:`f`        | :math:`μ`  | :math:`η(N \cdot s \cdot m^{−1})` | :math:`υ(m·\cdot s^{−1})`   |
+================+==============================+===============================+====================================+==================+============+===================================+=============================+
| 0.6            | 7.5e3                        | 1.3e3                         | 10.0                               |  0.4             |  0.3       | 0.04                              | 0.04                        |
+----------------+------------------------------+-------------------------------+------------------------------------+------------------+------------+-----------------------------------+-----------------------------+

`The particle packing consists of four particle sizes, with diameters and quantity ratio of 0.2 mm, 0.4 mm, 0.5 mm, and 0.6 mm and 2:2:1:1, respectively. :math:`d` , largest particle diameter. :math:`ρ` , particle density. :math:`g` , gravitational acceleration. :math: `f` , safety factor of the time step. :math:`k` , stiffness of the contact. :math:`μ` , friction coefficient. :math:`η` , dynamic viscosity. :math:`υ` , velocity of the mobile wall.`


``gen.py`` 

.. literalinclude:: gen.py

``push.py`` 

.. literalinclude:: push.py


计算结束后，将得到以下结果：

.. figure:: dem_and_am02.jpg
  :width: 60%
  :align: center

.. figure:: dem_and_am04.jpg
  :width: 60%
  :align: center

.. figure:: dem_and_am08.jpg
  :width: 60%
  :align: center

.. figure:: dem_and_am12.jpg
  :width: 60%
  :align: center

.. figure:: dem_and_am16.jpg
  :width: 60%
  :align: center

  **单位(cm)**


参考文献

.. [Li2021] `LI C.S., YIN H.W.*, et al. (2021) Calibration of the discrete element method and modelling of shortening experiments. Front. Earth Sci. 9:636512. <https://doi.org/10.3389/feart.2021.636512>`_


