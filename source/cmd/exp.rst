.. index:: ! exp

exp
===

:说明: ``exp[xyr]`` 导出颗粒的xyr等信息到ASCII格式文件，其它离散元软件可以直接读取

使用方法::

    #从 xyr.dat 中读取颗粒坐标、半径和[所属组]
    exp xyr.dat [GROUP] [RANGE ...]

其中，``xyr.dat`` 是 ``x y r [GROUP]`` 格式的ASCII文件，可由VBOX或者其他软件生成。

实例::

   # 导出全部颗粒的x y r信息
   exp xyr.dat
   # 导出全部颗粒的x y r group信息
   exp xyr.dat GROUP
   # 导出bom组中颗粒的x y r信息
   exp xyr.dat range group bom
   # 导出 1000.0<y<2000.0 的颗粒的x y r group信息
   exp xyr.dat GROUP range y 1000.0 2000.0
