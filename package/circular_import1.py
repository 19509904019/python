

def func():
    print("-----1-----")
    from circular_import import task1
    task1()
    print("-----2-----")
