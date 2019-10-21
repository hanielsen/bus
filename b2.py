#coding: utf-8
import sys

def f1(lni,ll):
    m='var l{0:}=['.format(lni)
    u=ll[0].split(',')
    m+='["'+u[0]+'",'+'"'+u[1]+'",'+u[2][:-1]+'],\n'
    for t in ll[1:61]:
        m+='['+t[:-1]+'],\n'
    m=m[:-2]+'];\n'
    outfile.write(m)
    m='var r{0:}=['.format(lni)
    u=ll[61].split(',')
    m+='["'+u[0]+'",'+'"'+u[1]+'",'+u[2][:-1]+'],\n'
    for t in ll[62:122]:
        m+='['+t[:-1]+'],\n'
    m=m[:-2]+'];\n'
    outfile.write(m)
        
lname=['11','12','15','6A']

with open('v1.txt',encoding='utf-8', mode='w') as outfile:
    for lni in lname:
        with open('{0:}.csv'.format(lni),'r') as infile:
            ll=infile.readlines()
        f1(lni,ll)    
