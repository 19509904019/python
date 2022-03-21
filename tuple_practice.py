'''
王者荣耀角色管理
角色：姓名   性别   职业

添加角色
删除角色
修改角色
查询角色  单个角色
显示所有角色
退出系统

'''
# print("----------欢迎进入王者荣耀管理系统----------")
# # 存放角色信息
# characters = []

# print("**********添加角色***********")
# # 添加角色
# while True:
#     # 输入信息
#     name = input("输入添加角色姓名：")
#     gender = input("输入添加角色性别:")
#     career = input("请输入添加角色职业:")
#     # 存放角色信息
#     character = (name, gender, career)
#     characters.append(character)
#     print("角色列表信息为:%s" % characters)
#     answer = input("是否继续添加(按q或者Q退出):")
#     if answer.lower() == 'q':
#         print("添加角色退出成功！")
#         break

# print("**********删除角色**********")
# # 删除角色
# while True:
#     # 输入角色名称
#     delete_name = input("请输入想删除角色名称：")
#     # 判断是否有角色
#     if len(characters) != 0:
#         # 遍历角色再删除
#         for character in characters:
#             if delete_name == character[0]:
#                 characters.remove(character)
#             else:
#                 print("删除失败，请重新输入！")
#     else:
#         print("角色列表为空...")
#     print("角色列表信息为:{}".format(characters))
#     answer = input("是否继续删除(按q或者Q退出):")
#     if answer.lower() == 'q':
#         print("删除角色退出成功！")
#         break

# print("**********修改角色**********")
# # 修改角色
# while True:
#     if len(characters)!=0:
#         # 输入修改信息
#         modify_name_before = input("请输入角色名称:")
#         for character in characters:
#             #存放修改信息
#             modify_list = []
#             #修改角色名称
#             if modify_name_before == character[0]:
#                 answer = input("是否修改名称？(按q或Q继续):")
#                 if answer.lower() == 'q':
#                     modify_name_after = input("请输入修改名称：")
#                     modify_list.append(modify_name_after)
#                 else:
#                     modify_list.append(character[0])
#                 #修改性别
#                 answer = input("是否修改性别？(按q或Q继续):")
#                 if answer.lower() == 'q':
#                     modify_gender = input("请输入修改的性别：")
#                     modify_list.append(modify_gender)
#                 else:
#                     modify_list.append(character[1])
#                 #修改职业
#                 answer = input("是否修改职业？(按q或Q继续):")
#                 if answer.lower() == 'q':
#                     modify_career = input("请输入修改的职业：")
#                     modify_list.append(modify_career)
#                 else:
#                     modify_list.append(character[2])
#                 #替换
#                 modify_list = tuple(modify_list)
#                 character = modify_list
#             else:
#                 print("输入错误，请重新输入！")
#     else:
#         print("角色列表为空...")
#     # 更新角色信息
#     print("角色列表信息为:{}".format(characters))
#     answer = input("是否继续修改(按q或Q结束)：")
#     if answer.lower() == 'q':
#         print("修改名称退出成功！")
#         break

# # 查询角色
# while True:
#     select_character = input("输入要查询的角色名称：")
#     for character in characters:
#         if select_character == character[0]:
#             print("{}".format(character))
#         else:
#             print("输入错误！")
#     answer = input("是否继续查询(按q或Q结束)：")
#     if answer.lower() == 'q':
#         print("退出成功！")
#         break

# # 显示所有角色
# for character in characters:
#     print(character)


'''
王者荣耀角色管理
角色：姓名   性别   职业

1.添加角色
2.删除角色
3.修改角色
4.查询角色  单个角色
5.显示所有角色
6.退出系统
'''
import time
print("----------欢迎进入王者荣耀管理系统----------")
# 存放所有角色信息
all_role = []
while True:
    # 选择操作
    choice = input("\n1.添加角色\n2.删除角色\n3.修改角色\n\
4.查询单个角色\n5.查询所有角色\n6.退出系统\n请选择操作：")
    
    # 添加角色
    if choice == '1':
        while True:
            name = input("请输入角色名称：")
            gender = input("请输入角色性别：")
            career = input("请输入角色职业：")
            # 保存角色信息
            role = [name, gender, career]
            all_role.append(role)
            print("角色{}添加成功！".format(name))
            answer = input("是否继续添加(按q或者Q结束)：")
            if answer.lower() == 'q':
                print("退出成功！")
                break

    # 删除角色
    elif choice == '2':
        while True:
            #判断角色是否为空
            if len(all_role)!=0:
                delete_name = input("请输入删除角色名称：")
                for role in all_role:
                    if delete_name in role:
                        answer = input("确定删除角色吗(y/n):")
                        if answer.lower() == 'y':
                            #删除角色
                            all_role.remove(role)
                            print("角色{}删除成功！".format(delete_name))
                            break
                        elif answer.lower() == 'n':
                            print("取消成功！")
                            break
                        else:
                            print("输入错误，请重新输入！")
                else:
                    print("角色不存在！")
                answer = input("是否继续删除(按q或者Q结束)：")
                if answer.lower() == 'q':
                    print("退出成功！")
                    break 
            else:
                print("角色列表为空！")
                break

    # 修改角色
    elif choice == '3':
        pass
    
    # 查询单个角色
    elif choice == '4':
        if len(all_role) != 0:
            while True:
                select_name = input("请输入查询的角色名称：")
                for role in all_role:
                    if select_name in role:
                        print("{}{}{}".format('姓名'.ljust(5),
                              '性别'.ljust(5), '职业'.ljust(5)))
                        print("{}{}{}".format(role[0].ljust(
                            5), role[1].ljust(6), role[2].ljust(5)))
                        break
                else:
                    print("角色不存在！")
                answer = input("是否继续查询(按q或者Q结束)：")
                if answer.lower() == 'q':
                    print("退出成功！")
                    break
        else:
            print("角色列表为空！")

    # 查询所有角色
    elif choice == '5':
        if len(all_role) != 0:
            print("正在查询...")
            time.sleep(1)
            print()
            print("{}{}{}".format('姓名'.ljust(5), '性别'.ljust(5), '职业'.ljust(5)))
            for role in all_role:
                print("{}{}{}".format(role[0].ljust(
                    5), role[1].ljust(6), role[2].ljust(5)))
        else:
            print("角色列表为空！")

    # 退出系统
    elif choice == '6':
        print("正在退出系统...")
        time.sleep(1)
        print("退出成功！")
        break
    
    else:
        print("输入错误，请重新输入！")
