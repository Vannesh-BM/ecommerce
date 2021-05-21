import time

import openpyxl
import os
from utilities import PropertyFile, ExcelUtil
import datetime
from win32com import client

excel = client.Dispatch(dispatch="Excel.Application")
wb = excel.Workbooks.Add()

today = datetime.date.today()
d1 = today.strftime("%d-%m-%Y")
t = time.localtime()
ctime = time.strftime("%H:%M:%S", t).replace(":", "_")
path = os.path.join(os.getcwd(), f'excel-report\\Ecommerce_Test_Data-{d1}_{ctime}.xlsx')
wb.SaveAs(path)
excel.Application.Quit()

xl = client.Dispatch("Excel.Application")
# xl.Visible = True  # You can remove this line if you don't want the Excel application to be visible
originalFilePath = os.path.join(os.getcwd(), PropertyFile.getValues('excelFilePath'))
wb1 = xl.Workbooks.Open(Filename=originalFilePath)

wb2 = xl.Workbooks.Open(
    Filename=path)

ws1 = wb1.Worksheets(1)
ws1.Copy(Before=wb2.Worksheets(1))

wb2.Close(SaveChanges=True)
xl.Quit()

row = 7


class TestData:
    BASE_URL = PropertyFile.getValues('url')
    USERNAME = PropertyFile.getValues('username')
    PASSWORD = PropertyFile.getValues('password')

    @staticmethod
    def getCustomerInformationTestData():
        dataList = []
        filePath = path
        testSheet = PropertyFile.getValues('sheet')

        rowCount = ExcelUtil.get_rowcount(filePath, testSheet)
        for i in range(7, rowCount + 1, 6):  # to get rows
            Dict = {}
            Dict['firstname'] = ExcelUtil.read_data(filePath, testSheet, i+1, 4)
            Dict['lastname'] = ExcelUtil.read_data(filePath, testSheet, i + 2, 4)
            Dict['postalcode'] = ExcelUtil.read_data(filePath, testSheet, i + 3, 4)
            print(Dict)

            dataList.append(Dict)
        return dataList

    @staticmethod
    def write_valid_result():
        global row
        expected = ExcelUtil.read_data(path, PropertyFile.getValues('sheet'), row, 5)

        ExcelUtil.write_data(path,
                             PropertyFile.getValues('sheet'), row, 6,
                             "successful")
        if expected == "successful":
            ExcelUtil.write_data(path,
                                 PropertyFile.getValues('sheet'), row, 7,
                                 'Pass')
        else:
            ExcelUtil.write_data(path,
                                 PropertyFile.getValues('sheet'), row, 7,
                                 'Fail')
        row = row + 6

    @staticmethod
    def write_invalid_result():
        global row
        expected = ExcelUtil.read_data(path,PropertyFile.getValues('sheet'), row, 5)

        ExcelUtil.write_data(path,
                             PropertyFile.getValues('sheet'), row, 6,
                             "unsuccessful")
        if expected == "unsuccessful":
            ExcelUtil.write_data(path,
                                 PropertyFile.getValues('sheet'), row, 7,
                                 'Pass')
        else:
            ExcelUtil.write_data(path,
                                 PropertyFile.getValues('sheet'), row, 7,
                                 'Fail')

        row = row + 6
