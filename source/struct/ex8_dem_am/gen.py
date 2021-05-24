######################################
# title: 离散元数值模拟与构造物理模拟对比试验:1 沉积
# date: 2021-05-16
# authors: 李长圣
# E-mail: sheng0619@163.com
# ref: Li et al. (2021) Calibration of the discrete element method and modelling of shortening experiments. Front. Earth Sci. doi: 10.3389/feart.2021.636512
# more info, see www.geovbox.com
#######################################
start
set disk hex
BOX left 0.5e-3 right 615.0e-3 bottom 0.5e-3 height 110.0e-3 kn=1.5e4 ks=1.5e4 fric 0.3 

wall id 4, nodes (     5e-3  158.0e-3) (  5.0e-3     5.0e-3), kn= 1.5e4 ks= 1.5e4 fric 0.0 
wall id 5, nodes (     5e-3    5.0e-3) (605.0e-3     5.0e-3), kn= 1.5e4 ks= 1.5e4 fric 0.0 
wall id 6, nodes ( 605.0e-3    5.0e-3) (605.0e-3   158.0e-3), kn= 1.5e4 ks= 1.5e4 fric 0.0 

gen grid idmin 0 rad discrete 0.1e-3 0.1e-3 0.2e-3 0.2e-3 0.25e-3 0.3e-3,  x (5.0e-3,  605.0e-3), y (5.0e-3, 155.0e-3), GROUP ball_rand 

PROP color red den 1.3e3, fric 0.0, kn  1.5e4, ks  1.5e4 damp 0.4
FIX spin

SET frac 0.4
SET GRAVITY ( 0.0,  -10.0 )
SET  stepbar 1000
SET  save  20000
SET  print 20000
SET  ps    20000
HIST ID 1 INTERVAL 1000 , kinetic
HIST ID 2 INTERVAL 1000 , step
PLOT hist 2 1

CYC 60000
DEL range x (4.0e-3, 606.0e-3), y (30.0e-3, 1.0),
CYC 20000
#save 2del.sav
EXP ini_xyr.dat
STOP
