Windows下使用
=============

.. NOTE::

	小白用户请参考 `如何在南京大学高性能计算中心使用VBOX <http://t.cn/Ei0epmg>`_

#. 申请南京大学高性能计算中心帐号，申请办法见 :ref:`njuhpc` 。
#. 下载安装 `Xshell <https://www.netsarang.com/products/xsh_overview.html>`_ ， 使用 ``Xshell`` 连接南京大学高性能计算中心的主机。

   - 文件-新建
   - 连接 南京大学高性能计算中心的主机 ``hpcc.nju.edu.cn`` 端口号 ``8801`` 
   
    .. figure:: 5.png
       :width: 80%
       :align: center
       
   - 连接-用户身份验证 填入南京大学高性能计算中心分配给你的用户名和密码，点击连接，登陆成功。
   
     .. figure:: 6.png
       :width: 80%
       :align: center

#. 下载安装 `Xftp <https://www.netsarang.com/products/xfp_overview.html>`_ ，实现在主机（南京大学高性能计算中心的集群）和本地电脑间传输数据。下载VBOX的官方实例 example，下载完，利用 ``Xftp`` 将 example 传输到主机。

    百度网盘 ``example`` 下载 
    
    链接：``https://pan.baidu.com/s/1bCYXzA3cITksu3jQRl8tCw``  提取码： ``0h7r``   
        
    .. figure:: 10.png
      :width: 80%
      :align: center

#. 配置环境变量并，运行示例 ``ex1_push`` ，在 ``Xshell`` 中，输入::
   
    cd example  #进入example目录
    chmod a+x ./vboxinstall.sh #修改执行权限
    ./vboxinstall.sh #安装vbox
    source ~/.bashrc #更新环境变量
    cd ex1_push #进入ex1_push目录
    vbox push.py # 开始计算

#. 计算完成后，将 ``ex1_push`` 下载到本地，``ex1_push/data`` 中保存了计算结果。可以使用 ``gsview`` 查看ps图片格式计算结果。

    - 安装 ``gsview`` 
    
        - `gsv50w32.exe <http://www.ghostgum.com.au/download/gsv50w32.exe>`_ Win32 self extracting archive  
        - `gsv50w64.exe  <http://www.ghostgum.com.au/download/gsv50w64.exe>`_ Win64 (x86_64) self extracting archive 
    - 安装 ``Ghostscript``
    
        - `Ghostscript 9.26 for Windows (32 bit) <https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs926/gs926aw32.exe>`_
        - `Ghostscript 9.26 for Windows (64 bit)  <https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs926/gs926aw64.exe>`_ 



   
.. TODO::

    如何使用 `paraview <https://www.paraview.org/>`_ 查看vtk格式计算结果

