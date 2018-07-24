class FileOperations:
    filepathR = "C:\\Users\Sachin\Desktop\PythonEnvProj\dbex\data.txt"
    filepathW = "C:\\Users\Sachin\Desktop\PythonEnvProj\dbex\data1.txt"
    filedata = []
    def readfromfile(self):
        f = open(FileOperations.filepathR, 'r')
        FileOperations.filedata = f.readlines()
        print(FileOperations.filedata)
        f.close()
       #return FileOperations.filedata

    def writeDataIntoFile(self,list):
        file = open('C:\\Users\Sachin\Desktop\PythonEnvProj\dbex\data2.txt','w')
        for tpl in list:
            line=''
            for item in tpl:
                line += str(item)+','

            print(line[:-1])
            file.write(line[:-1] +'\n')
        file.close()

if __name__ == '__main__':
    fo = FileOperations()
    fo.readfromfile()
    fo.writetofile()

