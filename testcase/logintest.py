#coding=utf-8
import unittest
import json
import unittest
import requests
import HtmlTestRunner
from common import md5,get_testcase,Get_Variable,Url,read_csv,parametizedtestcase
import readconfig
class SaveTestCase(parametizedtestcase.ParametrizedTestCase):
    __testcase = list(testcase for testcase in get_testcase.Testcase(r'C:\Users\zhangqin\Desktop','demo.xlsx').read())
    def setUp(self):
        self.__headers = {"Content-Type":"application/json;charset=UTF-8"}
        # user = read_csv.read_csv(r'C:\Users\zhangqin\Desktop','user.csv').read()
        # id = read_csv.read_csv(r'C:\Users\zhangqin\Desktop', '条目id.txt').read()
    def test_login(self):
        testcase = self.__testcase[0]
        data = self.param
        passwd = md5.md5(str(data['password']))
        data['password'] = passwd
        url = Url.url(testcase['path'])
        res = requests.request(testcase['method'], url, data=json.dumps(data), headers=self.__headers)
        text = json.loads(res.text)
        print('当前登录用户为:%s' %(data['username']))
        self.assertEqual(text['message'], testcase['message'], msg='%s登录失败' %(data['username']))
    '''
    def test_getinfo(self,id):
        testcase = next(self.__readcase)
        path = testcase['path'] + id['id']
        url = Url.url(path)
        res = requests.request(testcase['method'], url, headers=self.__headers)
        text = json.loads(res.text)
        key = ["id","infos","name","summary","tags","types","typePaths","infos","imageId","imageUrl","disambiguation","aliases"]
        data1 = Get_Variable.data(res, key)
        self.assertEqual(text['message'], testcase['message'], msg=r'获取词条“%s”信息失败' %(data1['name']))
    def test_getcontent(self):
        testcase = next(self.__readcase)
            id = next(tmp)['id']
            path = testcase['path'] + id
            url = Url.url(path)
            res = requests.request(testcase['method'], url, headers=self.__headers)
            text = json.loads(res.text)
            key = ["content", "supRefs", "supNotes"]
            data2 = Get_Variable.data(res,key)
            self.assertEqual(text['message'], testcase['message'], msg='获取词条正文失败')
    def tearDown(self):
        pass
    '''
if __name__ == '__main__':
    suite = unittest.TestSuite()
    for user in read_csv.read_csv(r'C:\Users\zhangqin\Desktop','user.csv').read():
        suite.addTest(parametizedtestcase.ParametrizedTestCase.parametrize(SaveTestCase, param=user))
    unittest.TextTestRunner(verbosity=2).run(suite)