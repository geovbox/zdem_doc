.. index:: ! convert

convert
=======


:说明: 读取 ``jpg`` ``tif`` 等格式的图片，生成　``gif``。


可选选项
--------

``-delay=<int>``
    播放速度，一般取100
    
    
- 实例 ``convert -delay 100 ./data/*[0-9].jpg -loop 0 ./data/process.gif  #　制作 gif``
    读取目录 ``./data`` 中的图片 ``*[0-9].jpg`` ，并生成 ``process.gif`` ，保存到 ``./data`` 中。






