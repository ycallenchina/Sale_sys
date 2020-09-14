import pandas as pd
import numpy as np
import sys
sys.path.append("..")#为了import引用上一级包
from Tools.sql_db import *

PF_all=PF_all_GlobalX
def 更新配方表(data='E:/PythonStudy_Git/调用资料/更新配方表.xlsx',sheet_name = None):
	df=pd.read_excel(data,sheet_name = None)#读取excel表格
	PF_content=()
	for PF_df in df:#读取表名i,并创建
		if PF_df in PF_all:
			# cursor.execute(f"DROP TABLE {PF_df}")
			print(f"DROP TABLE {PF_df}")
		excel创建sql表(df,PF_df)
		PF_content+=excel写入sql表(df,PF_df)

	update_content=[]	
	for i in PF_content:
		CL_name=i[0]
		if CL_name not in sql表的材料list('材料库'):
			update_content.append(CL_name)
			print(f"INSERT INTO {'材料库'} VALUES "+str((CL_name,0)))	
	print(update_content)
	sql材料库更新excel('进货表')
	sql材料库更新excel('校准表')


更新配方表()

