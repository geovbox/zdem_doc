.. index:: ! range

range
=====

:简介: 圈定颗粒范围

不指定range则默认选定全部颗粒，必须放在其他命令的最后 ``prop`` ``bond`` ``del`` 后。

圈定方法
--------

- 矩形 ``X (<float> <float>), Y (<float> <float>)`` ，指定 ``左右边界`` ``下上边界``
- 四边形 ``P4 (<float> <float>), (<float> <float>), (<float> <float>), (<float> <float>)`` ，逆时针指定四个点
- 椭圆 ``ellipse (<float> <float>), <float> <float>`` ，指定椭圆中心 (x0, y0) 和 a、b，椭圆方程 (x-x0)^2/a^2 + (y-y0)^2/b^2 = 1
- 组名 ``GROUP <str>``
- 支持变量 ``{left} {right} {bottom} {top}``, 大括号引用所需要的变量，如式子 ``{top}-1000.0``, 式子内不能有空格。

:实例:

1. 矩形

::

    #圈定一个矩形范围，左右边界(1.0 10.0)，下上边界(1.0 10.0)
    #将该范围内的颗粒的颜色设置为红色
    PROP COLOR red RANGE x (1.0 10.0) y (1.0 10.0)

2. 四边形

::

    #圈定一个四边形范围，逆时针指定四个点 ( 2e-2, 0.0) (3e-2, 0.0) ( 1e-2, 2e-2) (1e-2, 1e-2)
    #将该范围内的颗粒的摩擦系数设置为0.0
    PROP fric 0.0 range P4 ( 2e-2, 0.0) (3e-2, 0.0) ( 1e-2, 2e-2) (1e-2, 1e-2)

3. 椭圆

::

    #圈定一个椭圆范围，指定椭圆中心和a,b ( 2e-2, 0.0)  3e-2, 0.0 
    #将该范围内的颗粒的摩擦系数设置为0.0
    PROP fric 0.0 range ellipse ( 2e-2, 0.0)  3e-2, 0.0 

4. 使用变量 ``{left} {right} {bottom} {top}``

::

    #删除顶部1km的颗粒
    DEL RANGE y {top}-1000.0, {top} 

.. figure:: /cmd/del1.jpg
  :width: 100%
  :align: center

  **剥蚀前**
  
.. figure:: /cmd/del2.jpg
  :width: 100%
  :align: center
  
  **剥蚀后**

使用 ``AND`` ``OR``
-------------------

- ``AND`` 并

::

    #颗粒在矩形X()Y()并且在GROUP中，才设置为红色
    prop color red range X (<float> <float>), Y (<float> <float>) AND GROUP <str> 

- ``OR`` 或

::

    #颗粒在矩形X()Y()或者在GROUP中，都设置为红色
    prop coloe red range X (<float> <float>), Y (<float> <float>) OR GROUP <str>

:实例:

1. ``AND`` 

::

    # 颗粒在矩形 x() y()中，并且在四边形 P4 ()()()()中， 则其颜色设置为红色
    PROP COLOR red RANGE x (1.0 10.0) y (1.0 10.0) AND P4 ( 2e-2, 0.0) (3e-2, 0.0) ( 1e-2, 2e-2) (1e-2, 1e-2)
    #颗粒在矩形 x() y()中，并且在组GROUP sed中，则其颜色设置为红色
    PROP COLOR red RANGE x (1.0 10.0) y (1.0 10.0) AND GROUP sed

2. ``OR`` 

::

    #颗粒在矩形 x() y()中， 或者在P4 ()()()() 中，其颜色设置为红色
    PROP COLOR red RANGE x ( 1e-2, 2.0e-2) y ( 0e-2, 1.5e-2) OR P4 ( 2e-2, 0.0) (3e-2, 0.0) ( 1e-2, 2e-2) (1e-2, 1e-2)


