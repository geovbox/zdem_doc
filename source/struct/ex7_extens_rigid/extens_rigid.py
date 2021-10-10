#2019-06-29
#建议使用notepad++查看本文件
#LI ChangSheng @ NanJing Uninversity 
#E-mail: sheng0619@163.com
#more info, see www.geovbox.com
######################################
# title: 刚性基底伸展构造实例
#括号内参数可根据模型大小及个人需要修改
#脚本命令不区分大小写
#该计算在南京大学高性能计算中心
#######################################
#程序初始化
START
#颗粒设为球，计算颗粒体积用4/3*pi*r^3计算
SET DISK off
#设置研究范围 
BOX LEFT 1.0e-3 RIGHT (51000.0) BOTTOM 1.0e-3 HEIGHT (26000.0) kn=4e10 ks=4e10 fric 0.30 
#设置挡板墙，这里模型采用hertz接触模型，挡板墙的kn ks无效，计算时取颗粒的参数
WALL ID 0, NODES (  10000.0 ,  26000.0 ) ( 10000.0 ,    1080.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR black
WALL ID 1, NODES (  40000.0 ,   1080.0 ) ( 40000.0 ,   26000.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR blue
#设置基底
GLINE P1 (   10000.0 , 1160.0 ) P2 ( 20000.0 ,   1160.0 ) RAD 80.0 GROUP bom_wall1
GLINE P1 (   10000.0 , 1000.0 ) P2 ( 40000.0 ,   1000.0 ) RAD 80.0 GROUP bom_wall2
PROP COLOR blue  RANGE GROUP bom_wall1
PROP COLOR red   RANGE GROUP bom_wall2
#限制颗粒位移和转动
FIX x y spin RANGE GROUP bom_wall1
FIX x y spin RANGE GROUP bom_wall2
#在矩形范围内生成颗粒
GEN NUM 100000, RAD DISCRETE (60.0 80.0)  x (10000.0, 40000.0) y (1000.0, 26000.0) GROUP ball_rand
PROP COLOR black RANGE GROUP ball_rand
PROP DEN 2.5e3 FRIC 0.0 SHEAR 2.9e9 POISS 0.2 DAMP 0.4 HERTZ

SET  STEPBAR  1000
SET  SAVE    20000
set  PRINT   10000
set  PS      10000

SET DT 5e-2     
SET GRAVITY ( 0.0,  -10.0 )

CYC  50000
#删除10000米以上的颗粒，可实现剥蚀
DEL  RANGE y (11000.0, 25000.0)
CYC  10000
EXP  initxyr.dat RANGE GROUP ball_rand
SAV  initxyr.sav
################################ 设置颜色 #########################################
prop color lg  RANGE GROUP ball_rand
prop color mg  RANGE  x 101.0 59999.0 y   261.0 1000.0
prop color mg  RANGE  x 101.0 59999.0 y 2000.0  3000.0
prop color mg  RANGE  x 101.0 59999.0 y 4000.0  5000.0
prop color mg  RANGE  x 101.0 59999.0 y 6000.0  7000.0
prop color mg  RANGE  x 101.0 59999.0 y 8000.0  9000.0
prop color mg  RANGE  x 101.0 59999.0 y 10000.0  11000.0
PROP FRIC 0.3 RANGE GROUP bom_wall1
prop FRIC 0.3 RANGE GROUP bom_wall2
#设置粘结
PROP ebmod 2e8 gbmod 2e8 tstrength 2e7 sstrength 4e7 fric 0.3 RANGE GROUP ball_rand
#开始伸展
INI  XV 2.0 RANGE GROUP bom_wall2
WALL ID 1 XV 2.0
IMPLE WALL ID 1 XMOVE 2000.0 SAVE 2000.0 PRINT 1000.0 PS 1000.0

################################# 沉积1 #########################################
gen NUM 200000, rad discrete 60.0 80.0 , x( 10000.0, 42000.0)   y (10000.0, 14000.0 )  GROUP ballsed1
PROP COLOR blue DEN 2.5e3 FRIC 0.3 SHEAR 2.9e9 POISS 0.2  DAMP 0.0  HERTZ RANGE GROUP ballsed1 
#新沉积的颗粒粘结（胶结）在一起
#prop ebmod 2e8 gbmod 2e8 tstrength 2e7 sstrength 4e7 fric 0.3 range group ballsed1 
INI  XV 0.0 RANGE GROUP bom_wall2
WALL ID 1 XV 0.0
set ps    1000
set print 1000
CYC 5000
DEL RANGE y 11000.0 16000.0
CYC 2000
#开始伸展
INI  XV 2.0 RANGE GROUP bom_wall2
wall id 1 xv 2.0
IMPLE WALL ID 1 XMOVE 2000.0 SAVE 2000.0 PRINT 1000.0 PS 1000.0

################################# 沉积2 #########################################
gen NUM 200000, rad discrete 60.0 80.0 , x( 10000.0, 44000.0)  y (10000.0, 14000.0 ),  GROUP ballsed2
PROP color red den 2.5e3, fric 0.3, shear 2.9e9, poiss 0.2, damp 0.0, hertz  range group ballsed2 
INI  XV 0.0 RANGE GROUP bom_wall2
WALL ID 1 XV 0.0
set ps    1000
set print 1000
CYC 5000
DEL RANGE y 11000.0 16000.0
CYC 2000

#开始伸展
INI  XV 2.0 RANGE GROUP bom_wall2
wall id 1 xv 2.000
IMPLE WALL ID 1 XMOVE 2000.0 SAVE 2000.0 PRINT 1000.0 PS 1000.0

################################# 沉积3 #########################################
gen NUM 200000, rad discrete 60.0 80.0 , x( 10000.0, 46000.0)   y (10000.0, 14000.0 ),  GROUP ballsed3
PROP color mg den 2.5e3, fric 0.3, shear 2.9e9, poiss 0.2, damp 0.0, hertz  range group ballsed3 
INI  XV 0.0 RANGE GROUP bom_wall2
WALL ID 1 XV 0.0
set ps    1000
set print 1000
CYC 5000
DEL RANGE y 11000.0 16000.0
CYC 2000

#开始伸展
INI  XV 2.0 RANGE GROUP bom_wall2
wall id 1 xv 2.000
IMPLE WALL ID 1 XMOVE 2000.0 SAVE 2000.0 PRINT 1000.0 PS 1000.0

################################# 沉积4 #########################################
gen NUM 200000, rad discrete 60.0 80.0 , x( 10000.0, 48000.0)   y (10000.0, 14000.0 ),  GROUP ballsed4
PROP color gb den 2.5e3, fric 0.3, shear 2.9e9, poiss 0.2, damp 0.0, hertz  range group ballsed4 
INI  XV 0.0 RANGE GROUP bom_wall2
WALL ID 1 XV 0.0
set ps    1000
set print 1000
CYC 5000
DEL RANGE y 11000.0 16000.0
CYC 2000

#结束计算
STOP
