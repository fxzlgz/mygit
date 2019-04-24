import re
import sys


port=sys.argv[1]

f=open('1.txt')

while True:
    data=''
    for line in f:
        #如果不是空行
        if line !='\n':
            data+=line
        else:
            break
    if not data:
        print("No found")
        break
    #匹配首单词是否为port
    try:
        PORT=re.match(r'\S+',data).group()
    except Exception:
        continue

    if port==PORT:
        #pattern=r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}\.'
        pattern=r'([0-9]{1,3}\.){3}[0-9]{1,3}/\d+|Unknow'
        address=re.search(pattern,data).group()
        print(address)
        break
f.close()


