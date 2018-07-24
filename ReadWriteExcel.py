import xlrd as read
import xlwt as write
import os
from ReadWriteFile import FileOperations


class ExcelOperations:
    excelpath = 'C:\\Users\Sachin\Desktop\PythonEnvProj\dbex\ExcelInfo.xls'
    listOfLines = []
    readExcelDataList = []

    def readexcel(self):
        workbook = read.open_workbook(ExcelOperations.excelpath)
        userinfosheet = workbook.sheet_by_name("UserInfo")

        for rindex in range(0, userinfosheet.nrows):
            for cindex in range(0, userinfosheet.ncols):
                ExcelOperations.readExcelDataList.append(userinfosheet.cell(rindex, cindex).value)
        print(ExcelOperations.readExcelDataList)
        return ExcelOperations.readExcelDataList

    def writeexcel(self):
        workBook = write.Workbook()
        userInfoSheet = workBook.add_sheet('UserInfo')
        count = 0
        cols = []
        for item in FileOperations.filedata:
            for words in item.split(','):
                cols.append(words)
                #print(words)

        for num in range(FileOperations.filedata.__len__()):
            row = userInfoSheet.row(num)
            for item in range(3):
                row.write(item, cols.__getitem__(count))
                count += 1

        workBook.save(ExcelOperations.excelpath)



if __name__ == '__main__':
    Eob = ExcelOperations()
    FileOperations().readfromfile()
    print('Write excel:')
    Eob.writeexcel()
    print('Read excel:')
    Eob.readexcel()