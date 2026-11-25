import json, sys, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
fm.fontManager.addfont('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
plt.rcParams['font.family']=['DejaVu Sans','Noto Sans CJK JP']
d=json.load(open(sys.argv[1]))
def curve(a,b=None):
    pts=[(p['s'],p['t']) for p in d[a]]
    if b: pts+=[(p['s'],p['t']) for p in d[b]]
    pts=np.array(sorted(set(pts))); return np.c_[1/pts[:,0],pts[:,1]]   # y = 1/s (short), z = t (long)
Z1=curve('Z1_t_of_s','Z1_s_of_t'); D1=curve('D1_t_of_s','D1_s_of_t'); Z2=curve('Z2_t_of_s'); D2=curve('D2_t_of_s')
fig,ax=plt.subplots(figsize=(10.5,8))
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(0.24,1.0); ax.set_ylim(1,8.5)
ax.set_xticks([0.25,0.3,0.4,0.5,0.6,0.7,0.8,1.0]); ax.set_xticklabels(['0.25','0.3','0.4','0.5','0.6','0.7','0.8','1'])
ax.set_yticks([1,1.5,2,3,4,5,6,8]); ax.set_yticklabels(['1','1.5','2','3','4','5','6','8']); ax.minorticks_off()
ax.plot([0.24,1],[1,1],color='#1f6fb2',lw=7,solid_capstyle='butt',zorder=1,clip_on=False)
ax.plot([1,1],[1,8.5],color='#c2541c',lw=7,solid_capstyle='butt',zorder=1,clip_on=False)
for C in (Z1,Z2): ax.plot(C[:,0],C[:,1],'k-',lw=2.4)
for C in (D1,D2): ax.plot(C[:,0],C[:,1],'k--',lw=2.2)
kw=dict(fontsize=14,fontweight='bold')
ax.text(0.36,1.32,'Z₁',**kw); ax.text(0.28,6.2,'Z₂',**kw); ax.text(0.80,1.6,'∂₁',**kw); ax.text(0.28,2.45,'∂₂',**kw)
for y,z,l,dx,dy in [(0.40796,1,'c_o ≈ 0.408',-0.0,1.07),(0.64355,1,'b_o ≈ 0.644',0,1.07),(1,2.0654,'b_p ≈ 2.07',0.86,0.93),(1,4.7244,'c_p ≈ 4.72',0.86,1.04)]:
    ax.plot(y,z,'o',ms=10,mfc='yellow',mec='k',zorder=6,clip_on=False)
    ax.text(y*(dx if dx else 0.96),z*dy,l,fontsize=10.5,ha='right' if dx else 'center')
ax.plot(1,1,'*',ms=22,color='k',zorder=7,clip_on=False); ax.text(0.985,0.93,'球',fontsize=13,ha='right')
rk=dict(fontsize=10.5,ha='center',va='center',bbox=dict(boxstyle='round,pad=0.3',fc='white',ec='0.7',alpha=0.92))
ax.text(0.88,1.22,'中心だけ\n（極小）',**rk)
ax.text(0.53,1.33,'中心（極小）\n＋ 短軸の対',**rk)
ax.text(0.86,3.1,'中心（極小）\n＋ 短軸の対\n＋ 長軸…ではなく\n中間軸の対',**rk) if False else ax.text(0.86,3.0,'中心（極小）\n＋ 短軸の対\n＋ 中間軸の対',**rk)
ax.text(0.30,1.6,'中心だけ\n（指数 1）',**rk)
ax.text(0.45,3.6,'中心（指数 1）\n＋ 中間軸の対',**rk)
ax.text(0.45,7.4,'中心だけ（指数 2）',**rk)
ax.text(0.245,1.04,'扁平の辺 z = 1（第一論文、λ = y）',color='#1f6fb2',fontsize=11.5,fontweight='bold')
ax.text(0.985,8.1,'扁長の辺 y = 1\n（第一論文、λ = z）',color='#c2541c',fontsize=11.5,fontweight='bold',ha='right',va='top')
ax.set_xlabel('y（短い軸）　← 円盤に近づく',fontsize=12.5)
ax.set_ylabel('z（長い軸）　→ 針に近づく',fontsize=12.5)
ax.set_title('形の地図：x = 1（中間の軸）、y ≤ 1 ≤ z',fontsize=15)
fig.text(0.07,0.035,'実線 Z₁・Z₂：中心で対が生まれる・吸い込まれる　破線 ∂₁・∂₂：軸の端から対が出入りする　黄色：第一論文の閾値（辺の上で λ をそのまま読める）',fontsize=10)
fig.text(0.5,0.008,'診断用の数値（非区間・倍精度、2026-11-20 の地図 runB_curves.json を y = 1/s、z = t に変換）。確かめてあるのは二つの辺（第一論文）だけ。',ha='center',fontsize=9.5,color='0.35')
plt.tight_layout(rect=(0,0.06,1,1)); plt.savefig(sys.argv[2],dpi=150)
