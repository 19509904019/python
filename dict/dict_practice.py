'''
练习：
book = {}
书名，价格，作者，出版社
促销：价格打八折
打印最终字典中的内容
'''
# book = {}
# bookname = input("请输入书名：")
# book['bookname'] = bookname
# bookprice = input("请输入价格：")
# book['bookprice'] = bookprice
# bookwriter = input("请输入作者：")
# book['bookwriter'] = bookwriter
# bookpress = input("请输入出版社：")
# book['bookpress'] = bookpress
# print(book)
# #打折
# book['bookprice'] *= 0.8
# print(book)


# #借了两本书
# books = [
# {'书名':'三体','价格':84,'作者':'刘慈欣','出版社':'新华出版社'},
# {'书名':'盗墓笔记','价格':100,'作者':'南派三叔','出版社':'长江出版社'}
# ]
# print(books)

# 删除  出版社
# for book in books:
#     print(book)
#     book.pop('出版社')
# print(books)


'''
books = []  能放多本书
书：{}
书名  作者  价格

添加三本书：
1.添加书
  不能添加同名书籍
'''
# 111111
# #存放书籍信息
# books = []

# while True:
#     bookname = input("请输入书名：")
#     for book in books:
#         #判断是否已存在
#         if bookname in book.values():
#             print("书籍已存在，请重新输入！")
#             break
#     else:
#         bookwrite = input("请输入作者：")
#         bookprcice = input("请输入价格：")
#         books.append({'bookname':bookname,'bookwrite':bookwrite,'bookprcice':bookprcice})
#     #最多添加三本书
#     if len(books) == 3:
#         print(books)
#         break


# 2222
# 存放书籍
books = []

while True:
    msg = input("请依次输入书籍名称，作者，价格（以空格分隔）：").split(" ")  # 列表
    for book in books:
        # 判断书籍是否已经存在
        if msg[0] in book.get('bookname'):
            print("书籍已存在，请重新输入！")
            break
    else:
        books.append(
            {'bookname': msg[0], 'bookwrite': msg[1], 'bookprice': msg[2]})
    # 存放三本书
    if len(books) == 3:
        print(books)
        break
