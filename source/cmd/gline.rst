.. index:: ! gline

gline
=====

:说明: ``gli[ne]`` 在两个点之间建立一组线形排列的颗粒

使用方法::

   GLINE RAD=<float> P1 ( <float> <float> ) P2 ( <float> <float> ), KN=<float> KS=<float> FRIC=<float>, [COLOR=<str>] , [GROUP=<str>], [CRATIO=<float>] 

其中，CRATIO为初始叠和率，cratio = |OA|/(rO+rA)，取值范围(0.0~1.0]。当颗粒刚好接触时，cratio=(rO+rA)/(rO+rA)=1.0；当颗粒完全重合时，cratio=0.0/(rO+rA)=0.0

实例::

   # 在点 ``( 2.0  10.0 )`` 和点 ``( 40.0  10.0 )`` 间生成半径为0.5的颗粒，法向刚度系数kn=4.14e3，切向刚度系数ks=4.14e3，摩擦系数fric=0.55，颜色color=red，组名GROUP=bom
   GLINE RAD=0.5 P1 ( 2.0  10.0 ) P2 ( 40.0  10.0 ), kn=4.14e3 ks=4.14e3 fric=0.55 color=red GROUP=bom
   # 初始叠合率设置为0.8，颗粒圆心间的距离为|OA| = (rO+rA)*cratio=(0.5+0.5)*0.8=0.8
   GLINE RAD=0.5 P1 ( 2.0  10.0 ) P2 ( 40.0  10.0 ), kn=4.14e3 ks=4.14e3 fric=0.55 color=red GROUP=bom CATRIO=0.8
