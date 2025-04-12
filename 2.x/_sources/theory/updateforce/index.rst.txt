接触力的计算
============


自从 Cundall 和 Strack 给出了对颗粒物质进行离散模拟的思路，各个学科领域的学者提出了各种适用于不同问题的 DEM 接触力学模型。自然界中，颗粒间的作用力往往是非线性的，真实的再现自然界中的颗粒行为，需要构建复杂的接触力学模型，相应的求解接触力也需要更大的计算量。然而，一些简化的接触力学模型，也可以解释一些自然界中的岩土体相互作用的机制，如断层传播时的脉冲滑动行为 [Place1999]_ 、高孔隙度砂岩中不同形态压密带的形成机制 [Liu2015]_ 等。这里，我们将详细阐述每种接触模型的实现方法，以往研究中，不同的接触模型往往采用不同的粘结模型。将粘结模型和接触模型作为一整体，将从接触模型、粘结模型和计算实例三个方面给出实现方法。 

首先区分一下粘结和接触的区别，如果两颗粒间的圆心距离小于等于两颗粒半径之和，则认为两颗粒是相互接触的。离散元初始模型生成后，相互接触的颗粒间生成粘结，粘结的信息放入粘结链表，粘结有抗拉和剪切强度，整个计算过程粘结往往只生成一次。两个颗粒间的粘结断裂之后，如果再次接触，则接触信息放入无粘结接触链表，无粘结接触没有抗拉和抗剪强度（`Fig 7.3`_） 。


  
.. _Fig 7.3:
.. figure:: contact_and_bond.png
  :width: 60%
  :align: center
  
  **接触与粘结关系** 
  


本文涉及的接触模型分成两类线弹性模型和 Hertz-Mindlin 模型。

.. _liner:

线弹性模型
----------
Cundall 和 Strack(Cundall and Strack,1979)于 1979 年的给出线弹性模型，该模型是 DEM
中最基本的接触力学模型， 基本上所有的离散元软件中嵌入了该模型(Cundall and Strack,1979; 
Cundall P A,1988a; Itasca Consulting Group,2008; Itasca Consulting Group,2012b; Šmilauer et 
al.,2018)。与之后 PFC2D(Itasca Consulting Group,2008)中接触点的描述略微不同。这里采用
PFC2D 中的描述的线弹性接触模型。 详见　[Li2019]_

Hertz-Mindlin 模型
------------------
Hertz 模型中，颗粒为一个球，而不再是之前的圆盘。模型提供了颗粒挤压状态下的法向
力的计算方法，不提供拉伸状态下法向力计算方法。Cundall 描述的 Hertz_Mindlin 接触模型
(Cundall P A,1988a)是 Mindlin 和 Deresiewicz 理论模型(Mindlin,1953)的近似，是一种非线性
接触模型。法向力采用公式(2-12)计算，切向力采用公式(2-15)计算，考虑颗粒转动。详见　[Li2019]_


.. [Place1999] Place D, Mora P (1999) The lattice solid model to simulate the physics of rocks and earthquakes: incorporation of friction. Journal of Computational Physics 150:332-372(ISSN 0021-9991)

.. [Liu2015] Liu C, Pollard DD, Gu K, Shi B (2015) Mechanism of formation of wiggly compaction bands in porous sandstone: 2. Numerical simulation using discrete element method. Journal of Geophysical Research: Solid Earth 120:8153-8168(ISSN 2169-9356)

.. [Li2019] 李长圣 (2019) 基于离散元的褶皱冲断带构造变形定量分析与模拟. 南京大学


