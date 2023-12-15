import pymysql
import os
import matplotlib.pyplot as plt  
plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['axes.unicode_minus'] = False#绘图模块字体调整
from tkinter import *
import tkinter as tk  
from tkinter import messagebox
from functools import partial  
hostx='localhost';
userx='root'; 
passwordx='648475';
dbx='medical_database'; 
  

  
def searcher(databasename):  #查询,name为数据库的名字
    # 创建数据库连接  
    connection = pymysql.connect(  
        host=hostx, 
        user=userx, 
        password=passwordx, 
        db=dbx,  
        cursorclass=pymysql.cursors.DictCursor  # 返回字典类型  
    )  
  
    try:  
        with connection.cursor() as cursor:  
            # 执行SQL查询  
            sql = "SELECT * FROM "+databasename
            cursor.execute(sql)  
  
            # 获取所有记录列表  
            result = cursor.fetchall()  
    finally:  
        connection.close()  # 关闭数据库连接  
  
    return result  # 返回数据库中的内容  
  

  
def add(databasename,adder):  
    # 连接MySQL数据库  
    connection = pymysql.connect(  
        host=hostx, 
        user=userx, 
        password=passwordx, 
        db=dbx,   
    )  
    if databasename=="doctor":#可以使用else if来调整添加的目标数据库
        head=" (name,department,title,job_number) "
        tail="(%s,%s,%s,%s)"
    try:  
        with connection.cursor() as cursor:  
            # 创建插入数据的SQL语句  
            sql = "INSERT INTO "+databasename+head+" VALUES "+tail
              
            # 执行SQL语句并传入参数  
            cursor.execute(sql, adder)  
              
            # 提交事务  
            connection.commit()  
    except Exception as e:  
        print(f"Error: {e}")  
    finally:  
        # 关闭数据库连接  
        connection.close()  


def deleter(databasename,job_number):  
    # 建立数据库连接  
    connection = pymysql.connect(host=hostx, 
                                user=userx, 
                                password=passwordx, 
                                db=dbx,  
                                 port=3306)
    if databasename=="doctor":#可以通过else if语句添加对于其他数据的操作，但要注意主键的更改
        keyer="job_number"  
    try:  
        with connection.cursor() as cursor:  
            # 定义要执行的SQL语句  
            sql = "DELETE FROM " +databasename+" WHERE "+keyer+"=%s"
            # 执行SQL语句  
            cursor.execute(sql, (job_number,))  
            # 提交事务  
            connection.commit()  

    except pymysql.MySQLError as error:  
        print(f"An error occurred while deleting the doctor: {error}")  
        # 如果发生错误，回滚事务  
        connection.rollback()  
    finally:  
        # 关闭数据库连接  
        connection.close()
  

  
def line_search(databasename,key):
    if databasename=="patient":#同上
        keyer="patient_id"
    try:  
        # 创建游标对象  
        cursor = connection.cursor()  
          
        # 构建 SQL 查询语句
        sql = "SELECT * FROM "+databasename+" WHERE "+keyer+" = %s"   
          
        # 执行 SQL 查询  
        cursor.execute(sql, (key,))  
          
        # 获取查询结果  
        result = cursor.fetchone()  
          
        # 关闭游标和连接  
        cursor.close()  
        connection.close()  
          
        # 返回查询结果  
        return result  
    except Exception as e:  
        print(f"An error occurred: {e}")  
        return 0  


 

