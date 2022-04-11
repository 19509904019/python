# # chr ord
#
# print(chr(65))  # Unicode码  ----> str
#
# print(ord('A'))  # str ----> Unicode码
#
# print(ord('🐉'))  # 128009
#
# print(chr(128009))  # 🐉
#
# # print()  input()  str()......


# 加密算法：md5 sha1 sha256
# base64可逆
import hashlib

msg = '阿燕一起去吃饭！'
md5 = hashlib.md5(msg.encode('utf-8'))

print(md5)
print(md5.hexdigest())  # 加密 9d2525ddd6257caf3bebfed73d0685b0

sha256 = hashlib.sha256(msg.encode("UTF-8"))
print(sha256.hexdigest())

# 用户登录
list1 = []
password = '123456'
password = hashlib.sha256(password.encode("UTF-8")).hexdigest()  # 加密
list1.append(password)

pwd = input("请输入密码：")
pwd = hashlib.sha256(pwd.encode("utf-8")).hexdigest()  # 加密
for i in list1:
    # 比对加密后的文本
    if i == pwd:
        print("登录成功！")
