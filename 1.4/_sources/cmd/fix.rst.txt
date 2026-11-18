.. index:: ! fix

fix
===

:说明: ``fix`` 限制颗粒运动

:使用方法:

::

   FIX x y spin [RANGE ...]

:实例:

::

   # 限制颗粒 x y 方向速度和角速度
   FIX x y spin
   # 限制bom组中颗粒的y向速度和角速度
   FIX y spin RANGE group bom

