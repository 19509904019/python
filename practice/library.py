'''
图书管理系统
至少五本书
library = [{'bookname':'xxx','author':'xxx','price':100,'number':5},{},{},{},{}]

1.借书  √
2.还书  √
3.查询(书名/作者)  √
4.查看所有  √
5.退出  √

'''
import time
print("---------------欢迎进入图书馆管理系统---------------")
# 书库
library = [{'bookname': '红楼梦', 'author': '曹雪芹', 'price': 88, 'number': 5},
           {'bookname': '三国演义', 'author': '罗贯中', 'price': 98, 'number': 4},
           {'bookname': '水浒传', 'author': '施耐庵', 'price': 108, 'number': 6},
           {'bookname': '西游记', 'author': '吴承恩', 'price': 81, 'number': 5},
           {'bookname': '红高粱', 'author': '莫言', 'price': 68, 'number': 2}]

while True:
    print()
    # 选择操作
    choice = input("1.借书\n2.还书\n3.查询\n4.查看所有\n5.退出\n请选择操作：")
    # 借书
    if choice == '1':
        while True:
            bookname = input("请输入书名：")
            for book in library:
                # 判断是否存在
                if bookname in book.values():
                    # 书本数量
                    numbers = book['number']
                    # 判断是否剩余
                    if numbers != 0:
                        print("借书成功！")
                        # 数量减少
                        numbers -= 1
                        book['number'] = numbers
                        break
                    else:
                        print("此书已经借完！")
                        break
            else:
                print("此书不存在！")
            # 判断是否继续
            answer = input("是否继续借书(q/Q结束):")
            if answer.lower() == 'q':
                print("退出成功！")
                break
    # 还书
    elif choice == '2':
        while True:
            bookname = input("请输入书名:")
            for book in library:
                # 该书数量
                numbers = book['number']
                if bookname in book.values():
                    print("还书成功！")
                    # 数量增加
                    numbers += 1
                    book['number'] = numbers
                    break
            else:
                print("该书不是本图书馆所借！")
            # 判断是否继续
            answer = input("是否继续还书(q/Q结束):")
            if answer.lower() == 'q':
                print("退出成功！")
                break
    # 查询某本书籍
    elif choice == '3':
        while True:
            choice = input("请按照以下方式查询：\n1.作者\n2.书名\n请选择：")
            #按作者查询
            if choice == '1':
                author = input("请输入作者:")
                for book in library:
                    if author in book.values():
                        print(book)
                        break
                else:
                    print("查询不到此作者！") 
            #按书名查询
            elif choice == '2':
                bookname = input("请输入书名:")
                for book in library:
                    if bookname in book.values():
                        print(book)
                        break
                else:
                    print("查询不到此书名！")
            else:
                print("输入错误，请重新输入！")
            # 判断是否继续
            answer = input("是否继续查询(q/Q结束):")
            if answer.lower() == 'q':
                print("退出成功！")
                break      
    # 查询所有书籍
    elif choice == '4':
        if len(library) != 0:
            for book in library:
                print(book)
        else:
            print("图书为空！")
    # 退出系统
    elif choice == '5':
        print("正在退出...")
        time.sleep(1)
        print("退出成功！")
        break
    else:
        print("输入错误，请重新输入！")
