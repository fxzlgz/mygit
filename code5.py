import re

#:re模块
#pattern=r"\w+:\d+"
# pattern=r"(\w+):(\d+)"
# s="zhang:1994  li:1993"
# l=re.findall(pattern,s)
# print(l)

#
# pattern=r"(\w+):(\d+)"
# s="zhang:1994  li:1993"
# #regex调用
#
# regx=re.compile(pattern)
# l=regx.findall(s,pos=0,endpos=60)
# print(l)

#
# l=re.split(r'\s+','hello word')
# print(l)


s=re.sub(r'垃圾',r'**',"玩的禎垃圾，张三禎垃圾")
#s=re.sub(r'垃圾','**',"玩的禎垃圾，张三禎垃圾",1)
print(s)



s=re.subn(r'垃圾','**',"玩的禎垃圾，张三禎垃圾")
print(s)


