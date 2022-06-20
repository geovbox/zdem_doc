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
