######################################
# title: 一个实例学会ZDEM
# 简化版，测试DSH-SLOP
# date: 2026-11-16
# authors: 李长圣
# E-mail: sheng0619@163.com
#######################################
START
set disk off
BOX left 0.0 right 21000.0 bottom 0.0 height 6000.0 kn=0e10 ks=0e10 fric 0.00 
WALL ID 0, NODES (      0.0 ,     10.0 ) (  20000.0 ,     10.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR black
WALL ID 1, NODES (     10.0 ,   5000.0 ) (     10.0 ,     10.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR blue
WALL ID 2, NODES (  20000.0 ,     10.0 ) (  20000.0 ,   5000.0 ), kn=0e10 ks=0e10 fric 0.0 COLOR red
GEN NUM 100000.0 rad discrete 60.0 80.0,  x ( 10.0, 20000.0), y ( 10.0, 3000.0), COLOR black GROUP ball_rand
PROP DENSITY 2.5e3, fric 0.0, shear 2.9e9, poiss 0.2, damp 0.4, hertz
SET  DT 5e-2,  GRAVITY  0.0,  -9.8 
SET  ps 1000
SET  print 200
SET stepbar 200

CYC 1000

PROP fric 0.3 
PROP COLOR red         range y    0.0   500.0
PROP COLOR blue        range y  500.0  1000.0
PROP COLOR mg          range y 1000.0  1500.0
PROP COLOR mg          range y 1500.0  2000.0

WALL id 0 fric 0.3
WALL id 1 fric 0.3
WALL id 2 fric 0.3

WALL id 1 xv 2.0
IMPLE wall id 1 xmove 5000.0 save 5000.0 print 1000.0 ps 5000.0
STOP
