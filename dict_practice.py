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


#借了两本书
books = [
{'书名':'三体','价格':84,'作者':'刘慈欣','出版社':'新华出版社'},
{'书名':'盗墓笔记','价格':100,'作者':'南派三叔','出版社':'长江出版社'}
]
print(books)

#删除  出版社
for book in books:
    print(book)
    book.pop('出版社')
print(books)