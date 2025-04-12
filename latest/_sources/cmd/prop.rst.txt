.. index:: ! prop
.. _prop:

prop
====

:说明: ``pro[p]`` 设置材料参数

可选选项
--------

``DENSITY=<float>``
    颗粒密度

``FRIC =<float>``
    颗粒密度

``SHEAR=<float>``
    颗粒密度

``POISS=<float>``
    颗粒密度

``DAMP=<float>``
    局部阻尼系数，见PFC2D 4.0手册或李长圣博士论文

``HERTZ``
    使用hertz接触模型

``xv=<float>``
    颗粒x方向速度

``yv=<float>``
    颗粒y方向速度
    
``spin=<float>``
    颗粒角速度


``ebmod=<float>``
    粘结的杨氏模量，ref. [李长圣博士论文,2019]

``gbmod=<float>``
    粘结的剪切模量，ref. [李长圣博士论文,2019]

``tstrength=<float>``
    粘结的抗拉强度，ref. [李长圣博士论文,2019]

``sstrength=<float>``
    粘结的聚合强度，ref. [李长圣博士论文,2019]


``n_bond=<float>``
    粘结的抗拉强度，ref. [PFC2D 4.0 手册]

``s_bond=<float>``
    粘结的抗剪强度，ref. [PFC2D 4.0 手册]



:使用方法:

::

   PROP DENSITY <float>, FRIC <float>, SHEAR <float>, POISS <float>, DAMP <float>, HERTZ [RANGE ...]
   PROP ebmod <float>, gbmod <float>, tstrength <float>, sstrength <float>, [tolerate 10.0] [fric <float>] [RANGE ...]
   PROP DENSITY <float>, FRIC <float>, KN <float>, KS <float> [tolerate rext 0.8] [RANGE ...]
   PROP n_bond <float> s_bond <float> [RANGE ...]
   PROP xv <float> yv <float> spin <float> [RANGE ...]

其中， ``tolerate`` 默认值为1e-6，``rext`` 默认值为1.0。 ``rext`` 可与 ``gline`` 的 cratio，联合使用，设置 ``rext=cratio``，可以避免0-1-2-3-4...线性叠合的颗粒，出现0-2跨颗粒1产生粘结。

:实例:

::

   # Model 1. ref. [Morgan 2015 JGR] 和 [李长圣博士论文,2019]
   # 设置材料参数 密度DEM，摩擦系数FRIC，剪切模量shear，泊松比poiss，阻尼DAMP
   PROP DENSITY 2.5e3, fric 0.3, shear 2.9e9, poiss 0.2, damp 0.4, HERTZ
   #设置 range x 1.0 10.0 y 1.0 10.0 中颗粒粘结在一起，使颗粒具有粘聚力 
   PROP ebmod 2e8 gbmod 2e8  tstrength 2e7 sstrength 4e7 fric 0.3 range x 1.0 10.0 y 1.0 10.0
   #
   # Model 2. ref. [PFC2D 4.0 手册] 和 [李长圣博士论文,2019]
   # 设置所有颗粒的材料参数 密度DEM，摩擦系数FRIC，法向刚度KN，切向刚度KS，阻尼DAMP 
   PROP DENSITY 2.5e3, KN 1e4, KS 1e4, FRIC 0.3, DAMP 0.4

   #
   #
   #设置( |OA| - (rO+rA)| ) <= tolerate的颗粒粘结在一起，使颗粒具有粘聚力 ,使得更多颗粒粘结到一起
   PROP n_bond 1.0e4 s_bond 1.0e4 tolerate 10.0
   #
   #设置( |OA| - (rO+rA)*rext| ) <= tolerate的颗粒粘结在一起，使颗粒具有粘聚力 。这里，tolerate取默认值1e-6
   PROP n_bond 1.0e4 s_bond 1.0e4 tolerate rext 0.8
   
   #设置所有颗粒线速度和角速度为零
   PROP xv 0.0 yv 0.0 spin 0.0

