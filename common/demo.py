import xlrd
import os
class get_Excel():
    def __init__(self,path,name):
        self.__path = os.path.join(path,name)
    def read(self):
        data = xlrd.open_workbook(self.__path)
        #返回所有表名
        name = data.sheet_names()
        #以表名来选择表
        table = data.sheet_by_name(name[0])
        #返回该表中的有效行数
        rows = table.nrows
        #以LIST形式返回对应行的所有数据
        row1 = table.row_values(1)
        type1 = table.row_types(1)
        print(type1)




a = get_Excel(r'C:\Users\zhangqin\Desktop','demo.xlsx')
a.read()