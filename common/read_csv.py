import os
import pandas as pd
class read_csv():
    def __init__(self,filepath,filename,*variable):
        self.filepath = filepath
        self.filename = filename
        self.variable = list(variable for variable in variable)
        self.path = os.path.join(self.filepath, self.filename)
    def read(self):
        if len(self.variable) ==1:
            tmp =list(pd.read_csv(filepath_or_buffer=self.path, sep=',')[self.variable[0]].values)
            return dict(zip(self.variable, tmp))
        else:
            d = []
            for variable in self.variable:
                #每次循环读取对应的列的数据并转化为list类型存储
                tmp = list(pd.read_csv(filepath_or_buffer=self.path, encoding='utf-8', sep=',')[variable].values)
                #将每次读取到的数据放入临时list中
                d.append(tmp)
            #将每一列列名和数据组合成dict返回
            return dict(zip(self.variable,d))
