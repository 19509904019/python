"""
开发模式：单例模式
使用同一个方法建立多个对象时，共用同一个地址
"""


class Singleton:
    # 私有化
    __instance = None

    # 重写__new__开辟空间
    def __new__(cls, *args, **kwargs):
        # __instnace 为空则创建地址
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        #     return cls.__instance
        # else:
        #     return cls.__instance

        # 简化
        return cls.__instance


s = Singleton()
s1 = Singleton()

print(s)
print(s1)
