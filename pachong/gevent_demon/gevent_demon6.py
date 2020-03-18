
# 对于greenlet，最常用的写法是 x = gr.switch(y)。 这句话的意思是切换到gr，传入参数y。
# 当从其他协程（不一定是这个gr）切换回来的时候，将值付给x。
#  test1中的z的值及是a=gr1.switch(10)的时候传回来的参数，即10

import greenlet
def test1(x, y):
    print(id(greenlet.getcurrent()), id(greenlet.getcurrent().parent)) # 40240272 40239952
    z = gr2.switch(x+y)
    print('test1',z)
    gr2.switch(5)
    print('test1 ', x + y)

def test2(u):
    print(id(greenlet.getcurrent()), id(greenlet.getcurrent().parent))
    print ('test2 ', u)
    b=gr1.switch(u,u)
    print('test22',b)
    a=gr1.switch(10)
    print("test222",a)
    gr1.switch()

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
#
# 判断greentlete是否正常结束
print(gr1.dead,gr2.dead)

gr2.switch(110)

print(gr1.dead,gr2.dead)
gr2.switch()
print(gr1.dead,gr2.dead)



