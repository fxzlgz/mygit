import  re

##匹配ASCII码
# regex=re.compile(r'\w+',flags=re.A)
#
# s='''Welcome to
# 北京
# '''
# l=regex.findall(s)
# print(l)



# #匹配忽略大小写
# regex=re.compile(r'[A-Z]\w+',flags=re.I)
# s='''Welcome to
# 北京
# '''
# l=regex.findall(s)
# print(l)

# #使 . 可以匹配换行
# regex=re.compile(r'.+',flags=re.S)
# s='''Welcome to
# 北京
# '''
# l=regex.findall(s)
# print(l)

# #使^ $ 匹配每一行的开头和结尾
# regex=re.compile(r'^北京',flags=re.M)
# s='''Welcome to
# 北京
# '''
# l=regex.findall(s)
# print(l)

#匹配ASCII和不区分大小写
regex=re.compile(r'[A-Z]\w+',flags=re.I|re.A)
s='''Welcome to
北京
'''
l=regex.findall(s)
print(l)




