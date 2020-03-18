
from greenlet import greenlet



# 当创建一个greenlet时，首先初始化一个空栈会运行在greenlet构造时传入的函数（首先在test1中打印 12）
# ， 如果在这个函数（test1）中switch到其他协程（到了test2 打印34），那么该协程会被挂起，等到切换回来
# （在test2中切换回来 打印34）。当这个协程对应函数执行完毕，那么这个协程就变成dead状态。


def test1():
    print (12)
    gr2.switch()
    print (34)

def test2():
    print (56)
    gr1.switch()


gr1 = greenlet(test1)

gr2 = greenlet(test2)
# #
gr1.switch()
# #
# gr2.switch()
