提交计算
========

直接计算
--------

    ::

        #程序名 脚本名
        vboxdaily cmd.py

    - 优点：实时查看计算是否正确，使用`ctrl+c`结束计算

    - 缺点：关闭`xshell`，计算停止



使用SGE调度VBOX
---------------

    ::

        qsub run.sh
        qstat
        qdel <id>

    - 优点：同时计算多个，关闭 ``xshell`` ，不影响计算
    - 缺点：不能实时查看计算情况

    1. 提交计算

    ::

        qsub run.sh

    显示 ``Your job 3136 ("example") has been submitted`` 说明提交成功。
    
    
    ``run.sh`` 中内容如下::

        #!/bin/sh
        #2017-04-05
        #LI ChangSheng @ NanJing Uninversity 
        #sheng0619@163.com
        #演示如何用SGE调度VBOX
        #$ -S /bin/bash
        #$ -N example #设置任务的名字
        #$ -j y
        #$ -M sheng0619@163.com #修改为自己邮箱
        #$ -m e
        #$ -o log.txt #程序执行日志，记录了错误信息
        #$ -V
        #$ -cwd
        #$ -pe orte 16 #调用16个核计算
        export OMP_NUM_THREADS=$NSLOTS
        time vboxdaily cmd.py #提交计算 

    2. 查看计算状态

    ::

        qstat

    显示
    ::
    
        job-ID  prior   name       user         state submit/start at      queue                          slots ja-task-ID 
        -----------------------------------------------------------------------------------------------------------------
        3136    0.55500 example    zhangsan     r     01/20/2019 14:43:53  all.q@sand-0-0.local              16        

    从上面的输出可知，该任务的 ``id`` 为 ``3136`` 。``state`` 状态为 ``r`` 说明正在计算，如果为 ``w`` 为排队等待状态。任务分配给了节点 ``sand-0-0``，调用了 ``16`` 个核计算。更为详细的说明，可以查询 ``SGE`` 调度系统教程。

    3. 强制结束计算

    ::

        qdel <id>

    我们要杀死上面的任务， ``qdel  3136`` 即可以。输出
    ::
    
        zhangsan has registered the job 3136 for deletion
    
    说明任务已经被杀死。
