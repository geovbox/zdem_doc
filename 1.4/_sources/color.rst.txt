颜色表
======

VBOX支持的颜色列表如下，支持 **数字** 和 **字符** 两种方式:


=====  ===========  ===========  ======
数字   字符          颜色         RGB   
=====  ===========  ===========  ======
``0``  ``lg``       light gray   0.85
``1``  ``green``    green        010
``2``  ``yellow``   yellow       110
``3``  ``red``      red          100
``4``  ``white``    white        1.0
``5``  ``black``    black        0.15
``6``  ``mg``       medium gray  0.5
``7``  ``blue``     blue         001
``8``  ``gb``       green/blue   011
``9``  ``violet``   violet       101
=====  ===========  ===========  ======

后处理阶段，使用 `vbox2jpg <https://doc.geovbox.com/latest/cmd/vbox2jpg/>`_ 命令时， 可以通过 ``--colormap``　制定自己的RGB格式的颜色配置表，默认颜色配置为 ``ColorRicebal.txt`` 格式如下:

.. literalinclude::  ColorRicebal.txt


.. figure:: /images/color.png
   :width: 50%
   :align: left
  



