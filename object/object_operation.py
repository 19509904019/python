"""
面向对象：
程序         现实中
对象 ---->  具体的食物

现实中事物  -----> 转成电脑程序
世间万物皆对象

好处：
1.复用
2.灵活

面向对象：
    类
    对象
    属性
    方法

对象：
    A的手机
    B的手机
    C的手机
    D的手机
    ...

    对象的集合  ----->  共同特征：品牌  颜色  大小  价格     动作：打电话  发短信  上网  玩游戏
    类别：手机类
        学生类
    特征：姓名  年龄  性别  身高  血型  ....   -----> 属性
    动作：刷微博  刷抖音  发动态  ....   ---->方法

    多个对象  --->  提取对象的共同特征和动作  ---->  封装到一个类中

定义：
    class 类名(父类):
        属性：特征
        方法：动作

"""
# # 所有的类名要求首字母大写，多个单词使用驼峰式命名
# # ValueError  TypeError  StopIterable
# # 默认继承object
# class Phone:
#     # 属性
#     brand = 'HUAWEI'
#     # 方法
#     pass
#
#
# # 使用类创建对象
# ayan = Phone()
# print(ayan.brand)
# 改变属性
# ayan.brand = 'iPhone'
# print(ayan.brand)

# yjun = Phone()
# print(yjun.brand)

"""
定义类和属性
"""


# 定义类
class Student:
    # 类属性
    name = 'ayan'
    age = 18


# 使用类
yanyan = Student()
# yanyan.age = 3  # 对象属性
# 先找自己空间的，然后再去模型中去找，如果自己空间中存在age属性，则不会去模型中去找
print(yanyan.age)
# 更改类属性
Student.age = 20
print(yanyan.age)
# 新的对象也是改过后的类属性
yujun = Student()
print(yujun.age)
