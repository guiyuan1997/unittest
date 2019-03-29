from common import read_csv
filepath = r"C:\Users\zhangqin\Desktop"
filename = "testuser.csv"
variable = ["username", "passwd", "mobile"]
r = read_csv.read_csv(filepath,filename,*variable)
print(r.path)
print(r.read())
