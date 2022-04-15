.. index:: ! zdemss
.. _zdemss:

zdemss
======

:说明: 绘制应力应变。

:使用方法: ``zdemss [可选项]`` 

例如　``zdemss --dir ./datass``　，将 ``./datass`` 目录中的数据绘制成云图。前提，已经采用 ``zdem -s ./datass`` 计算了应力应变数据，数据已默认保存到了 ``./datass/ss/data`` 中，见 :doc:`zdem` 。 ``zdemss`` 完成应力应变绘制，生成的目录结构如下：

    - ``./datass/ss/data`` 该文件夹保存了 :ref:`zdem` 输出的颗粒位置和(假)应力的原始数据
    - ``./datass/ss/data2ps``  该文件夹内为 (真)应力应变数据，用于绘制应力应变图(ps)，用户可以用于定量分析
    - ``./datass/ss/ps``  该文件夹内为应力应变图(矢量图)
    - ``./datass/ss/Tmp`` 该文件夹内为计算应力应变产生的中间数据
    - ``./datass/ss/*.jpg`` **绘制完成的应力应变图(位图)**


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

``--strainvol`` ON/OFF       
    绘制体积应变，默认ON
``--strainshear`` ON/OFF     
    绘制变形应变，默认ON
``--straincolormap`` 	value 
    设置应变颜色映射表，默认default。  示例 ``--straincolormap ./ss/gradwhite-invar.cpt`` ，其中 ``./ss/gradwhite-invar.cpt`` 为用户自定义的颜色映射表
``--sigma1`` ON/OFF 
    最大主应力矢量(叠加在应变图上)，默认OFF不绘制
    
    - ``--scale`` value
        矢量长度缩放系数,默认1.0(取值范围0.0~+∞)
    - ``--gridsize`` value
        计算最大主应力均值的正方形边长大小,默认600.0(取值应大于颗粒直径）。取值越大,绘制的矢量线越稀疏。
``--stressmean`` ON/OFF      
    绘制平均应力，默认ON
``--stressshear`` ON/OFF     
    绘制剪切应力，默认ON
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
    读取 ``./datass`` 中的数据计算应力应变 ，设置x轴最大值 40.0 km，设置y轴最大值 10.0 km，设置颜色条应力最大值400 MPa
``zdemss --dir ./data --sigma1 ON --scale 2.0 --gridsize 1000.0``
    读取 ``./data`` 中的数据计算应力应变，绘制最大主应力矢量，默认叠加在变形应变图上

.. note::
    详细用法示例，参考应力应变 :ref:`no_add_del` 、 :ref:`add_del` 和 :ref:`plot_sigma1` 

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
