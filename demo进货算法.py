
import pandas as pd
import numpy as np
import sys
sys.path.append("..")#为了import引用上一级包
from Tools.sql_db import *

df=pd.read_excel('E:/PythonStudy_Git/调用资料/进货表.xlsx',sheet_name = 0)#读取excel表格
记录表(df,'进货记录表')

for index,row in df.iterrows():#获取进货表
	CL_name,CL_purchase=row
	stock=sql材料的用量('材料库',CL_name)
  
	# #用获取的材料名对应的数值相加;算出本次库存剩余数据,并updata到材料库里
	updata_db=stock+CL_purchase
	updata_db=round(updata_db,2)#保留2位小数
	# # cursor.execute(f"UPDATE 材料库 SET 用量 = '{updata_db}' WHERE 材料='{CL_name}'")
	print(f"UPDATE 材料库 SET 用量 = '{updata_db}' WHERE 材料='{CL_name}'")

connection.close()