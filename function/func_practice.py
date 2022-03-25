# '''
# 定义一个login函数：
# admin 1234
# 输入用户名和密码，验证是否正确
# '''
# def login():
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == 'admin' and password == '1234':
#         print("登录成功！")
#     else:
#         print("输入错误，请重新输入！")
# login()


# # 带参数，n表示允许输入错误的次数
# def login(n):
#     # 登录次数
#     count = 0
#     while True:
#         username = input("请输入用户名:")
#         password = input("请输入密码:")
#         # 登录条件
#         if username == 'admin' and password == '1234':
#             print("登录成功！")
#             break
#         else:
#             print(f"登录失败,失败{n}次会锁定！")
#             count += 1
#         # 错误次数
#         if count == n:
#             print(f"输入{n}次，已锁定！")
#             break
# # 调用函数
# login(3)


# # 求1-n的累加和
# def get_sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     print(sum)
# get_sum(100)


'''
(多个参数)
定义一个出租车打车程序，参数：手机号码，起步价：10元
函数体中输入乘车时间和里程数，2公里内起步价,超出2公里每公里5元
乘车时间每分钟0.5元
下车打印总账单
'''


# def take_taxi(phonenumbers, price):
#     time = float(input("请输入乘车时长(单位：分钟)："))
#     mileage = float(input("请输入里程数："))
#     if mileage > 2:
#         total = price + (mileage-2) * 5 + time * 0.5
#     else:
#         total = price + time * 0.5
#     #打印总账单
#     print(f"手机号为{phonenumbers}的乘客花费为{total}")

# take_taxi(13811114444,10)


''''
验证是否登录：islogin
    自定义一个判断用户是否登录功能islogin
    参数：username，password
    函数体：
    判断用户输入的用户名和密码是否正确，如果正确则返回True，否则返回False

借书：borrow_book
参数是：书名
函数体：
判断是否登录，如果登录则可以借书
如果没有登录则提示：还未登不能借书
'''
# #默认未登录
# islogin = False
# #验证是否登录
# def login(username,password):
#     global islogin
#     #用户名和密码
#     is_name = 'admin'
#     is_password = '1234'
#     if username == is_name and password == is_password:
#         print("登录成功！")
#         islogin = True
#     else:
#         print("登录失败！")
#         islogin = False

# #借书
# def borrow_book(bookname):
#     #已登录
#     if islogin:
#         print("已登录，可以借书！")
#         print(f"{bookname}借出成功！")
#     #未登录
#     else:
#         print("未登录，不能借书！")
#         username = input("请输入用户名：")
#         password = input("请输入密码：")
#         login(username,password)


# borrow_book('红楼梦')
# borrow_book('红楼梦')

'''
停车计费系统：
进入停车场记录进入时间，如果出去则记录出去时间，停车时间是：出去-进入时间
停车场的数据结构是：
[{'车牌':[进入时间，0]},{'车牌':[进入时间，出去时间]},...]
15分钟1块
1小时4块
停车场变量 ----> 全局变量

def enter():
    #键盘输入车牌
    pass

def leave():
    #键盘输入车牌
    pass
'''
import time
#记录车辆信息
car_park = []

# 进入停车场
def enter():
    '''
    Descripttion: 进入停车场
    :param: None
    :return: 
    '''
    #扫描车牌号
    plate_numbers = input("请输入车牌号：")
    print(f"欢迎{plate_numbers}进入南财停车场！")
    #构建结构{'车牌'：[进入时间，驶出时间]}
    car = {}
    #开始计时
    start = time.time()
    car[plate_numbers] = [start]
    #进入停车场
    car_park.append(car)
 
# 驶离停车场
def leave():
    #扫描车牌号
    plate_numbers = input("请输入车牌号：")
    #判断汽车是否进场
    for car in car_park:
        if plate_numbers in car.keys():
            #结束时间
            end = time.time()
            time_record = car.get(plate_numbers)
            time_record.append(end)
            #停车时长
            differential = time_record[1] - time_record[0]
            #计算花费
            total = differential * 4
            print("车牌为%s停车%.2f小时，应缴费%.2f元" % (plate_numbers,differential,total))
            break
    else:
        print("此车未进场！")


#主函数
def main():
    #进入停车场
    enter()
    #驶出停车场
    leave()


if __name__ == '__main__':
    main()