def collect_doctor_photo(doctor_id,save_name): #因为只有医生有照片，所以只针对医生表进行查询,
                                               #save_name为想把照片保存的文件名，
                                               #为了避免在不同电脑上操作带来的复杂性，
                                               #这里暂时选择相对路径，存放在py文件目录下
    # 连接到数据库  
    connection = pymysql.connect(  
        host=hostx, 
        user=userx, 
        password=passwordx, 
        db=dbx,    
        charset='utf8mb4',  
        cursorclass=pymysql.cursors.DictCursor  
    )  
  
    try:  
        with connection.cursor() as cursor:  
            # 查询job_number为1000的doctor的photo  
            sql = "SELECT photo FROM doctor WHERE job_number="+str(doctor_id) 
            cursor.execute(sql)  
            result = cursor.fetchone()  
              
            if result:  
                # 如果查询到了结果，保存photo为JPEG文件  
                photo = result['photo']  
                with open(os.path.join(os.path.dirname(__file__), save_name), 'wb') as f:  
                    f.write(photo)  
                print("Doctor photo saved successfully!")  
            else:  
                print("No photo found for job_number 1000.")  
    finally:  
        connection.close()  
  

def nested_query():  #查找大于平均年龄的病人现实意义有限，此处仅用于体现嵌套查询功能
    connection = pymysql.connect(host=hostx, 
        user=userx, 
        password=passwordx, 
        db=dbx,  )  
      
    try:  
        with connection.cursor() as cursor:  
            # 计算平均年龄  
            cursor.execute("SELECT AVG(age) FROM patient")  
            average_age = cursor.fetchone()[0]  
              
            # 查询年龄大于或等于平均年龄的患者的ID  
            query = "SELECT patient_id FROM patient WHERE age >= %s"  
            cursor.execute(query, (average_age,))  
            patient_ids = cursor.fetchall()  
              
            # 返回结果  
            return [id[0] for id in patient_ids]  
    finally:  
        connection.close()  
  
def collect_video(patient_id,save_name):
                                              
    # 连接到数据库  
    connection = pymysql.connect(  
        host=hostx, 
        user=userx, 
        password=passwordx, 
        db=dbx,    
        charset='utf8mb4',  
        cursorclass=pymysql.cursors.DictCursor  
    )  
  
    try:  
        with connection.cursor() as cursor:  
            # 查询job_number为1000的doctor的photo  
            sql = "SELECT ct_video FROM ct WHERE patient_id="+str(patient_id) 
            cursor.execute(sql)  
            result = cursor.fetchone()  
              
            if result:     
                with open(os.path.join(os.path.dirname(__file__), save_name), 'wb') as f:  
                    f.write(result)  
                print("saved success")  
            else:  
                print("fail")  
    finally:  
        connection.close() 
  
def get_all_medicine_remainings(): #获取各种药的剩余量（中间函数） 
    # 创建数据库连接  
    connection = pymysql.connect(host=hostx, 
        user=userx, 
        password=passwordx, 
        db=dbx,  )  
  
    try:  
        with connection.cursor() as cursor:  
            # 执行SQL查询  
            sql = "SELECT remaining_quantity FROM medicine"  
            cursor.execute(sql)  
              
            # 获取所有查询结果  
            result = cursor.fetchall()  
              
            # 将结果转换为数组形式  
            remaining_quantity = [quantity[0] for quantity in result]  
            return remaining_quantity 
    finally:  
        connection.close()  


 
def draw_pie_chart(data):  
  
    # 数据列表  
    labels = ["medicine_A", "medicine_B", "medicine_C", "medicine_D","medicine_E"]  
    sizes = [data[0],data[1], data[2], data[3],data[4]]   
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','silver']  
  
    # 绘制饼图  
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)  
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.  
    plt.title("药房中剩余药品饼图")  
  
    plt.show()  


  
def group_patients_by_doctor():  #将病人按照组主治医生进行分组
    # 创建游标对象
    connection = pymysql.connect(  
        host=hostx, 
        user=userx, 
        password=passwordx, 
        db=dbx,  )  
    try:  
        with connection.cursor() as cursor:  
            # 创建查询语句  
            sql = "SELECT job_number, patient_id FROM medical_record"  
              
            # 执行查询  
            cursor.execute(sql)  
              
            # 获取查询结果  
            data = cursor.fetchall()
            result = {}  
              
            for item in data:  
                key = item[0]  
                value = item[1]  
                if key in result:  
                    result[key].append(value)  
                else:  
                    result[key] = [value]  
              
            for key, values in result.items():  
                print('工号'+key+'的医生' + '：' +'治疗的病人id为'+ ', '.join(values))
    finally:  
        connection.close()
  
