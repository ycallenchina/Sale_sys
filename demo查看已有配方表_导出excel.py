
import pandas as pd
# import numpy as np
import sys
sys.path.append("..")#为了import引用上一级包
from Tools.sql_db import *

cursor.execute('show tables')#从sql获取所有表名
All=goto_1list(cursor.fetchall())
PF_all=[i for i in All if i[-3:]=='配方表']#在sql里找出所有配方表

with pd.ExcelWriter(r'E:/PythonStudy_Git/调用资料/newforPF.xlsx') as xlsx:#excel写入多sheet的方法
	for PF_sheet in PF_all:
		df=pd.DataFrame(sql整表(PF_sheet))#从sql获取整张表转换为DataFrame
		df.columns=sql表的字段(PF_sheet)#从sql获取表的列名
		df.to_excel(xlsx, sheet_name=f"{PF_sheet}", index=False)
		print(df)

connection.close()