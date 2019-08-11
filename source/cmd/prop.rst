.. index:: ! prop

prop
====

:说明: ``pro[p]`` 设置材料参数

使用方法::

   PROP DENSITY <float>, FRIC <float>, SHEAR <float>, POISS <float>, DAMP <float>, HERTZ [RANGE ...]
   PROP ebmod <float>, gbmod <float>, tstrength <float>, sstrength <float>, [fric <float>] [RANGE ...]
   PROP DENSITY <float>, FRIC <float>, KN <float>, KS <float>  [RANGE ...]
   PROP n_bond <float> s_bond <float> [RANGE ...]

实例::

   # Model 1. ref. [Morgan 2015 JGR] 和 [李长圣博士论文,2019]
   # 设置材料参数 密度DEM，摩擦系数FRIC，剪切模量shear，泊松比poiss，阻尼DAMP
   PROP DENSITY 2.5e3, fric 0.3, shear 2.9e9, poiss 0.2, damp 0.4, HERTZ
   #设置 range x 1.0 10.0 y 1.0 10.0 中颗粒粘结在一起，使颗粒具有粘聚力 
   PROP ebmod 2e8 gbmod 2e8  tstrength 2e7 sstrength 4e7 fric 0.3 range x 1.0 10.0 y 1.0 10.0
   #
   # Model 2. ref. [PFC2D 4.0 手册] 和 [李长圣博士论文,2019]
   # 设置所有颗粒的材料参数 密度DEM，摩擦系数FRIC，法向刚度KN，切向刚度KS，阻尼DAMP 
   PROP DENSITY 2.5e3, KN 1e4, KS 1e4, FRIC 0.3, DAMP 0.4
   #设置所有颗粒粘结在一起，使颗粒具有粘聚力 
   PROP n_bond 1.0e4 s_bond 1.0e4

