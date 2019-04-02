import pandas as pd
import os
import re
class Testcase():
    variable = ['path','method','data','cookie','code','messge']
    def __init__(self,path,name):
        self.path = os.path.join(path, name)
    #将读取的data数据转化为list类型
    def list_data(self,data):
        b=re.split(',',data)
        c = list(d.strip('[]') for d in b)
        return c
    def read(self):
        dict = pd.read_csv(filepath_or_buffer=self.path,sep=';')
        for variable in self.variable:
            tmp = list(dict[variable].values)
            if variable == 'data':
                tmp_list = []
                for data1 in tmp:
                    tmp_list.append(Testcase.list_data(self,data1))
                tmp = tmp_list
            #设置动态变量
            name = locals()
            name['%s' % variable] = tmp
        for i in range(len(name.get('path'))):
           list1 = []
           for j in self.variable:
               list1.append(name.get(j)[i])
           yield list1