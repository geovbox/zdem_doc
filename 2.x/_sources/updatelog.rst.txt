.. _updatelog:

版本更新
========

- V2.2 (2022-05-11) 
    1. 规则：重新设置n_bond等bond参数，将重置之前已经粘结的颗粒间的bond参数。例如
    ::
        PROP  n_bond 1.0 range id 1 2
        PROP  n_bond 2.0 range id 1 2
        # 颗粒1和颗粒2的n_bond将被设置为2.0
        # 之前的版本中，颗粒1和颗粒2的n_bond不更新，仍然保持为1.0
    2. BUG修复：线弹性模型，bond转为contact，kn和ks没有更新，导致它们取值为0。
    3. BUG修复： `sav 0000046.sav` ，缺失字符0，输出为000046.sav。
    4. BUG修复：zdem2jpg 使用参数 `--bondplot=true` 时，`xmax ymax` 失效
    5. 升级：显著提升zdem2jpg计算速度，
    
- V2.1 (2021-06-17) 
    1. 规则：墙 :ref:`wall` 默认为双面受力墙
    2. BUG修复： `zdem -s ./data` 多线程并行，弹出错误mkdir err
    3. BUG修复：zdem2jpg 使用1个核计算时内存溢出
    4. BUG修复：zdem2jpg 使用参数 `--wallshow=false` 时，`xmax ymax` 失效
    

