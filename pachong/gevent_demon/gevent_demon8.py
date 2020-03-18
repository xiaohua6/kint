from greenlet import greenlet, GreenletExit

huge = []


def show_leak():
    def test1():
        gr2.switch()

    def test2():
        huge.extend([x * x for x in range(100)])

        gr1.switch()

        print('finish switch del huge')
        del huge[:]

    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()
    # gr2.switch()
    gr1 = gr2 = None
    print(gr1,gr2)
    print('length of huge is zero ? %s' % len(huge))


if __name__ == '__main__':

    show_leak()  # output： length of huge is zero ? 100