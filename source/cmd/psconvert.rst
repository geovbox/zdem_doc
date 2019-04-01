.. index:: !psconvert

psconvert
=========

:简介: 将 VBOX 生成的 PS/EPS 文件转换为其他图片格式

该模块通过调用 GhostScript 将 PS/EPS 文件转换为其他图片格式，包括BMP、EPS、JPEG、
PDF、PNG、PPM、SVG、TIFF 格式。

必选选项
--------
``psfiles``
    要转换格式的 PS 文件名

    默认情况下，转换后的文件与转换前的文件有相同的文件名，文件后缀由文件格式决定。

    如下命令会将PS文件转换成JPG格式::

        gmt psconvert test.ps
        gmt psconvert test1.ps test2.ps map*.ps

可选选项
--------

``-A``
    对输出的图片做裁边

    默认情况下，转换得到的图片的大小由PS文件的纸张尺寸决定。通常画图的时候是
    不会把一张A4纸画满的，所以在图片周围就会出现多余的白色部分。

    ``-A`` 选项会对PS文件进行裁剪，仅保留其中有绘图的部分::

        gmt psconvert -A test.ps


``-D<outdir>``
    设置输出目录

    默认情况下，会在PS文件同一目录中生成其他图片文件，使用 ``-D<outdir>`` 选项
    可以指定输出目录， ``-D.`` 表示在当前目录输出。需注意，输出目录必须已存在，
    否则会报错。

``-E<dpi>``
    设置图片精度

    值越大，图片越清晰，文件也越大。PDF格式默认值为720，其他格式默认值为300，单位为dpi。

    ::

        gmt psconvert -Tj -E600 test.ps

    说明：

    #. EPS是矢量图片格式，-E选项对其无效
    #. PDF是矢量图片格式，-E选项对其中的pattern和字体有效

``-Tb|e|E|f|F|j|g|G|m|s|t``
    指定要转换的图片格式。可以接如下值：

    - ``b`` ：BMP；
    - ``e`` ：EPS；
    - ``E`` ：带有PageSize命令的EPS；
    - ``f`` ：PDF；
    - ``F`` ：多页PDF；
    - ``j`` ：JPEG（默认值）；
    - ``g`` ：PNG；
    - ``G`` ：透明PNG；
    - ``m`` ：PPM；
    - ``s`` ：SVG；
    - ``t`` ：TIFF；

    说明：

    #. ``g`` 和 ``G`` 的区别在于前者背景色为白色，后者背景色为透明；
    #. 对于 ``bjgt`` 格式可以在其后加 ``-`` 将PS文件转换为灰度图；
    #. EPS格式可以与其他格式合在一起使用。比如 ``-Tef`` 会同时生成EPS和PDF文件。
       除此之外，该命令一次只能转换一种格式，比如 ``-Tbf`` 则只会生成PDF格式
       （即以 ``-T`` 选项中的最后一个格式为准）
    #. ``-TF`` 会将多个PS/PDF文件转换并合并成一个多页的PDF文件，需要使用
       ``-F`` 选项指定输出的文件名

    转换为PDF格式::

        gmt psconvert -Tf test.ps

    转换为JPG格式的灰度图::

        gmt psconvert -Tj test.ps

    利用一堆PS文件生成一个多页PDF::

        gmt psconvert -TF -Fout.pdf *.ps

.. note::
    ``psconvert`` 详解见 `https://docs.gmt-china.org/6.0.0/module/psconvert <https://docs.gmt-china.org/6.0.0/module/psconvert>`_
