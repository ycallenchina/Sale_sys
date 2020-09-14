import pandas as pd
import numpy as np
import sys
sys.path.append("..")#为了import引用上一级包
from Tools.sql_db import *

PF_all=PF_all_GlobalX

def 更新配方表(data='E:/PythonStudy_Git/调用资料/更新配方表.xlsx'):
	df=pd.read_excel(data,sheet_name = None)#读取excel表格
	PF_content=()
	#更新配方表,删旧表
	for PF_df in df:#读取表名i,并创建
		if PF_df in PF_all:
			# cursor.execute(f"DROP TABLE {PF_df}")
			print(f"DROP TABLE {PF_df}")
		excel创建sql表(df,PF_df)
		PF_content+=excel写入sql表(df,PF_df)
	sql更新销售表excel('销售表')

	#材料库更新
	update_content=[]	
	for i in PF_content:
		CL_name=i[0]
		if CL_name not in sql表的材料list('材料库'):
			update_content.append(CL_name)
			# 执行sql('insert','材料库',值=str((CL_name,0)))
			执行sql('insert_set','材料库变动记录表',值=f"材料='{CL_name}',用量=0,时间='{localtime_GlobalX}',操作内容='更新'")
	sql材料库更新excel('进货表')
	sql材料库更新excel('校准表')
	return update_content#返回材料更新内容 
	#,进货,校准,销售3张excel表

print(更新配方表())




connection.close()
