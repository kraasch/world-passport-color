#!/usr/bin/env python3

import pandas as pd

csv1 = pd.read_csv('./testPoints.txt', sep=';', names=('ixs', 'iys', 'gxs', 'gys', 'names'))

ixz = csv1.ixs.to_numpy()
iyz = csv1.iys.to_numpy()
gxz = csv1.gxs.to_numpy()
gyz = csv1.gys.to_numpy()
naz = csv1.names.to_numpy()


print('-' * 110)
for lbl in ['x geo','x px','x px2','diff','','y geo','y px','y px2','diff','','name']:
    print(lbl,'\t', end='')
print()
print('-' * 110)

for x,y,gx,gy,name in zip( ixz, iyz, gxz, gyz, naz ):
    a=-1907
    b=14
    c=0.3
    d=-0.00249
    nx=(1-gx*gx*gx)*d+(1-gx*gx)*c+(1-gx)*b+(gx-a)
    ny=649

    print( 
            str(gx)[:5], '\t', 
            int(x), '\t', 
            int(nx), '\t', 
            int(nx-x), '\t', 
            '---', '\t', 
            str(gy)[:5], '\t', 
            int(y), '\t', 
            int(ny), '\t', 
            int(ny-y), '\t',
            '---', '\t', 
            name)

