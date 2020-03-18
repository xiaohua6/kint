import greenlet

def test_greenlet_tracing():
    def callback(event, args):
        print (event, 'from', id(args[0]), 'to', id(args[1]))

    def dummy():
        g2.switch()

    def dummyexception():
        raise Exception('excep in coroutine')

    main = greenlet.getcurrent()
    g1 = greenlet.greenlet(dummy)
    g2 = greenlet.greenlet(dummyexception)
    print ('main id %s, gr1 id %s, gr2 id %s' % (id(main), id(g1), id(g2)))
    oldtrace = greenlet.settrace(callback)
    try:
        g1.switch()
    except:
        print ('Exception')
    finally:
        greenlet.settrace(oldtrace)

test_greenlet_tracing()