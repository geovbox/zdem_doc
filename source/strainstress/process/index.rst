.. _ss_process:

步骤
====

无沉积剥蚀过程
--------------

如果没有沉积和剥蚀过程， ``sbatch jobs.sh`` 提交，出应力应变将输出到 ``ex5_detachment/data/ss``。

这里采用 ``构造模拟`` 中的 :ref:`detachment` 示例

目录结构：

::

    | -- ex5_detachment
        | -- detachment.py
        | -- init_xyr.dat
        | -- job.sh

- ``detachment.py`` 见 :ref:`detachment`
- ``init_xyr.dat`` 见 :ref:`detachment`
- ``job.sh`` 内容如下：

    .. literalinclude::  job.sh

最后两行， 

- ``zdem -s ./data`` 计算应力应变
- ``zdemss --dir ./data`` 绘制应力应变。

有沉积剥蚀过程
--------------


.. warning::

    这里步骤仅为了帮助用户理解应力应变计算过程，仍需要 Slurm 作业调度系统提交计算，见  :ref:`push_add_del` 。

初始目录结构：

::

    |-- ex1
        |-- push_add_del.py

``push_add_del.py`` 见  :ref:`push_add_del`

如果有沉积剥蚀过程，需要仔细选择沉积剥蚀的临界文件，详细的流程如下：


 
**所有操作均在 ex1 目录下操作**

1. ``zdem push_add_del.py``   
    计算完成，将生成 ``./data`` 文件夹。目录结构如下：
    
    ::

        |-- ex_strain_stress
            |-- push.py
            |-- data
                |--  all_0000000000_ini.dat
                |--  ...    
                |--  all_0000005000.dat    
                |--  all_0000058000_ini.dat
                |--  all_0000108000.dat    
    
2. ``zdem2jpg --dir=./data``   
    生成jpg，生成计算过程图．注意：这里，只需指定 ``--dir`` ，不加其它任何参数．
    目录结构如下 
    
    ::

        |-- ex_strain_stress
            |-- push.py
            |-- data
                |--  all_0000000000_ini.dat
                |--  all_0000000000_ini.jpg
                |--  ...    
                |--  all_0000005000.dat
                |--  all_0000005000.jpg
                |--  all_0000058000_ini.dat
                |--  all_0000058000_ini.jpg
                |--  all_0000108000.dat
                |--  all_0000108000.jpg
    
3. 新建datass文件夹，根据jpg挑选需要计算应力应变的.dat文件，复制到datass文件夹中。  
    这里，挑选原则如下：

    - 刚沉积完，并给定颜色，准备挤压的初始模型，必须。all_0000006000_ini.dat
        .. figure:: all_0000006000_ini.jpg
          :width: 100%
          :align: center
    - 刚剥蚀完，准备挤压的模型，必须。all_0000036000_ini.dat
        .. figure:: all_0000036000_ini.jpg
          :width: 100%
          :align: center
    - 沉积稳定，准备挤压前的模型。all_0000058000_ini.dat
        .. figure:: all_0000058000_ini.jpg
          :width: 100%
          :align: center
    - 沉积过程不要，其它的可酌情选取。
    
        目录结构如下 
    
    ::

        |-- ex_strain_stress
            |-- push.py
            |-- data
                |--  all_0000000000_ini.dat
                |--  all_0000000000_ini.jpg
                |--  ...    
                |--  all_0000005000.dat
                |--  all_0000005000.jpg
                |--  all_0000058000_ini.dat
                |--  all_0000058000_ini.jpg
                |--  all_0000108000.dat
                |--  all_0000108000.jpg
            |-- datass
                |-- all_0000006000_ini.dat
                |-- all_0000026000.dat
                |-- all_0000036000_ini.dat
                |-- all_0000056000.dat
                |-- all_0000058000_ini.dat
                |-- all_0000078000.dat
                |-- all_0000108000.dat
            
