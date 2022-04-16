#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HanaIKADA
# 
# 这是主flask文件
# 
########################################
from flask import Flask,render_template,request
import m_start_kensaku
#实例化一个Flask应用
app = Flask(__name__)
#相关全局变量
email = "" 
m_receive = []
m_name_link = {}
curr = 0
 #这样写视图函数，会将'/'这条URL规则和视图函数index()联系起来，
 #并且会形成一个Rule实例，再添加进Map实例中去。当访问'/'时，会执行index()
@app.route('/Evian')
def index():
    return render_template('Evian.html')

@app.route('/FlaskTutorial',methods = ['POST'])
def result():
	if request.method == 'POST':
		global curr
		curr = 0
		email = request.form['email']
		m_receive = m_start_kensaku.m_run(email)
		m_name_link = m_start_kensaku.m_run_name_link()
		return render_template('result_details2.html',
			email0 = m_receive[0], email00 = m_name_link[m_receive[0]],
			email1 = m_receive[1], email01 = m_name_link[m_receive[1]],
			email2 = m_receive[2], email02 = m_name_link[m_receive[2]],
			email3 = m_receive[3], email03 = m_name_link[m_receive[3]],
			email4 = m_receive[4], email04 = m_name_link[m_receive[4]],
			email5 = m_receive[5], email05 = m_name_link[m_receive[5]],
			email6 = m_receive[6], email06 = m_name_link[m_receive[6]],
			email7 = m_receive[7], email07 = m_name_link[m_receive[7]],
			email8 = m_receive[8], email08 = m_name_link[m_receive[8]],
			email9 = m_receive[9], email09 = m_name_link[m_receive[9]])
	else:
		pass

#下一页的方法。<a>里的href是get方法
@app.route('/FlaskTutorial2',methods = ['GET'])
def result2():
	if request.method == 'GET':
		# k = request['id']
		# print(k)
		global curr #要修改值时需要这样做
		curr = curr + 10
		if curr > 90: #最后一页自循环
			curr = curr - 10
		m_receive = m_start_kensaku.m_run(email)
		m_name_link = m_start_kensaku.m_run_name_link()
		return render_template('result_details2.html',
			email0 = m_receive[curr + 0], email00 = m_name_link[m_receive[curr + 0]],
			email1 = m_receive[curr + 1], email01 = m_name_link[m_receive[curr + 1]],
			email2 = m_receive[curr + 2], email02 = m_name_link[m_receive[curr + 2]],
			email3 = m_receive[curr + 3], email03 = m_name_link[m_receive[curr + 3]],
			email4 = m_receive[curr + 4], email04 = m_name_link[m_receive[curr + 4]],
			email5 = m_receive[curr + 5], email05 = m_name_link[m_receive[curr + 5]],
			email6 = m_receive[curr + 6], email06 = m_name_link[m_receive[curr + 6]],
			email7 = m_receive[curr + 7], email07 = m_name_link[m_receive[curr + 7]],
			email8 = m_receive[curr + 8], email08 = m_name_link[m_receive[curr + 8]],
			email9 = m_receive[curr + 9], email09 = m_name_link[m_receive[curr + 9]])
	else:
		pass

#上一页的方法。<a>里的href是get方法
@app.route('/FlaskTutorial3',methods = ['GET'])
def result3():
	if request.method == 'GET':
		# k = request['id']
		# print(k)
		global curr #要修改值时需要这样做
		curr = curr - 10
		if curr < 0: #最后一页自循环
			curr = curr + 10
		m_receive = m_start_kensaku.m_run(email)
		m_name_link = m_start_kensaku.m_run_name_link()
		return render_template('result_details2.html',
			email0 = m_receive[curr + 0], email00 = m_name_link[m_receive[curr + 0]],
			email1 = m_receive[curr + 1], email01 = m_name_link[m_receive[curr + 1]],
			email2 = m_receive[curr + 2], email02 = m_name_link[m_receive[curr + 2]],
			email3 = m_receive[curr + 3], email03 = m_name_link[m_receive[curr + 3]],
			email4 = m_receive[curr + 4], email04 = m_name_link[m_receive[curr + 4]],
			email5 = m_receive[curr + 5], email05 = m_name_link[m_receive[curr + 5]],
			email6 = m_receive[curr + 6], email06 = m_name_link[m_receive[curr + 6]],
			email7 = m_receive[curr + 7], email07 = m_name_link[m_receive[curr + 7]],
			email8 = m_receive[curr + 8], email08 = m_name_link[m_receive[curr + 8]],
			email9 = m_receive[curr + 9], email09 = m_name_link[m_receive[curr + 9]])
	else:
		pass
if __name__ == '__main__':
    app.run()