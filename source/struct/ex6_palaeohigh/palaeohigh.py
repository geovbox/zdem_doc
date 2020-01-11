######################################
# title: 古隆起设置方法
# date: 2019-06-29
# authors: 李长圣
# E-mail: sheng0619@163.com
# more info, see www.geovbox.com
#######################################
#程序初始化
LOAD init_xyr.dat
#导入的颗粒命名为 ball_rand
PROP GROUP ball_rand
#关闭圆盘，颗粒设为球，计算颗粒体积用4/3*pi*r^3计算
SET disk off
#设置研究范围 
BOX left 0.0 right 41000.0 bottom 0.0 height 11000.0 kn=0e10 ks=0e10 fric 0.00 
#设置挡板墙，这里模型采用hertz接触模型，挡板墙的kn ks无效，计算时取颗粒的参数
WALL ID 0, NODES (      0.0 ,     10.0 ) (  40000.0 ,     10.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR black
WALL ID 1, NODES (     10.0 ,  10000.0 ) (     10.0 ,     10.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR blue
WALL ID 2, NODES (  40000.0 ,     10.0 ) (  40000.0 ,  10000.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR red
#设置颗粒的微观参数
PROP DENSITY 2.5e3, FRIC 0.0, SHEAR 2.9e9, POISS 0.2, DAMP 0.4, HERTZ
#设置时间步及重力加速度
SET  DT 5e-2,  GRAVITY  (0.0,  -9.8) 

#设置bond粘结，使颗粒具有粘聚力
PROP ebmod 2e8 gbmod 2e8  tstrength 0e7 sstrength 0e7 fric 0.3 
#给地层赋上颜色
PROP COLOR lg          range y    0.0   500.0
PROP COLOR green       range y  500.0  1000.0
PROP COLOR yellow      range y 1000.0  1500.0
PROP COLOR white       range y 1500.0  2000.0
PROP COLOR black       range y 2000.0  2500.0
PROP COLOR mg          range y 2500.0  3000.0
PROP COLOR blue        range y 3000.0  3500.0
PROP COLOR gb          range y 3500.0  4000.0
PROP COLOR violet      range y 4000.0  4500.0

################################### 隆起设置 ####################################
#用ellipse指定椭圆，椭圆的中心（2000.0, 0.0） 长轴 2000.0 短轴 1000.0
PROP GROUP palaeohigh RANGE ellipse ( 20000.0,  0.0)  2000.0, 1000.0
#用range P4 (point1) (point2) (point3) (point4) 命令，逆时针指定四个点
#四个点组成的多边形，设置为组 palaeohigh
PROP GROUP palaeohigh RANGE P4 ( 10000.0,  0.0) ( 12000.0,  0.0) ( 15000.0  0.0) ( 12500.0  1500.0)
#打断struct1组内的颗粒粘结
BOND break RANGE GROUP palaeohigh
FIX x y spin RANGE GROUP palaeohigh
#将palaeohigh组的颗粒颜色设置为黑色 
PROP COLOR black  RANGE GROUP palaeohigh
################################################################################

#设置挡板墙摩擦系数
WALL id 0 fric 0.0
WALL id 1 fric 0.3
WALL id 2 fric 0.3
#设置墙的挤压速度 x方向速度为2.0
WALL id 1 xv 2.0
#设置墙的挤压量x方向推进10000.0，每挤压1000.0保存一次计算结果
IMPLE WALL id 1 xmove 10000.0 save 1000.0 print 1000.0 ps 1000.0
#计算停止
STOP