4. 计算应力和应变
    - 无沉积和剥蚀 ``zdem -s ./datass``  
    - 有沉积和剥蚀 ``zdem --xmove -1000.0 --ymove -1000.0 --addball --delball -s ./datass``   

    将生成 ``./datass/ss/data/*.out`` ，供GMT绘图用。注意：基于步骤2，我们知道 ``--xmove --ymove`` 应该设置为多少．如果有沉积 ``--addball`` 或者剥蚀 ``--delball`` 过程，需添加相应参数．
    
    目录结构如下 
    
    ::

        |-- ex_strain_stress
            |-- push.py
            |-- data
                |--  all_0000000000_ini.dat
                |--  all_0000000000_ini.jpg
                |--  ...    
                |--  all_0000005000.dat
                |--  all_0000005000.jpg
                |--  all_0000058000_ini.dat
                |--  all_0000058000_ini.jpg
                |--  all_0000108000.dat
                |--  all_0000108000.jpg
            |-- datass
                |--ss
                   |-- data
                       |-- *.out
                |-- all_0000006000_ini.dat
                |-- all_0000026000.dat
                |-- all_0000036000_ini.dat
                |-- all_0000056000.dat
                |-- all_0000058000_ini.dat
                |-- all_0000078000.dat
                |-- all_0000108000.dat
    
    
    
    ``zdem -h`` 查看如下帮助文档
    
    ::

        用法:
	        zdem [可选项] [script.py]

        可选项:
	        --addball 
		        配合-s选项，应力应变计算过程中，有新颗粒加入体系（沉积）,默认关闭。
	        --delball 
		        配合-s选项，应力应变计算过程中，删除了颗粒（剥蚀），默认关闭。
	        -g, --grid SIZE
		        配合-s选项，设置应力应变计算时候，网格的大小SIZE，默认200.0
	        -h, --hlep
		        显示帮助信息
	        -j NUM
		        并行计算开辟的线程数NUM，默认使用OMP_NUM_THREADS，
		        如未设置OMP_NUM_THREADS，则使用全部CPU物理核心数并行计算。
		        
	        --leftwallid ID
		        配合-s选项，设置左边墙ID，该墙左边颗粒均会被删除。如果颗粒被挤出到左边墙之外，需要设置该参数。
	        --rightwallid ID
		        配合-s选项，设置右边墙ID，该墙右边颗粒均会被删除。如果颗粒被挤出到右边墙之外，需要设置该参数。
	        -s, --strain-stress  DataDir
		        计算应力应变
		        从DataDir读取数据，将应力应变输出到DataDir/ss目录
	        -v, --version
		        打印版本信息
	        --xmove X
		        配合-s选项，设置模型x方向偏移位移X，默认0.0。
	        --ymove Y
		        配合-s选项，设置模型y方向偏移位移Y，默认0.0。

        例子:
	        zdem script.py
		        读取script.py中的VBOX命令，开始计算。
	        zdem --strin-stres  ./data
		        从./data目录读取数据，将计算的应力应变输出到./data/ss目录
	        zdem -v
		        打印版本信息

    
5. 使用GMT绘制应力应变。
    - 无沉积和剥蚀 ``zdemss --dir ./datass``    
    - 有沉积和剥蚀 ``zdemss --dir ./datass  --addball ON --delball ON``   

    ``zdemss`` 将会读取 ``zdem`` 生成的应力应变数据，生成应力应变云图到 ``./datass/ss`` 。  

    设置x轴最大值 40.0 km，设置y轴最大值 10.0 km，设置颜色条应力最大值400 MPa：
    
    ::
    
        zdemss --dir ./datass --xmax 40.0 --ymax 10.0 --maxstress 250.0
    
    
    运行完成之后，目录结构：
        
    ::

        |-- ex_strain_stress
            |-- job1.sh
            |-- job2.sh
            |-- push.py
            |-- data
                |--  all_0000000000_ini.dat
                |--  ...    
                |--  all_0000005000.dat    
                |--  all_0000058000_ini.dat
                |--  all_0000108000.dat    
            |-- datass
                |-- ss
                    |-- data
                        |-- *.out
                    |-- ps
                       |-- *.ps
                    |-- tmp
                        |-- *.grd
                    |-- *.jpg
                |-- all_0000006000_ini.dat
                |-- all_0000026000.dat


    - ``./datass/ss/data/*.out`` 应力应变原始数据
    - ``./datass/ss/ps/*.ps``  **输出的应力应变图(矢量图)**
    - ``./datass/ss/ps/*.grd`` 计算应力应变产生的中间数据
    - ``./datass/ss/*.jpg`` **输出的应力应变图(位图)**
    
    
    
    ``zdemss -h`` 查看如下帮助文档

    ::

        参数说明：
        --addball ON/OFF 	 有沉积事件，默认OFF
        --delball ON/OFF 	 有剥蚀事件，默认OFF
        -d, --dir 	 设置数据所在目录
        -h, --help 	 打印帮助信息
        --showcolorbar ON/OFF 	 绘制颜色条，默认ON
        --showlable ON/OFF/abc 	 绘制颜色条，默认OFF，其中abc只给子图命名为abc
        --stressshear ON/OFF 	 绘制剪切应力，默认ON
        --stressmean ON/OFF 	 绘制平均应力，默认ON
        --strainshear ON/OFF 	 绘制变形应变，默认ON
        --strainvol ON/OFF 	 绘制体积应变，默认ON
        --width value 	 图片宽(cm)，默认14
        --xmax value 	 x轴最大值(km)，默认自动设置
        --ymax value 	 y轴最大值(km)，默认自动设置
        --maxstress value 	 最大应力值(MPa)，默认 300
        -v, --version 	 显示版本信息

        实例：
        zdemss --dir .

.. _push_add_del.py:



