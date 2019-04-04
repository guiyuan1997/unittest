#encoding=UTF-8
import xlrd
import os
class Testcase():
    def __init__(self,path,name):
        self.__path = os.path.join(path,name)
    def read(self):
        #打开测试用例存放的文件
        book = xlrd.open_workbook(self.__path)
        #打开测试用例表
        testcase = book.sheet_by_index(0)
        variable = testcase.row_values(0)
        for i in range(1,testcase.nrows):
            data = testcase.row_values(i)
            yield dict(zip(variable,data))