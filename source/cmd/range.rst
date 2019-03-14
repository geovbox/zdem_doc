.. index:: ! range

range
=====

:基础: 圈定颗粒范围，不指定range则默认选定全部颗粒，必须放在其他命令的最后 ``prop`` ``bond`` ``del`` 后，拥有 ``矩形xy`` ``多边形P4`` 圈定方法

  使用方法::

    #指定 ``左右边界`` ``下上边界`` 圈定该范围
    RANGE X (<float> <float>), Y (<float> <float>)
    #逆时针指定四个点，圈定四个点组成的范围
    RANGE P4 (<float> <float>), (<float> <float>), (<float> <float>), (<float> <float>)

  实例::

    #圈定一个矩形范围，左右边界(1.0 10.0)，下上边界(1.0 10.0)
    #将该范围内的颗粒的颜色设置为红色
    PROP COLOR red RANGE x (1.0 10.0) y (1.0 10.0)
    #圈定一个四边形范围，逆时针指定四个点 ( 2e-2, 0.0) (3e-2, 0.0) ( 1e-2, 2e-2) (1e-2, 1e-2)
    #将该范围内的颗粒的摩擦系数设置为0.0
    PROP fric 0.0 range P4 ( 2e-2, 0.0) (3e-2, 0.0) ( 1e-2, 2e-2) (1e-2, 1e-2)

:进阶: 使用 ``AND`` ``OR`` 选定范围

使用方法::

    #圈定X()Y()和GROUP指定的范围
    range X (<float> <float>), Y (<float> <float>) AND/OR GROUP <str> 

实例::

    #1. AND用法
    # 将在矩形 x() y()中，并且在四边形 P4 ()()()()中， 的颗粒颜色设置为红色
    PROP COLOR red RANGE x (1.0 10.0) y (1.0 10.0) AND P4 ( 2e-2, 0.0) (3e-2, 0.0) ( 1e-2, 2e-2) (1e-2, 1e-2)
    #将在矩形 x() y()中，并且在组GROUP sed中，的颗粒颜色设置为红色
    PROP COLOR red RANGE x (1.0 10.0) y (1.0 10.0) AND GROUP sed
    
    #2. OR用法
    #将在矩形 x() y() 或者 P4 ()()()() 中的颗粒颜色设置为红色
    PROP COLOR red RANGE x ( 1e-2, 2.0e-2) y ( 0e-2, 1.5e-2) OR P4 ( 2e-2, 0.0) (3e-2, 0.0) ( 1e-2, 2e-2) (1e-2, 1e-2)


