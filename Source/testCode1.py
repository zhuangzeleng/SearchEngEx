#-*- encoding: utf-8 -*-

'''
Created on 2014年7月26日

@author: LachrY
'''
import testCode
import requests

print testCode.__file__
testCode.AA.helloPrint()

r = requests.get ('http://www.qq.com')
f = file('hhh.html', 'w')
f.write(r.content)
print r.encoding