.. index:: ! zdemss
.. _zdemss:

zdemss
======

:说明: 绘制应力应变。

:使用方法: ``zdemss [可选项]`` 

例如　``zdemss --dir ./data``　，将 ``./data`` 目录中的数据绘制成云图。前提，已经采用 ``zdem -s ./data`` 计算了应力应变数据，数据已默认保存到了 ``./data/ss/data`` 中，见 :doc:`zdem` 。

可选项
------

``--addball`` ON/OFF         
    有沉积事件，默认OFF
``--delball`` ON/OFF         
    有剥蚀事件，默认OFF
``-d``, ``--dir``        
    设置数据所在目录
``-h``, ``--help``       
    打印帮助信息
``--showcolorbar`` ON/OFF    
    绘制颜色条，默认ON
``--showlable`` ON/OFF/abc   
    绘制颜色条，默认OFF，其中abc只给子图命名为abc
``--stressshear`` ON/OFF     
    绘制剪切应力，默认ON
``--stressmean`` ON/OFF      
    绘制平均应力，默认ON
``--strainshear`` ON/OFF     
    绘制变形应变，默认ON
``--strainvol`` ON/OFF       
    绘制体积应变，默认ON
``--width`` value    
    图片宽(cm)，默认14
``--xmax`` value     
    x轴最大值(km)，默认自动设置
``--ymax`` value     
    y轴最大值(km)，默认自动设置
``--maxstress`` value        
    最大应力值(MPa)，默认 300
``-v``, ``--version``    
    显示版本信息

实例
----

``zdemss --dir ./data`` 
    读取 ``./data`` 中的数据计算应力应变 。
``zdemss --dir ./datass --xmax 40.0 --ymax 10.0 --maxstress 250.0``　
    设置x轴最大值 40.0 km，设置y轴最大值 10.0 km，设置颜色条应力最大值400 MPa

.. note::
    详细用法，参考应力应变 :ref:`no_add_del` 和 :ref:`add_del`

高级功能
--------
``--straincolormap`` default/filename.cpt
    绘制颜色映射表，默认default，示例 ``--straincolormap ./data/ss/gradwhite-invar.cpt``

- 示例1  
    
    .. figure:: 1600.jpg
      :width: 60%
      :align: center
  
  
    ``./data/ss/gradwhite-invar.cpt`` 内容如下：

    .. literalinclude::  gradwhite-invar2.cpt

- 示例2 

    .. figure:: 10000.jpg
      :width: 60%
      :align: center
  
    ``./data/ss/gradwhite-invar2.cpt``  中内容如下：

    .. literalinclude::  gradwhite-invar.cpt


.. note::
    - 颜色映射表内容解释参考 https://docs.gmt-china.org/5.4/cpt/format/
    - 颜色映射表制作方法参考 https://docs.gmt-china.org/5.4/cpt/makecpt/
