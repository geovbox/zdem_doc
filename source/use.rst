在Windows下使用
===============


#. 使用 `xshell <https://www.netsarang.com/products/xsh_overview.html>`_ 连接安装了VBOX的服务器 
#. 使用 `xftp <https://www.netsarang.com/products/xfp_overview.html>`_ 在服务器和本地电脑间传输数据
#. 使用 `paraview <https://www.paraview.org/>`_ 查看vtk格式计算结果
#. 使用 `gsview <http://pages.cs.wisc.edu/~ghost/>`_ 查看ps格式计算结果


- 使用xshell 连接服务器

   - 文件-新建
   - 连接 `nju` 主机 `hpcc.nju.edu.cn` 端口号 `8801`   
   - 连接-用户身份验证 用户名: `zhang_san`  密码 `123456`
   - 登陆成功后，输入::

       vboxdaily -v

    输出::
   
      VBOX 1.3(2018-10-28) (Education @ Nanjing University)

    成功！

.. note::

   帐号申请办法见 :ref:`njuhpc`


