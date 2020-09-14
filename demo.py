
import pandas as pd
import numpy as np
import sys
import  pymysql
import  pymysql.cursors

#链接sql
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
cursor = connection.cursor()

def 读取菜名创建sql配方表并写入内容(data='E:/PythonStudy_Git/调用资料/配方表.xlsx'):
	#读取excel内容,并用sheet名创建表名,第一行名创建keys,最后插入内容

	df=pd.read_excel(data,sheet_name = None)#读取excel表格
	#创建表
	for i in df:#读取表名i,并创建
		PF_name=i+'配方表'
		Csql_columns=''
		for c in df[i].columns:#读取列名,并创建
			Csql_columns+=c+' varchar(255),'
		sql = f"CREATE TABLE {PF_name}({Csql_columns[:-1]})ENGINE=MyISAM DEFAULT CHARSET=utf8;"	
		# print(sql)
		cursor.execute(sql)#执行sql
		
		#内容插入
		for index,row in df[i].iterrows():#读取行row,并插入内容
			sql2=f"INSERT INTO {PF_name} VALUES "+str(tuple(row))
			# print(sql2)
			cursor.execute(sql2)#执行sql

def 创建材料库(data='E:/PythonStudy_Git/调用资料/配方表.xlsx'):

	df=pd.read_excel(data,sheet_name = None)#读取excel表格

	sheetname_All=[]
	#创建表及字段
	Csql_columns=''
	for i in df:
		sheetname_All.append(i)
	for c in df[i].columns:#读取列名,并创建表材料库,和字段.
		Csql_columns+=c+' varchar(255),'
	sql = f"CREATE TABLE 材料库({Csql_columns[:-1]})ENGINE=MyISAM DEFAULT CHARSET=utf8;"	
	# print(sql)
	# print(sheetname_All)
	cursor.execute(sql)

	#插入内容

	noecho=[]#建立无重复的列表
	for i in df:
		for index,row in df[i].iterrows():#读取行row,并插入内容
			if row[0] in noecho+sheetname_All:#如果材料名重复或者是配方表名就pass,不重复就加入noecho列表
				pass
			else:
				noecho.append(row[0])
				sql2=f"INSERT INTO 材料库 VALUES "+str(tuple(row))
				# print(sql2)
				cursor.execute(sql2)#执行sql

def 从sql提取数据创建excel():

	cursor.execute(f'select * from 材料库')
	df = pd.DataFrame(cursor.fetchall())
	# print(df)
	df.to_excel('E:/PythonStudy_Git/调用资料/材料库.xlsx','Sheet1')

def 批量删除sql表():
	data='E:/PythonStudy_Git/调用资料/配方表.xlsx'
	df=pd.read_excel(data,sheet_name = None)
	for i in df:#读取表名i,并执行sql语句
		cursor.execute(f"DROP TABLE {i}")

def 手动建sql表():
	sql_old = f"CREATE TABLE 材料库变动记录表(材料 varchar(255),用量 varchar(255),时间 varchar(255),操作内容 varchar(255),备注 varchar(255) NULL DEFAULT NULL)ENGINE=MyISAM DEFAULT CHARSET=utf8;"	
	sql=f"CREATE TABLE `操作日志记录表` ( `目标名` VARCHAR(255) NOT NULL , `操作内容` VARCHAR(255) NOT NULL , `时间` VARCHAR(255) NOT NULL , `备注` VARCHAR(255) NULL DEFAULT NULL ) ENGINE = MyISAM DEFAULT CHARSET=utf8;"
	cursor.execute(sql_old)


手动建sql表()

connection.close()