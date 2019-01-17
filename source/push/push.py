######################################
# title: 一个实例学会VBOX
# date: 2019-01-13
# authors: 李长圣
# E-mail: sheng0619@163.com
# note:
# 括号内参数可根据模型大小及个人需要修改
# 脚本命令不区分大小写
# 用16个核心，实际用时<1小时
# 计算费用约<2元
# more info, see www.geovbox.com
#######################################
#程序初始化
START
#颗粒设为球，计算颗粒体积用4/3*pi*r^3计算
set disk off
#设置研究范围 
BOX left 0.0 right 41000.0 bottom 0.0 height 11000.0 kn=0e10 ks=0e10 fric 0.00 
#设置挡板墙，这里模型采用hertz接触模型，挡板墙的kn ks无效，计算时取颗粒的参数
WALL ID 0, NODES (      0.0 ,     10.0 ) (  40000.0 ,     10.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR black
WALL ID 1, NODES (     10.0 ,  10000.0 ) (     10.0 ,     10.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR blue
WALL ID 2, NODES (  40000.0 ,     10.0 ) (  40000.0 ,  10000.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR red
#在矩形范围内生成颗粒
GEN NUM 100000.0 rad discrete 60.0 80.0,  x ( 10.0, 40000.0), y ( 10.0, 10000.0), COLOR black GROUP ball_rand
#设置颗粒的微观参数
PROP DENSITY 2.5e3, fric 0.0, shear 2.9e9, poiss 0.2, damp 0.4, hertz
#设置时间步及重力加速度
SET  DT 5e-2,  GRAVITY  0.0,  -9.8 
#设置每1000步保存一次ps格式的计算结果
SET  ps 1000
#设置每1000步保存一次dat格式的计算结果
SET  print 1000
#沉积，计算5000步
CYC 5000
#删除6000米以上的颗粒
DEL RANGE y 4000.0 999000.0
#平衡，计算1000步
CYC 1000
#输出包含颗粒的[x y r]信息的初始模型 init_xyr.dat
#EXP init_xyr.dat

#设置bond粘结，使颗粒具有粘聚力
PROP ebmod 2e8 gbmod 2e8  tstrength 2e7 sstrength 4e7 fric 0.3 
#给地层赋上颜色
PROP COLOR lg          range y    0.0   500.0
PROP COLOR green       range y  500.0  1000.0
PROP COLOR yellow      range y 1000.0  1500.0
PROP COLOR red         range y 1500.0  2000.0
PROP COLOR black       range y 2000.0  2500.0
PROP COLOR mg          range y 2500.0  3000.0
PROP COLOR blue        range y 3000.0  3500.0
PROP COLOR gb          range y 3500.0  4000.0
PROP COLOR violet      range y 4000.0  4500.0

#设置挡板墙摩擦系数
WALL id 0 fric 0.3
WALL id 1 fric 0.3
WALL id 2 fric 0.3
#设置墙的挤压速度 x方向速度为2.0
WALL id 1 xv 2.0
#设置墙的挤压量x方向推进16000.0，每挤压2000.0保存一次计算结果
IMPLE wall id 1 xmove 10000.0 save 2000.0 print 1000.0 ps 1000.0
#计算停止
STOP
