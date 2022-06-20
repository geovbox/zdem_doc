配置环境变量
============

绘制应力应变图，需要引用如下文献：

1. `Li C, Yin H, et al. (2021) Calibration of the Discrete Element Method and Modeling of Shortening Experiments. Front. Earth Sci. 9:636512. <https://doi.org/10.3389/feart.2021.636512>`_
2. `李长圣 (2019) 基于离散元的褶皱冲断带构造变形定量分析与模拟. 博士论文. 南京大学. Li, C. (2019). Quantitative Analysis and Simulation of Structural Deformation in the Fold and Thrust Belt Based on Discrete Element Method. Doctor Thesis. NanJing University.(in Chinese with English abstract) <http://t.cn/Ai9ruJY5>`_ 推荐下载 `最新修订版 <https://pan.baidu.com/s/1JWORiC034DwWscT9SiLrGQ>`_ 提取码 ``zdem``  
3. `Morgan JK (2015) Effects of cohesion on the structural and mechanical evolution of fold and thrust belts and contractional wedges: Discrete element simulations. Journal of Geophysical Research: Solid Earth 120:3870-3896. <https://doi.org/10.1002/2014JB011455>`_  


配置 ``zdemss`` 的环境变量，将如下内容写入 ``~/.bashrc`` 的文件尾部。

::

    #gmt
    source /public1/soft/modules/module.sh
    source /public1/soft/other/module_GMT.sh
    module load GMT_5.4.5

    #zdemss
    export PATH=/public1/home/sch3726/bin:$PATH #T6分区
    #export PATH=/public1/home/sc80502/bin:$PATH #T分区

.. note::
    不会配置zdemss环境变量的小白用户可参考 `bilibili视频之配置zdemss的环境变量 <https://www.bilibili.com/video/BV1qq4y177Ni?p=4>`_


