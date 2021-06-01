import os
try:
    file = open('1.txt','r')
except:
    file = open('1.txt','w')
    file.close()
