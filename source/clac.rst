提交计算
========

 ``push.py`` 为要运行的脚本名
 

直接提交
--------

    ::

        #程序名 脚本名
        vbox push.py

- 优点：实时查看计算是否正确，使用 ``ctrl+c`` 结束计算
- 缺点：关闭 ``xshell`` ，计算停止



LSF调度 
---------------
南京大学高性能计算中心安装了该调度系统。

+ ``bsub < lsf.sh`` 提交
+ ``bjobs``　查看
+ ``bkill <id>``　删除

- 优点：同时计算多个，关闭 ``xshell`` ，不影响计算
- 缺点：不能实时查看计算情况

1. 提交计算

    ::

        bsub < lsf.sh

    显示 ``Job <230259> is submitted to queue <mpi>.`` 说明提交成功。


    ``lsf.sh`` 中内容如下::

	    #!/bin/bash
	    #
	    #BSUB -J sheng 
	    #BSUB -q mpi
	    #BSUB -n 24
	    #BSUB -R "span[ptile=24]"
	    vboxdaily push.py 
	    vbox2jpg --dir=./data  # 生成 jpg
	    convert -delay 100 ./data/*[0-9].jpg -loop 0 ./data/process.gif  #　制作 gif

2. 查看计算状态

    ::

        bjobs

    显示
    ::

	    JOBID   USER    STAT  QUEUE      FROM_HOST   EXEC_HOST   JOB_NAME   SUBMIT_TIME
	    230259  hwyin   RUN   mpi        c01n02      24*c38n11   *push.py Apr  1 12:44

    从上面的输出可知，该任务的 ``id`` 为 ``230259`` 。``STAT`` 状态为 ``RUN`` 说明正在计算。任务分配给了节点 ``c38n11``，调用了 ``24`` 个核计算。更为详细的说明，可以查询 ``LSF`` 调度系统教程。其中，　``-J``　参数为任务名，可自定义。

3. 强制结束计算

    ::

        bkill <id>

    我们要杀死上面的任务， ``bkill  230259`` 即可以。输出
    ::

        Job <230259> is being terminated

    说明任务已经被杀死。

SGE调度
---------------
南京大学尹宏伟课题组和东华理工大学并行计算实验室集群安装了该调度系统

+ ``qsub sge.sh`` 提交
+ ``qstat`` 查看
+ ``qdel <id>`` 删除

- 优点：同时计算多个，关闭 ``xshell`` ，不影响计算
- 缺点：不能实时查看计算情况

1. 提交计算

    ::

        qsub sge.sh

    显示 ``Your job 3136 ("example") has been submitted`` 说明提交成功。


    ``sge.sh`` 中内容如下::

        #!/bin/sh
        #$ -S /bin/bash
        #$ -N example #设置任务的名字
        #$ -j y
        #$ -M sheng@163.com #修改为自己邮箱
        #$ -m e
        #$ -o log.txt #程序执行日志，记录了错误信息
        #$ -V
        #$ -cwd
        #$ -pe orte 8 #调用8个核计算
        export OMP_NUM_THREADS=$NSLOTS
        time vboxdaily push.py #提交计算 
        vbox2jpg --dir=./data  # 生成 jpg
        convert -delay 100 ./data/*[0-9].jpg -loop 0 ./data/process.gif  # 制作 gif
        
2. 查看计算状态

    ::

        qstat

    显示
    ::

        job-ID  prior   name       user         state submit/start at      queue                          slots ja-task-ID 
        -----------------------------------------------------------------------------------------------------------------
        3136    0.55500 example    zhangsan     r     01/20/2019 14:43:53  all.q@sand-0-0.local              8        

    从上面的输出可知，该任务的 ``id`` 为 ``3136`` 。``state`` 状态为 ``r`` 说明正在计算，如果为 ``w`` 为排队等待状态。任务分配给了节点 ``sand-0-0``，调用了 ``16`` 个核计算。更为详细的说明，可以查询 ``SGE`` 调度系统教程。

3. 强制结束计算

    ::

        qdel <id>

    我们要杀死上面的任务， ``qdel  3136`` 即可以。输出
    ::

        zhangsan has registered the job 3136 for deletion

    说明任务已经被杀死。
    
PBS调度 
---------------
中国石油勘探开发研究院(北京)集群安装了该调度系统

PBS(Portable Batch System)最初由NASA的Ames研究中心开发，主要为了提供一个能满足异构计算网络需要的软件包，用于灵活的批处理，特别是满足高性能计算的需要，如集群系统、超级计算机和大规模并行系统。PBS的主要特点有：代码开放，免费获取；支持批处理、交互式作业和串行、多种并行作业。


1. ``qsub  pbs.sh`` 提交

    ::

        [zhangsan@mu01 ~]$ qsub pbs.sh 
        28.mu01

    其中， ``pbs.sh``　中内容：

    ::

        #PBS -N sheng ##可以给任务一个名字,方便辨识
        #PBS -l nodes=1:ppn=12 ##使用1节点，每个节点12核
        vboxdaily push.py
        vbox2jpg --dir=./data
        convert -delay 100 ./data/*[0-9].jpg -loop 0 ./data/process.gif 

2. ``qstat`` 查看

    ::

        [zhangsan@mu01 ~]$ qstat
        Job id                    Name             User            Time Use S Queue
        ------------------------- ---------------- --------------- -------- - -----
        31.mu01                    zhangsan         lichangsheng    00:00:13 R batch


3. ``qdel 31`` 删除作业号为31的作业

    ::

        [zhangsan@mu01 ~]$ qdel 28
        [zhangsan@mu01 ~]$ qstat
        Job id                    Name             User            Time Use S Queue
        ------------------------- ---------------- --------------- -------- - -----
        31.mu01                    sheng            zhangsan     00:22:43 C batch

参数解释

::

    Job id      Name       User      Time Use    S        Queue
    作业号      作业名     提交人    运行的时间  作业状态  队列


通常作业状态：

- Q 作业排队
- R 作业执行
- C 作业清除
- E 作业退出
- H 作业挂起

