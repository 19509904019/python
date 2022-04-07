# # 猫
#
# class Cat:
#     type = '猫'
#
#     # 通过__init__初始化特征
#     def __init__(self, nickname, age, color):
#         self.nickname = nickname
#         self.age = age
#         self.color = color
#
#     # 动作：方法
#     def eat(self, food):
#         print("{}喜欢吃{}".format(self.nickname, food))
#
#     def catch_mouse(self, color, weight):
#         print("{}抓了一只{}kg的，{}的大老鼠".format(self.nickname, weight, color))
#
#     def sleep(self, hour):
#         if hour < 5:
#             print("继续再多睡会！")
#         else:
#             print("赶快起床抓老鼠！")
#
#     def show(self):
#         print("猫的详细信息：")
#         print(self.nickname, self.age, self.color)
#
#
# # 创建对象
# cat1 = Cat('小花', '2', '灰色')
# # 通过对象调用方法
# cat1.catch_mouse('黑色', 2)
#
# cat1.sleep(8)
#
# cat1.eat('小鱼干')
#
# cat1.show()

"""

编写一个简单的工资管理程序，系统课题管理以下四类人：工人（worker）、销售员（saleman）、经理（manager）、销售经理（salemanger）  √
所有的员工都具有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法 √
1.工人：工人具有工作小时数和时薪的属性，工资计算方法为工作小时数 * 时薪
2.销售员：具有销售额和提成比例的属性，工资计算方法为销售额 * 提成比例
3.经理：具有固定月薪的属性，工资计算方法为固定月薪
4.销售经理：工资计算方法为销售额 * 提成比例 + 固定月薪

请根据以上要求设计合理的类，完成以下功能：
1.添加所有类型的人员
2.计算月薪
3.显示所有人工资情况

"""


# 父类
class Person:
    # 初始化
    def __init__(self, id, name):
        self.id = id
        self.__name = name

    # 设置姓名
    def set_name(self, name):
        self.__name = name

    # 获取姓名
    def get_name(self):
        return self.__name

    # 获取员工号
    def get_id(self):
        return self.id

    def show_salary(self):
        pass


# 工人类
class Worker(Person):
    # 初始化
    def __init__(self, id, name, hours, hour_salary):
        # 继承父类
        super(Worker, self).__init__(id, name)
        self.hours = hours
        self.hour_salary = hour_salary

    # 计算工资
    def calculate_salary(self):
        return self.hours * self.hour_salary


# 销售员类
class Saleman(Person):
    def __init__(self, id, name, saleroom, commission_rate):
        # 继承父类
        super(Saleman, self).__init__(id, name)
        self.saleroom = saleroom
        self.commission_rate = commission_rate

    # 计算工资
    def calculate_salary(self):
        return self.saleroom * self.commission_rate


# 经理类
class Manager(Person):
    def __init__(self, id, name, money):
        # 继承父类
        super(Manager, self).__init__(id, name)
        self.money = money

    # 计算工资
    def calculate_salary(self):
        return self.money


# 销售经理类
class SaleManager:
    def __init__(self, id, name, saleroom,commission_rate,money):
        # 继承父类
        super(SaleManager, self).__init__(id, name)
        self.saleroom = saleroom
        self.commission_rate = commission_rate
        self.money = money

    # 计算工资
    def calculate_salary(self):
        return self.money + self.saleroom * self.commission_rate


worker = Worker('1120211227','worker',200,30)

m = worker.calculate_salary()
print(m)