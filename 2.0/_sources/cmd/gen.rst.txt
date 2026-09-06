.. index:: ! gen

gen
===

:说明: ``gen`` 在一个矩形空间中生成一定数量的颗粒

- 支持变量 ``{left} {right} {bottom} {top}``, 大括号引用所需要的变量，如式子 ``{top}-1000.0``, 式子内不能有空格。

:使用方法:

::

   GEN NUM <int>, RAD DISCRETE <float> <float>, X (<float> <float>), Y (<float> <float>) [COLOR=<str>] [GROUP=<str>]

:实例:

1. 生成一定数量的颗粒，数量20000，颗粒半径随机生成为 60.0 或者 80.0 ， 矩形左右边界为(1000.0, 61000.0)，上下边界为 (1000.0, 13000.0)，黑色

::


   GEN NUM 20000 rad discrete 60.0 80.0,  x (1000.0, 61000.0), y (1000.0, 13000.0), COLOR black GROUP ball_rand 

2. 沉积。在挤压顶部往下1000米范围内生成颗粒，沉积后约 500 m 颗粒。经验：颗粒充填满1km范围，沉积之后的地层厚度约为500m。

::

   
   GEN NUM 100000.0 rad discrete 60.0 80.0,  x ({left}, {right}), y ( {top}-1000.0, {top}), COLOR red GROUP sed1
   
   
.. figure:: /cmd/gen1.jpg
  :width: 100%
  :align: center

  **沉积前**
  
.. figure:: /cmd/gen2.jpg
  :width: 100%
  :align: center
  
  **沉积后**
