% function HelloDEM  % Galileo’s leaning Tower of Pisa experiment 
M_Ball_Steel=10.0; % 10 kg streel ball 
M_Ball_Wood=1.0;   % 1 kg wood ball 
Y0_Ball_Steel = 100.0; % initiall position 
Y0_Ball_Wood  = 100.0; 
dT     = 0.01; % time step 
Nloops = 500; % number of cycles 
G      = 9.8; % gravitational constant 
U_Ball_Steel = 0.0; % initiall displacement 
U_Ball_Wood  = 0.0; 
V_Ball_Steel = 0.0; % initiall velocity 
V_Ball_Wood  = 0.0; 
A_Ball_Stell = 0.0; % accelerated velocity 
A_Ball_Wood  = 0.0; 
Y_Ball_Steel = Y0_Ball_Steel; % initiall position 
Y_Ball_Wood  = Y0_Ball_Wood; 
t   = 0.0; 
t_H = [];% history of time  
Y_H_Ball_Steel = []; 
Y_H_Ball_Wood  = [];
for i=1:NLoops 
    F_Ball_Steel=-G*M_Ball_Steel; %ball force,constitutive model 
    F_Ball_Wood = -G*M_Ball_Wood; 
    A_Ball_Steel= F_Ball_Steel/M_Ball_Steel; %Newton’s second law 
    A_Ball_Wood = F_Ball_Wood /M_Ball_Wood; 
    V_Ball_Steel= V_Ball_Steel+A_Ball_Steel*dT; %update velocity 
    V_Ball_Wood = V_Ball_Wood+A_Ball_Wood*dT; 
    U_Ball_Steel=U_Ball_Steel+V_Ball_Steel*dT; %update displacement 
    U_Ball_Wood  = U_Ball_Wood+ V_Ball_Wood*dT; 
    Y_Ball_Steel = Y0_Ball_Steel + U_Ball_Steel; %update position 
    Y_Ball_Wood  = Y0_Ball_Wood  + U_Ball_Wood; 
    t=t+dT; 
    %record history 
    t_H=[t_H,t]; 
    Y_H_Ball_Steel=[Y_H_Ball_Steel,Y_Ball_Steel]; 
    Y_H_Ball_Wood=[Y_H_Ball_Wood,Y_Ball_Wood]; 
end
plot(t_H,Y_H_Ball_Steel,'k','linewidth',1); 
hold on; 
plot(t_H(1:20:end),Y_H_Ball_Wood(1:20:end),'ks','MarkerFace','y'); 
Ground=zeros(1,length(t_H)); 
plot(t_H,Ground,'r'); 
xlabel('Time [s]') 
ylabel('Height [m]') 
le=legend('Steel Ball','Wood Ball','Ground'); 