def count_medicine_D():
    connection = pymysql.connect(  
        host=hostx, 
        user=userx, 
        password=passwordx, 
        db=dbx,  )  
    try:  
            with connection.cursor() as cursor:  
                # 创建SQL查询语句  
                sql = "SELECT COUNT(*) FROM prescription WHERE medicine_id = '14'"  
                cursor.execute(sql)  
                result = cursor.fetchone()
                results=str(result[0])+'个人正在使用medicine_D'
                return results  
    finally:  
        connection.close()
        
vistornamey="123456"
visitorpasswordy="123456" 
  
def login():  
    # 创建主窗口  
    root = tk.Tk()  
    root.title("Login")  
      
    # 创建标签  
    welcome_label = tk.Label(root, text="Welcome!")  
    welcome_label.pack()  
      
    # 创建用户名和密码输入框  
    username_label = tk.Label(root, text="用户名")  
    username_label.pack()  
    username_var = tk.StringVar()  
    username_entry = tk.Entry(root, textvariable=username_var)  
    username_entry.pack()  
      
    password_label = tk.Label(root, text="密码")  
    password_label.pack()  
    password_var = tk.StringVar()  
    password_entry = tk.Entry(root, textvariable=password_var, show="*")  
    password_entry.pack()  
      
    # 创建登录按钮  
    login_button = tk.Button(root, text="登录", command=lambda: check_login(username_var, password_var,root))  
    login_button.pack()  
      
    # 运行主循环  
    root.mainloop()
    return 1
  
def check_login(username, password,root):  
    if username.get() == "123456" and password.get() == "123456":  
        messagebox.showinfo("Success", "登录成功！")
        root.destroy()
        return 1, True  
    else:  
        messagebox.showerror("Error", "用户名或密码错误！")  
        return 0, False


def create_ui():  
    root = tk.Tk()  
    root.title("请选择功能")       
    tk.Button(root, text="所有病人信息检索", command=lambda: print(print(searcher("patient")))).pack()  
    tk.Button(root, text="添加某个医生", command=lambda: print(add("doctor",("测试名","测试科室","测试职称",66666)))).pack()
    tk.Button(root, text="删除某个医生", command=lambda: print(deleter("doctor",66666))).pack()  
    tk.Button(root, text="单个病人信息检索", command=lambda: print(print(line_search("patient",1)))).pack()
    tk.Button(root, text="查询并下载某个医生的照片", command=lambda: print(collect_doctor_photo(1002,"doctorphoto.jpg"))).pack()  
    tk.Button(root, text="查询大于平均年龄的病人的id", command=lambda: print(print(nested_query()))).pack()
    tk.Button(root, text="画出病人的配药花费分布饼图", command=lambda: draw_pie_chart(get_all_medicine_remainings())).pack()  
    tk.Button(root, text="将病人按照主治医生进行分类", command=lambda: print(group_patients_by_doctor())).pack()  
    tk.Button(root, text="计算使用某个药品(medicine_D)的病人数量", command=lambda: print(count_medicine_D() ) ).pack()  
    root.mainloop()  
    





  
# 使用示例  

        
#print(searcher("doctor"))
#add("doctor",("测试名","测试科室","测试职称",66666))
#deleter("doctor",66666)
#print(line_search("doctor",1000))
#getFile()
#collect_doctor_photo(1002,"doctorphoto.jpg")
#print(nested_query())
#print(get_all_medicine_remainings() ) 
#draw_pie_chart(get_all_medicine_remainings())
#group_patients_by_doctor()
#print(count_medicine_D() )  
x=login()
if __name__ == "__main__":  
   create_ui()
  



























  

