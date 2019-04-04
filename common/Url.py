#encoding=UTF-8
import readconfig
def url(path):
    tmp = readconfig.read_config().get_http()
    url = '%s:%s' %(tmp['host'], tmp['port']) + path
    return url