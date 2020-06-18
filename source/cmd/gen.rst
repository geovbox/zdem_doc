.. index:: ! gen

gen
===

:说明: ``gen`` 在一个矩形空间中生成一定数量的颗粒

:使用方法:

::

   GEN NUM <int>, RAD DISCRETE <float> <float>, X (<float> <float>), Y (<float> <float>) [COLOR=<str>] [GROUP=<str>]

:实例:

::

   # 生成一定数量的颗粒，数量20000，颗粒半径随机生成为 60.0 或者 80.0 ， 矩形左右边界为(1000.0, 61000.0)，上下边界为 (1000.0, 13000.0)，黑色
   GEN NUM 20000 rad discrete 60.0 80.0,  x (1000.0, 61000.0), y (1000.0, 13000.0), COLOR black GROUP ball_rand 

