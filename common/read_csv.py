import os
import pandas as pd
class read_csv():
    def __init__(self,filepath,filename,):
        self.filepath = filepath
        self.filename = filename
        self.path = os.path.join(self.filepath, self.filename)
    def read(self):
        read = pd.read_csv(filepath_or_buffer=self.path,sep=',')
        key = list(read.keys())
        for value in read.values:
            data = dict(zip(key,value))
            yield data