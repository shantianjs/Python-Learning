import matplotlib.pyplot as pt
import numpy as np
import chardet
import random
from xpinyin import Pinyin

def draw():
	n = 40
	x = np.arange(0, 1e2)
	y = 100 * x ** 3
	z = 0.5 * 2 ** x
	pt.plot(x, y, color='green', label='y = 100 * n**3')
	pt.plot(x, z, color='red', label='z = 0.5 * 2**n')
	pt.xlim(0, 1.2 * n)
	pt.ylim(0, 1.5e6)
	pt.xlabel('Degree')
	pt.ylabel('Value')
	pt.title('sin&cos function ptot')
	pt.legend()  # 注册line label
	pt.savefig(f'E:/{random.randint(1,100)}.png')
	pt.show()

def draw_bar():
	data = '''北    京	7355291
	天    津	3963604
	河    北	20813492
	山    西	10654162
	内 蒙 古	8470472
	辽    宁	15334912
	吉    林	9162183
	黑 龙 江	13192935
	上    海	8893483
	江    苏	25635291
	浙    江	20060115
	安    徽	19322432
	福    建	11971873
	江    西	11847841
	山    东	30794664
	河    南	26404973
	湖    北	17253385
	湖    南	19029894
	广    东	32222752
	广    西	13467663
	海    南	2451819
	重    庆	10272559
	四    川	26383458
	贵    州	10745630
	云    南	12695396
	西    藏	689521
	陕    西	11084516
	甘    肃	7113833
	青    海	1586635
	宁    夏	1945064
	新    疆	6902850'''

	data = data.split('\n')
	d = {}
	pinyin = Pinyin()

	for i in data:
		k = pinyin.get_initials(i[:6].strip().replace(' ',''),'')
		v = int(i[6:].strip())
		d[k] = v
	pt.figure(figsize=(9,6))
	ind = np.arange(len(d))

	pt.bar(ind,d.values(),alpha=0.9,width=0.5,facecolor = 'lightskyblue',edgecolor = 'white',label = '人口',lw=1)
	pt.xticks(ind,d.keys())
	pt.plot(ind,d.values(),color='red',label='plot',lw=1,alpha=0.6)
	pt.title('china population')
	pt.legend(loc = "upper left")
	pt.savefig(f'{random.randint(1,100)}.png')
	pt.show()

def points():
	x = np.linspace(0,2*np.pi,100)
	pt.plot(x,np.sin(x),'bo',alpha=0.6,color='red')
	pt.savefig(f'{random.randint(1,100)}.png')
	pt.show()

