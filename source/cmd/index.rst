命令参考
########


**文档约定**

所有的命令，在介绍其用法时，都尽量遵循如下约定：

- 中括号 ``[ ]`` 括起来的字符串是可选项
- 尖括号 ``< >`` 括起来的项表明实际使用时需要用具体的数值替代
- ``#`` 之后的内容为注释

比如， ``bal[l] id=<int> X=<float> Y=<float>`` ：

- ``<int>`` 是必须的，使用时需要用具体数字代替
- ``[l]`` 是可选的，实际使用时可以省略

**按功能分类**

下面将VBOX中的命令按照功能分类，并用一句话简述其功能。

- 主程序

  - ``vboxdaily cmd.txt`` : 运行 ``cmd.txt`` 脚本
  - :doc:`vboxplot` : ``vboxplot ./data`` ， 将 ``./data`` 中的计算结果绘制成 ``jpg`` 格式
  
*脚本* ``cmd.txt`` *中支持的命令如下：*

- 程序开始

  - :doc:`start` : 开始一个新的计算
  - :doc:`restore` : 从某个计算节点恢复，继续计算
  - :doc:`load` : 从坐标文件 ``xyr.dat`` 文件中读取颗粒坐标和半径，并生成这些颗粒。

- 颗粒生成

  - :doc:`wall` ：基于两个点，新建一个墙体
  - :doc:`ball` ：新建一个颗粒
  - :doc:`gen` ：在一个矩形空间中生成一定数量的颗粒
  - :doc:`gline` ：在两个点之间建立一组线形排列的颗粒
  - :doc:`del` ：删除颗粒，用于实现剥蚀

- 基本参数设置

  - :doc:`set` ：设置计算的基本参数，如 时间步长 ``DT`` ，重力加速度 ``G`` 等

- 颗粒参数设置

  - :doc:`prop` ：设置颗粒的微观参数
  - :doc:`bond` ：断开粘结 ``bond``

- 范围圈定

  - :doc:`range`: 用在 ``prop`` ``bond`` ``del`` 后，拥有 ``矩形xy`` ``多边形P4`` 圈定方法

- 设置挤压量

  - :doc:`cyc` ：从网格文件中提取基本信息
  - :doc:`imple` ：从表数据中提取信息

- 格式转换

  - :doc:`vboxplot` ：利用VBOX生成的 ``all_*.dat`` 文件绘制如 ``jpg`` ``pdf`` 等各种格式的图片
  - :doc:`ps2raster <psconvert>` ：将VBOX生成的PS文件转换为其他图片格式。 `GMT <https://gmt-china.org/>`_ 命令
  - :doc:`psconvert` ：将VBOX生成的PS文件转换为其他图片格式。`GMT <https://gmt-china.org/>`_ 命令

.. raw:: latex

   \addtocontents{toc}{\protect\setcounter{tocdepth}{0}}
   \setcounter{secnumdepth}{0}

.. toctree::
   :maxdepth: 1
   :caption: 命令列表

   ball
   bond
   cyc
   del
   gen
   gline
   imple
   load
   prop
   psconvert
   range
   restore
   set
   start
   wall
   vboxplot
