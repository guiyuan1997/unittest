import unittest
import json
import unittest
import requests
import HtmlTestRunner
from common import md5,get_testcase,Get_Variable,Url,read_csv
import readconfig
class SaveTestCase(unittest.TestCase):
    __readcase = get_testcase.Testcase(r'C:\Users\zhangqin\Desktop','demo.xlsx').read()
    def setUp(self):
        self.__headers = {"Content-Type":"application/json;charset=UTF-8"}
    def test_login(self):
        testcase = next(self.__readcase)
        #tmp = read_csv.read_csv(r'C:\Users\zhangqin\Desktop','user.csv','username','password').read()
        data = {'username':'人民艺术家刘波', 'password':'123456789'}
        passwd = md5.md5(data['password'])
        data['password'] = passwd
        url = Url.url(testcase['path'])
        res = requests.request(testcase['method'], url, data=json.dumps(data), headers=self.__headers)
        text = json.loads(res.text)
        self.assertEqual(text['message'], testcase['message'], msg='%s登录失败' %(data['username']))
    def test_getinfo(self):
        testcase = next(self.__readcase)
        #tmp = read_csv.read_csv(r'C:\Users\zhangqin\Desktop', 'id.txt','id').read()
        id = '59241b9855b54278ac006def'
        path = testcase['path'] + id
        url = Url.url(path)
        res = requests.request(testcase['method'], url, headers=self.__headers)
        text = json.loads(res.text)
        key = ["id","infos","name","summary","tags","types","typePaths","infos","imageId","imageUrl","disambiguation","aliases"]
        data1 = Get_Variable.data(res, key)
        self.assertEqual(text['message'], testcase['message'], msg=r'获取词条“%s”信息失败' %(data1['name']))
    def tearDown(self):
        print("Test Is Over")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SaveTestCase('test_login'))
    suite.addTest(SaveTestCase('test_getinfo'))
    unittest.TextTestRunner(verbosity=2).run(suite)