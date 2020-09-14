import sys
sys.path.append("..")#为了import引用上一级包
from Tools.sql_db import *

def 内嵌销量表(CL_sheet,CL_need):#含有递归算法
	
	CL_list=sql表的材料list(CL_sheet)

	for CL_name in CL_list:

		CL_need_percent=sql材料的用量(CL_sheet,CL_name)/sql表的总用量(CL_sheet)
		
		if CL_name+'配方表' in sheetname_All_GlobalX:
			CL_need=CL_need*CL_need_percent#第二次材料表实际的用量

			CL_name+='配方表'
			sheetname_All_GlobalX.remove(CL_name)#递归反死循环机制,每进入下一级,删除本级元素.防无线递归.
			内嵌销量表(CL_name,CL_need)
		else:
			#用获取的材料名对应的数值相减;算出本次库存剩余数据,并updata到材料库里
			#用第二次材料表实际的总用量 乘以 这次材料所在总用量中的占比,算出实际用量
			sql_fig2=sql材料的用量('材料库',CL_name)
			updata_db=sql_fig2//(CL_need*CL_need_percent)
			updata_db=round(updata_db,2)#保留2位小数
			CL_sheet_MinCount[CL_name]=updata_db

sheetname_All_GlobalX=PF_all_GlobalX
PF_all=PF_all_GlobalX.copy()

# df=pd.read_excel('E:/PythonStudy_Git/调用资料/销量表.xlsx',sheet_name = 0)#读取excel表格,第一张sheet表
for CL_sheet in PF_all:#获取销量表的菜单名,及销量

	CL_list=sql表的材料list(CL_sheet)
	CL_sheet_MinCount={}

	for CL_name in CL_list:#遍历sql表咖喱酱里的材料名
		if CL_name+'配方表' in sheetname_All_GlobalX:
			CL_need=sql材料的用量(CL_sheet,CL_name)#材料用量=单位用量*销量
			
			CL_name+='配方表'
			sheetname_All_GlobalX.remove(CL_name)#递归反死循环机制,每进入下一级,删除本级元素.防无线递归.
			内嵌销量表(CL_name,CL_need)
		else:
			sql_fig1=sql材料的用量(CL_sheet,CL_name)#配方数据
			sql_fig2=sql材料的用量('材料库',CL_name)#库数据
			
			#用获取的材料名对应的数值相减;算出本次库存剩余数据,并updata到材料库里
			updata_db=sql_fig2//sql_fig1
			updata_db=round(updata_db,2)#保留2位小数
			CL_sheet_MinCount[CL_name]=updata_db

	print(f'{CL_sheet}    的最多可出:',min(CL_sheet_MinCount.values()))
	print({i:CL_sheet_MinCount[i] for i in CL_sheet_MinCount if CL_sheet_MinCount[i]==min(CL_sheet_MinCount.values())})
	# print(CL_sheet_MinCount)			
connection.close()