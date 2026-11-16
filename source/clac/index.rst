提交计算
########

``push.py`` 为要运行的脚本名

直接提交
========

::

    #程序名 脚本名
    zdem push.py

- 优点：实时查看计算是否正确，使用 ``ctrl+c`` 结束计算
- 缺点：关闭窗口，计算停止

.. warning::

    这种方式只能作简单测试用，长时间使用会被管理员封号。
    如果想交互式的提交计算，可采用如下命令 ``srun -n 1 -c 12 zdem push.py`` ，即采用1个节点 ``-n 1`` ， 12个核 ``-c 12`` 计算。这种方式会正常计费，不会被管理员封号。

.. _slurm:

Slurm 作业调度系统
==================

`并行超算云 <https://geovbox.com/hpc/>`_ 安装了该调度系统。

SLURM （Simple Linux Utility for Resource Management）是一种可扩展的工作负载管理器，已被全世界的国家超级计算机中心广泛采用。 它是免费且开源的，根据GPL通用公共许可证发行。

+ ``sbatch job.sh`` 提交作业
+ ``squeue`` 查看作业状态（可以查看所有作业的id号）
+ ``scancel id`` 取消一个作业（id号定位该作业）

.. note::

    * 优点：同时计算多个，关闭窗口，不影响计算
    * 缺点：不能实时查看计算情况


提交作业 ``sbatch job.sh``
--------------------------
显示
::

    Submitted batch job 134573 

说明提交成功。 `job.sh <https://github.com/geovbox/zdem_doc/blob/master/source/clac/job.sh>`_  内容如下:

.. literalinclude:: job.sh

.. warning::

    这里配置 ``module load zdem2.0`` ，将使用 ``2.*`` 系列的最新版本。

.. warning::

    注意job.sh的行结尾符需采用 Unix 的 ``\n`` 格式，否则将产生如下错误信息：
    
    ::
    
        sbatch: error: Batch script contains DOS line breaks (\r\n)
        sbatch: error: instead of expected UNIX line breaks (\n).
    
    修改 ``job.sh`` 的行结尾符 见 `第00课 并行超算云上使用ZDEM <https://www.bilibili.com/video/BV1m7411M7rz?p=1>`_ 的 10:15

查看作业状态 ``squeue``
--------------------------

显示
::

         JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON) 
        134573    v6_384     test  sc80502  R       0:30      1 cb0503 

从上面的输出可知，该任务的 ``id`` 为 ``134573`` 。``ST`` 状态为 ``R`` 说明正在计算。任务分配给了节点 ``cb0503``。

.. tip::

    `squeue -l` 可以查看作业细节信息

取消作业 ``scancel id``
--------------------------

要杀死上面的作业， 输入 ``scancel 134573`` 即可，134573为上面作业的id号。

再次输入 ``squeue``。显示
::

         JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON) 

说明作业已经取消。

.. seealso::

    Slurm更多介绍 https://docs.hpc.sjtu.edu.cn/job/slurm.html


DeepSeek Harness 提交
=====================

在 DeepSeek Harness 中安装超算远程连接插件 `DSH-SLOP <https://github.com/zrzrv5/dsh-slop>`_，你就可以使用如下自然语言控制计算任务：

    .. only:: html

       .. figure:: /clac/ZDEM@harness-1提交计算示例11月14日.gif
          :width: 100%
          :align: center

  

提示词示例
----------

提示词示例1

::

    把 ex1_small2 上传、提交并登记追踪；计算完成后把结果下载到本地，
    注意只下载 jpg 和 gif 图片，本地目录结构要与远程保持一致。
    再把 jpg + gif + 模拟参数做成 1 页 PPT，做好后发到我的邮箱。

提示词示例2

::

    我要分析颗粒摩擦系数fric对构造变形过程的影响，你在ex1_small2的基础上，
    创建ex1_small3文件夹，对应修改push.py中的fric为0.0，
    把这个文件夹传上去、提交并登记追踪，计算完成后，把结果下载到本地，注意只下载jpg和gif图片，
    本地目录结构保证和远程一致。
    把ex1_small2和ex1_small3这两个实验的jpg+gif+模拟参数做成2页实验结果对比PPT，
    把做好的这个PPT发我邮箱。


.. figure:: /clac/deekseekharness-example1-2.png
  :width: 100%
  :align: center
  
  **DeepSeek Harness 中使用示例**
  
.. figure:: /clac/20261114李长圣@地大武汉3-harness.png
  :width: 100%
  :align: center
  
  **DeepSeek Harness 做好的多个实验对比PPT示例**


如何选择
--------

- 优点：
    * 用自然语言下达任务，上传、提交、任务状态监测、结果下载全程自动完成
    * 可接续生成汇报 PPT 并直接发送至本人邮箱
    * 适合单因素批量多算例提交，无需手工建目录、逐个提交和下载

- 缺点：
    * 依赖 DeepSeek-V4.1 Flash 模型，需消耗 Token（约几分到几毛钱）
    * 计算规模较小时，Deepseek理解自然语言所花的时间在总耗时中占比偏高，性价比不佳

.. note::

    - **Slurm**：单任务提交
    - **DeepSeek Harness**：多算例、单因素批量任务



配置DeepSeek Harness
----------------------

让智能体在高性能计算集群上运行，需要安装 DeepSeek Harness 插件 DSH-SLOP 

:适用版本: DeepSeek Harness ``0.2.2-rc.3`` ＋ DSH-SLOP ``0.0.17``
:仓库: https://github.com/demsheng/dsh-slop
:最后更新: 2026-11-16

- 打开 **DeepSeek Harness** 输入以下提示词

    .. code-block:: text

       安装插件 https://github.com/demsheng/dsh-slop


- 安装PPT制作skill提示词

    .. code-block:: text

       安装skill https://github.com/wendaokeliu-sys/ppt-builder

- 安装邮件插件	提示词

    .. code-block:: text

       推荐给我，可以给我发邮件的插件


测试用例
--------

目录结构

::

    |-- test-dsh-slop #设置为 DeepSeek Harness 的工作目录
        |-- slurm.sh
        |-- syn_erosion.py

``slurm.sh``

.. literalinclude:: /clac/test-dsh-slop/slurm.sh

``push.py``

.. literalinclude:: /clac/test-dsh-slop/push.py



在DeepSeek Harness中设置工作目录为 ``test-dsh-slop`` ，打开对话框，输入以下提示词

- 仅仅测试 dsh-slop 插件

    ::

        把 test-dsh-slop 上传、提交并登记追踪；计算完成后把结果下载到本地，
        注意只下载 jpg 和 gif 图片，本地目录结构要与远程保持一致。

- 测试 ``dsh-slop`` ``ppt-builder`` 和 给本人发邮件功能

    ::

        把 test-dsh-slop 上传、提交并登记追踪；计算完成后把结果下载到本地，
        注意只下载 jpg 和 gif 图片，本地目录结构要与远程保持一致。
        再把 jpg + gif + 模拟参数做成 1 页 PPT，做好后发到我的邮箱。


