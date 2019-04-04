#encoding=UTF-8
import json
import re
def data(res , list):
    tmp = []
    text = json.loads(res.text)
    data1 = text['data']
    for key in list:
        value = data1[key]
        tmp.append(value)
    return dict(zip(list,tmp))

def cookie(res):
    bearer = re.match(r'bearer=(.*?); Max-Age', res.headers['Set-Cookie']).group(1)
    Cookie = {'Cookie':'bearer=%s' %(bearer)}
    return Cookie