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

说明提交成功。 `job.sh <https://github.com/geovbox/vbox_doc/blob/master/source/clac/job.sh>`_  (**点击下载**) 内容如下::

    #!/bin/bash
    #SBATCH --job-name=test
    #SBATCH --partition=v6_384   #Submit to v6_384 queue
    #SBATCH -n 1
    #SBATCH -c 12   #Use 12 core
    #SBATCH -t 1440   #Forced to stop running for more than 1440 min (24 hours)
    #SBATCH --output=%j.out

    source /public1/soft/modules/module.sh
    source /public1/soft/other/module_zdem.sh
    module load zdem2.0 

    srun -n 1 zdem push.py # run zdem
    srun -n 1 zdem2jpg --dir=./data # gen jpg

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
