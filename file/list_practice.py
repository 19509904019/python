"""
持久化保存：文件
list  元组  字典 ---->  内存


1.用户注册
2.用户登录
3.图书馆书籍列表

"""
# 默认未登录
islogin = False


# 用户注册
def register():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    repassword = input("请再次确认密码：")
    # 判断密码是否一致
    if password == repassword:
        # 保存账户名和密码
        with open(r'C:\Users\Dell\Desktop\books\users.txt', 'a') as user:
            user.write("{}  {}\n".format(username, password))
        print("账号注册成功！")
    else:
        print("两次密码不一致，请重新输入！")


# 用户登录
def login():
    global islogin
    username = input("用户名：")
    password = input("登录密码：")
    # 保存登录信息
    login_msg = '{}  {}\n'.format(username, password)
    # 读取保存的用户名和密码
    with open(r'C:\Users\Dell\Desktop\books\users.txt', 'rt') as users:
        user_line = users.readlines()
    # 遍历保存的信息
    for msg in user_line:
        # 验证用户名和密码
        if login_msg == msg:
            print("登录成功！")
            islogin = True
            break
    else:
        print("用户名或密码输入错误！")


# 图书馆书籍列表
def show_book():
    # 读取书籍列表
    with open(r'C:\Users\Dell\Desktop\books\books.txt', 'rt', encoding='UTf-8') as book:
        books = book.readlines()
    # 展示所有书籍
    for book in books:
        print(book, end='')


# 增加书籍
def add_book():
    if islogin:
        bookname = input("请输入书名：")
        bookname = f'{bookname}\n'
        with open(r'C:\Users\Dell\Desktop\books\books.txt', 'rt', encoding='UTF-8') as booknames:
            bookname_lines = booknames.readlines()
            for book_name in bookname_lines:
                if book_name == bookname or bookname.isspace():
                    print("书名已存在或不能为空！")
                    break
            else:
                with open(r'C:\Users\Dell\Desktop\books\books.txt', 'a', encoding='UTF-8') as newbookname:
                    newbookname.write(f'{bookname}')
                    print("添加成功！")

    else:
        print("请先登录账号！")
        login()


while True:
    add_book()
    answer = input("按q/Q退出：")
    if answer.lower() == 'q':
        break
