from mpmath import *
mp.dps=40
def f_int(e,a=1):
    c=a*sqrt(1-e**2)
    g=lambda u:(a**4/(a**2+u)**2-c**2/(c**2+u))/((a**2+u)*sqrt(c**2+u))
    return quad(g,[0,1,10,100,inf])
def f_cl(e,a=1):
    return ((3+8*e**2*(1-e**2))*asin(e)-e*sqrt(1-e**2)*(3+10*e**2))/(4*a*e**5)
for e in [mpf('0.05'),mpf('0.3'),mpf('0.8'),mpf('0.99')]:
    print('closed',e,f_int(e)-f_cl(e), f_int(e,2)*2-f_cl(e))
# Psi' integrand vs numeric derivative
Psi=lambda s:f_cl(sqrt(s))
for s in [mpf('0.1'),mpf('0.7'),mpf('0.99')]:
    I=quad(lambda v: v*(3+4*v+2*v**2-(1-s)*(2+v))/(2*(1+v)**3*(1-s+v)**2.5),[0,1,10,inf])
    print('Psi\'',s,diff(Psi,s)-I, I, I>=mpf(22)/105)
# Fprime formula
def Fp(e):
    s=e*e;q=sqrt(1-s);al=asin(e);P=3+8*s*(1-s);Q=e*(3+10*s);N=P*al-q*Q
    Np=16*e*(1-2*s)*al+P/q+e*Q/q-q*(3+30*s);return (e*Np-5*N)/(4*e**6)
for e in [mpf('0.2'),mpf('0.8126')]: print('Fp',diff(f_cl,e)-Fp(e))
# bounds large e
mx=lambda fn: max(fn(mpf(k)/4000*0.25) for k in range(1,4001))
A=lambda q:(3+8*q**2-8*q**4)/(4*(1-q**2)**2.5); B=lambda q:(13-10*q**2)/(4*(1-q**2)**2); C=lambda q:(1+2*q**2)/(1-q**2)**1.5
print('A-3/4<=5q2',mx(lambda q:(A(q)-0.75)/q**2), 'A max',A(mpf(1)/4),'<=17/16',A(mpf(1)/4)<=mpf(17)/16)
print('B',mx(lambda q:(B(q)-3.25)/q**2),'C',mx(lambda q:(C(q)-1)/q**2))
F=lambda q:f_cl(sqrt(1-q**2))
print('R1/q3 min',min((F(q)-3*pi/8+4*q)/q**3 for q in [mpf(k)/4000*0.25 for k in range(1,4001)]),'R1/q2 max',mx(lambda q:(F(q)-3*pi/8+4*q)/q**2))
om=lambda e:2*sqrt(1-e**2)*(3-2*e**2)*asin(e)/e**3-6*(1-e**2)/e**2
omq=lambda q:om(sqrt(1-q**2))
print('Rw',min((omq(q)-pi*q+8*q**2)/q**4 for q in [mpf(k)/4000*0.25 for k in range(1,4001)]), mx(lambda q:(omq(q)-pi*q+8*q**2)/q**3))
print('small w',max(abs(om(e)-mpf(8)/15*e**2)/e**4 for e in [mpf(k)/4000/8 for k in range(1,4001)]))
print('R0',max((f_cl(e)+mpf(4)/15-mpf(22)/105*e**2)*(1-e**2)/e**4 for e in [mpf(k)/4000/8 for k in range(1,4001)]))
print('F(1/8)',f_cl(mpf(1)/8),'F(63/64)',f_cl(mpf(63)/64))
r=findroot(f_cl,0.81);print(r,om(r))
