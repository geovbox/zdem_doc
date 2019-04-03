Windows下使用
=============

.. NOTE::

	小白用户请参考 `如何在南京大学高性能计算中心使用VBOX <http://t.cn/Ei0epmg>`_

#. 申请南京大学高性能计算中心帐号，申请办法见 :ref:`njuhpc` 。
#. 下载安装 `Xshell <https://www.netsarang.com/products/xsh_overview.html>`_ ， 使用 ``Xshell`` 连接南京大学高性能计算中心的集群。

   - 文件-新建
   - 连接 `nju` 主机 `hpcc.nju.edu.cn` 端口号 `8801`   
   - 连接-用户身份验证 用户名: `zhang_san`  密码 `123456`
   - 登陆成功后，输入::

       vbox -v

    输出::
   
      VBOX 1.3(2018-10-28) (Education @ Nanjing University)

    成功！


#. 下载安装 `Xftp <https://www.netsarang.com/products/xfp_overview.html>`_ ，实现在主机（南京大学高性能计算中心的集群）和本地电脑间传输数据。
#. 使用 ``gsview`` 查看ps图片格式计算结果。
    - 安装 ``gsview`` 
        - `gsv50w32.exe <http://www.ghostgum.com.au/download/gsv50w32.exe>`_ Win32 self extracting archive  
        - `gsv50w64.exe  <http://www.ghostgum.com.au/download/gsv50w64.exe>`_ Win64 (x86_64) self extracting archive 
    - 安装 ``Ghostscript``
        - `Ghostscript 9.26 for Windows (32 bit) <https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs926/gs926aw32.exe>`_
        - `Ghostscript 9.26 for Windows (64 bit)  <https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs926/gs926aw64.exe>`_ 



   
.. TODO::

    如何使用 `paraview <https://www.paraview.org/>`_ 查看vtk格式计算结果

