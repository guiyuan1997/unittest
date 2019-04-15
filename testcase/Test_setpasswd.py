#coding=utf-8
import requests
import unittest
import json
from common import get_testcase, Url, md5
class TestSetpasswd(unittest.TestCase):
    __headers = {"Content-Type": "application/json;charset=UTF-8", "Cookie":"bearer=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiLkurrmsJHoibrmnK_lrrbliJjms6IiLCJjcmVhdGVkIjoxNTU0Nzk5MjgwMjMzLCJleHAiOjE1NTU0MDQwODAsInVzZXJpZCI6MTUwNn0.j9R2h3y2vQli_2kL0jBqyhxbf_p-A3Z9_dHR0ti4Igol0WxCKO6HXi8AVQC3ZmWW8NbsFuMnXqXz9_dv71yyxg"}
    def Setup(self):
        print('请输入你要修改的账号绑定的手机号和新密码')
    def test_Setpasswd(self):
        path = r'/api/auth/w1/y/modifyPassword'
        phone = input('请输入该账号绑定的手机号:')
        data = {"language":"cn","password":"25d55ad283aa400af464c76d713c07ad","nationCode":"86","phone":str(phone)}
        url = Url.url(path)
        res = requests.request('POST', url, data=json.dumps(data), headers=self.__headers)
        text = json.loads(res.text)
        print(text)
        message = '成功'
        print(url)
        self.assertEqual(text['message'], message, msg='修改失败')

if __name__ == '__main__':
    unittest.main()
