.. index:: ! prop

prop
====

:说明: ``pro[p]`` 设置材料参数

使用方法::

   PROP DENSITY <float>, FRIC <float>, SHEAR <float>, POISS <float>, DAMP <float>, HERTZ

实例::

   # 设置材料参数 密度DEM，摩擦系数FRIC，法向刚度KN，切向刚度KS，阻尼DAMP
   PROP DENSITY 2.5e3, fric 0.0, shear 2.9e9, poiss 0.2, damp 0.0, hertz
   #设置bond粘结，使颗粒具有粘聚力
   PROP ebmod 2e8 gbmod 2e8  tstrength 2e7 sstrength 4e7 fric 0.3 range x 1.0 10.0 y 1.0 10.0

