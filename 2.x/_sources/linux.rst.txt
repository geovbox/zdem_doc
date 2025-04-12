Linux命令行
===========

使用软件应该具备Linux命令行基本操作知识。

- 查看当前所在目录

::

    pwd

输出 ``/share/home/zhangsan``

- 列出当前目录下的目录和文件

::

    ls

输出 ``backup.sh  bin  Desktop  git  help  programs  projects  vbox``

- 改变当前目录

到当前目录下的 ``Desktop`` 目录里

::

    cd Desktop

到上一级目录。当前目录 ``.`` 上级目录 ``..``

::

    cd ..

- 创建目录

在当前目录下创建一个 ``data`` 目录

::

    mkdir data 

- 删除文件或目录

删除当前目录下 ``a.txt``

::

    rm a.txt

递归删除当前目录下的 ``data`` 目录中的全部内容和 ``data`` 目录本身

::

    rm -r data 

- 移动或换名 ``mv <源文件或原目录> <目标文件或目标目录>``

::

    mv vi.tex vi.txt #把文件vi.tex 换名为vi.txt
    mv data data1    #把目录data 换名为data1
    mv data ..       #把目录data 移动到上级目录

- 复制文件或目录 ``cp <参数> [源文件] [目标文件或路径]``

::

    cp a.txt b.txt # 把当前目录下的a.txt复制一份，并命名为b.txt
    cp -r data ../maya # 把当前目录下的data目录复制到上一级目录下的maya 目录中

- 分屏查看文件内容 `more, less <参数> <文件名>`

分屏查看文件 ``example.txt`` 的内容。按空格键向下翻页，b向上翻页

::

    more example.txt

- 改变文件属性 ``chmod <参数> <属性> <文件名或目录>``

将文件 ``example.txt`` 改成自己可读、可写、可执行同组和其他用户只准读和执行

::

    chmod 755 exaple.txt 

.. note::
    更详细的教程请参考 `Linux命令行基本操作知识 <http://www.runoob.com/linux/linux-tutorial.html>`_ 。


