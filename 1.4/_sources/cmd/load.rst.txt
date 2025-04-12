.. index:: ! load

load
====

:说明: ``loa[d]`` 从xyr.dat文件中读取颗粒坐标和半径，并生成这些颗粒。

:使用方法:

::

    #从 xyr.dat 中读取颗粒坐标和半径
    LOAD xyr.dat [scale <float>] [x <float> <float> ] [y <float> <float> ]

其中，``xyr.dat`` 是 ``x y r [GROUP]`` 格式的ASCII文件，可由VBOX或者其他软件生成。

:实例:

::

   # 导入全部颗粒的x y r [group]信息，其中 xyr.dat文件可以包含GROUP信息
   LOAD xyr.dat
   # 导入颗粒的x y r 信息，并缩放0.1倍，即 x=scale*x, y=scale*y, r=scale*r
   LOAD xyr.dat scale 0.1
   # 导入颗粒（1000.0<x<2000.0 并且 2000.0<y<4000.0 ）的x y r信息
   LOAD xyr.dat x 1000.0 2000.0 y 2000.0 4000.0 

