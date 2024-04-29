离散元原理
##########


二十世纪七十年代，基于分子动力学原理，[Cundall1979]_ 首先提出了对颗粒物质进行
离散模拟的思路，用于研究岩土体的各种力学行为，其基本思想是将颗粒材料内部细观尺度
的单个离散颗粒视为一个离散单元，将颗粒集合体模型视为若干离散单元的集合，通过一系
列离散的单元来模拟颗粒材料的力学行为。 离散元法假设单元为刚性
的，不可变形；单元相互作用通过弹簧阻尼器和滑动摩擦器产生的力体现；每一个时步内，
速度和加速度是常数，这要求时间步足够小，同时保证一个时步内，单元只能以很小的位移
与其相邻单元相互作用。


.. raw:: latex

   \addtocontents{toc}{\protect\setcounter{tocdepth}{2}}
   \setcounter{secnumdepth}{2}

.. toctree::
   :maxdepth: 2
   :caption: 离散元原理
   
   miniDEM/index
   updatepostion/index
   updateforce/index

.. [Cundall1979] Cundall PA, Strack OD (1979) A discrete numerical model for granular assemblies. Geotechnique 29:47-65. https://doi.org/10.1680/geot.1979.29.1.47 (ISSN 0016-8505)
