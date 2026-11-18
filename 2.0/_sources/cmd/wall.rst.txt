.. index:: ! wall
.. _wall:

wall
====

:说明: ``wal[l]`` 基于两个点，新建一个墙体

使用方法::

   WALL ID <int>, NODES ( <float> <float> ) ( <float> <float> ), KN=<float> KS=<float> FRIC=<float>, [COLOR=<str>]
   WALL ID <int>, XV <float>, YV <float>

注意: 墙为一个射线，射线仅左边受力。


实例::

   # 建立一个墙，id为1，两个点( 2.0  40.0 ) ( 2.0  2.0 )连线确定该墙，法向刚度系数kn=4.14e3，切向刚度系数ks=4.14e3，摩擦系数fric=0.55，颜色color=red
   WALL id 1, nodes ( 2.0  40.0 ) ( 2.0  2.0 ), kn=4.14e3 ks=4.14e3 fric=0.55 color=red
   # 设置墙的挤压速度 x方向速度为2.0
   WALL id 1 xv 2.0
   # 设置墙的挤压速度 x方向速度为0.0 y方向速度为2.0
   WALL id 1 xv 0.0 yv 2.0
