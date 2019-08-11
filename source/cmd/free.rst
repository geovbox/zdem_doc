.. index:: ! free

free
====

:说明: ``free`` 与 `fix` 相反，释放颗粒

使用方法::

   FREE x y spin [RANGE ...]

实例::

   # 释放颗粒 x y 方向速度和角速度
   FREE x y spin
   # 释放bom组中颗粒的y向速度和角速度
   FREE y spin RANGE group bom

