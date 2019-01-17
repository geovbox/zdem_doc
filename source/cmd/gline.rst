.. index:: ! gline

gline
=====

:说明: ``gli[ne]`` 在两个点之间建立一组线形排列的颗粒

使用方法::

   GLINE RAD=<float> NODES ( <float> <float> ) ( <float> <float> ), KN=<float> KS=<float> FRIC=<float>, [COLOR=<str>]

实例::

   # 在点 ``( 2.0  10.0 )`` 和点 ``( 40.0  10.0 )`` 间生成半径为0.5的颗粒，法向刚度系数kn=4.14e3，切向刚度系数ks=4.14e3，摩擦系数fric=0.55，颜色color=red
   GLINE RAD=0.5 nodes ( 2.0  10.0 ) ( 40.0  10.0 ), kn=4.14e3 ks=4.14e3 fric=0.55 color=red

