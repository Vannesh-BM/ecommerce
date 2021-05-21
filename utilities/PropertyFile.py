from jproperties import Properties

conf = Properties()

with open('conf.properties', 'rb') as read_prop:
    conf.load(read_prop)


def getValues(key):
    if key == 'excelFilePath':
        value = conf.get('excelFilePath').data
    elif key == 'sheet':
        value = conf.get('sheetName').data
    elif key == 'url':
        value = conf.get('url').data
    elif key == 'username':
        value = conf.get('username').data
    elif key == 'password':
        value = conf.get('password').data
    return value