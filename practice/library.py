'''
图书管理系统
至少五本书
library = [{'bookname':'xxx','author':'xxx','price':100,'number':5},{},{},{},{}]

1.借书
2.还书
3.查询(书名/作者)
4.查看所有
5.退出

'''
print("---------------欢迎进入图书馆管理系统---------------")
# 书库
library = [{'bookname': '红楼梦', 'author': '曹雪芹', 'price': 88, 'number': 5},
           {'bookname': '三国演义', 'author': '罗贯中', 'price': 98, 'number': 4},
           {'bookname': '水浒传', 'author': '施耐庵', 'price': 108, 'number': 6},
           {'bookname': '西游记', 'author': '吴承恩', 'price': 81, 'number': 5},
           {'bookname': '蛙', 'author': '莫言', 'price': 68, 'number': 2}]

choice = input("1.借书\n2.还书\n3.查询\n4.查看所有\n5.退出\n请选择操作：")

if choice == 1:
    bookname = input("请输入书名：")
    for book in library:
        #判断是否有该书
        if bookname in book.values():
            print("借书成功！")
            break
        else:
            print("此书不存在！")
elif choice == 2:
    pass
elif choice == 3:
    pass
elif choice == 4:
    pass
elif choice == 5:
    pass
else:
    print("输入错误，请重新输入！！")
