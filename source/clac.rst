提交计算
========

- 直接计算
    ::

        vboxdaily cmd.txt

    - 优点：实时查看计算是否正确，使用`ctrl+c`结束计算

    - 缺点：关闭`xshell`，计算停止



- 使用SGE调度VBOX
    ::

        qsub run.sh
        qstat
        qdel <id>

    - 优点：同时计算多个，关闭 ``xshell`` ，不影响计算
    - 缺点：不能实时查看计算情况

    1. 提交计算

    ::

        qsub run.sh

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

    3. 强制结束计算

    ::

        qdel <id>

