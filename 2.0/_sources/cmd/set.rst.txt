.. index:: ! set

set
===

:说明: 设置计算的基本参数，如 时间步长 ``DT`` ，重力加速度 ``G`` 等

:使用方法:

   设置时间步长 和 重力加速度::
   
    SET DT <float>, GRAVITY (<float> <float>)
  
   设置颗粒形状，默认为 ``on`` ，即圆盘颗粒体积为 :math:`V=\pi \cdot r^2` ；``off`` 为球，颗粒体积为 :math:`V= 4/3 \cdot \pi \cdot r^3` ::
   
    SET disk <on|off>
   
   设置进度条刷新间隔::
   
    SET stepbar <int>
   
   设置ZDEM格式的 ``.sav`` 文件保存间隔::
   
    SET sav <int>
  
   设置 ``.ps`` 矢量图保存间隔::
   
    SET ps <int>
   
   设置ZDEM格式的 ``.dat`` ASCII文件保存间隔::
   
    SET print <int>
   
   设置 ``paraview`` 格式的 ``.vtk`` 文件保存间隔::
   
    SET vtk <int>

:实例:

    ::

        #设置时间步DT 及 重力加速度 G
        SET  DT 5e-2,  GRAVITY  0.0,  -9.8 
        #设置颗粒形状
        SET disk off #球，计算颗粒体积用4/3*pi*r^3计算
        SET disk on  #圆盘（默认开启），V=pi*r^2
        #每计算 100 步更新一次进度条
        SET stepbar 100

