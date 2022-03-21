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
            # 判断角色是否为空
            if len(all_role) != 0:
                delete_name = input("请输入删除角色名称：")
                for role in all_role:
                    if delete_name in role:
                        answer = input("确定删除角色吗(y/n):")
                        if answer.lower() == 'y':
                            # 删除角色
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
        while True:
            if len(all_role) != 0:
                modify_name_before = input("请输入修改的角色名称：")
                for role in all_role:
                    if modify_name_before in role:
                        while True:
                            choice = input("1.名称 2.性别 3.职业 (请选择操作)：")
                            # 修改角色名称
                            if choice == '1':
                                modify_name_after = input("请输入要修改的名称：")
                                role[0] = modify_name_after
                                print("修改成功！")
                            # 修改角色性别
                            elif choice == '2':
                                modify_gender_after = input("请输入要修改的性别：")
                                role[1] = modify_gender_after
                                print("修改成功！")
                            # 修改角色职业
                            elif choice == '3':
                                modify_career_after = input("请输入要修改的职业：")
                                role[2] = modify_career_after
                                print("修改成功！")
                            else:
                                print("输入错误，请重新输入！")
                            answer = input("是否继续修改角色{}信息(按q或者Q结束)：".format(modify_name_before))
                            if answer.lower() == 'q':
                                print("退出成功！")
                                break
                        break
                else:
                    print("角色不存在！")
                answer = input("是否继续修改其他角色(按q或者Q结束)：")
                if answer.lower() == 'q':
                    print("退出成功！")
                    break
            else:
                print("角色列表为空！")
                break

    # 查询单个角色
    elif choice == '4':
        if len(all_role) != 0:
            while True:
                select_name = input("请输入查询的角色名称：")
                for role in all_role:
                    if select_name in role:
                        print("{}{}{}".format('姓名'.ljust(5),
                              '性别'.ljust(5), '职业'.ljust(5)))
                        print("{}{}{}".format(role[0].ljust(5), role[1].ljust(6), role[2].ljust(5)))
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
                print("{}{}{}".format(role[0].ljust(5), role[1].ljust(6), role[2].ljust(5)))
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
