######################################
# title: 滑脱层设置方法
# date: 2019-06-29
# authors: 李长圣
# E-mail: sheng0619@163.com
# more info, see www.geovbox.com
#######################################
# init_xyr.dat 保存了沉积后的所有颗粒的[x y r]信息，由一个实例学会VBOX生成
LOAD init_xyr.dat
#导入的颗粒命名为 ball_rand
PROP GROUP ball_rand
#关闭圆盘，颗粒设为球，计算颗粒体积用4/3*pi*r^3计算
SET DISK OFF
#设置研究范围 
BOX LEFT 0.0 RIGHT 41000.0 BOTTOM 0.0 HEIGHT 11000.0 KN=0e10 KS=0e10 FRIC=0.00 
#设置挡板墙，这里模型采用hertz接触模型，挡板墙的kn ks无效，计算时取颗粒的参数
WALL ID 0, NODES (      0.0 ,     10.0 ) (  40000.0 ,     10.0 ), KN=0e10 KS=0e10 FRIC=0.0 COLOR black
WALL ID 1, NODES (     10.0 ,  10000.0 ) (     10.0 ,     10.0 ), KN=0e10 KS=0e10 FRIC=0.0 COLOR blue
WALL ID 2, NODES (  40000.0 ,     10.0 ) (  40000.0 ,  10000.0 ), KN=0e10 KS=0e10 FRIC=0.0 COLOR red

#设置颗粒的微观参数
PROP DENSITY 2.5e3, FRIC 0.0, SHEAR 2.9e9, POISS 0.2, DAMP 0.4, HERTZ
#设置时间步及重力加速度
SET  DT 5e-2,  GRAVITY  0.0,  -9.8 

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

################################### 滑脱层设置 ####################################
#用range y (ymin ymax)圈定范围，该范围内颗粒命名为detachment
PROP GROUP detachment RANGE y ( 0.0, 1000.0)
#打断detachment组内的颗粒粘结
BOND break RANGE GROUP detachment
#将detachment组的颗粒颜色设置为红色，摩擦系数设置为0.0，摩擦系数可以根据断层强弱改变
PROP COLOR red FRIC 0.0 DEN 2.2e3 RANGE GROUP detachment
################################################################################

#设置挡板墙摩擦系数
WALL ID 0 fric 0.0
WALL ID 1 fric 0.3
WALL ID 2 fric 0.3
#设置墙的挤压速度 x方向速度为2.0
WALL ID 1 XV 2.0
#设置墙的挤压量x方向推进10000.0，每挤压1000.0保存一次计算结果
IMPLE WALL ID 1 XMOVE 10000.0 SAVE 1000.0 PRINT 1000.0 PS 1000.0
#计算停止
STOP
