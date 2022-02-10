import pandas as pd

excelData = pd.read_excel('D:\ebc-python\Practica01-py\sample-xls-file-for-testing.xls')
dataframe = pd.DataFrame(excelData)
print(dataframe)

