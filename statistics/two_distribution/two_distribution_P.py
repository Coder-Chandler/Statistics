import math


class Distribution(object):
    def distribution_coin(self, x, n):
        """
        :param x: 抛硬币次数
        :param n: 抛硬币x次得到正面次数n
        :return: 抛硬币x次得到n次正面的概率
        """
        a = (1 / 2) ** x
        denominator = math.factorial(n) * math.factorial((x - n))
        Numerator = math.factorial(x)
        b = Numerator / denominator
        Probability = a * b
        return Probability

    def distribution_shoot(self, x, n):
        """
        :param x: 投篮次数
        :param n: 投篮x次命中次数n
        :return: 投篮x次得到n次命中的概率
        假设投篮命中率30%
        """
        a = (0.3 ** n) * ((1 - 0.3) ** (x - n))
        denominator = math.factorial(n) * math.factorial((x - n))
        Numerator = math.factorial(x)
        b = Numerator / denominator
        Probability = a * b
        return Probability


def count():
    fs = []
    for i in range(1, 4):
        def foo(i=i):
            return i

        fs.append(foo)
    return fs


f1 = count()
for i in f1:
    print(i())


def new_fn(f):
    def fn(x):
        print('call function: ' + f.__name__ + '()')
        x = x * 2
        return f(x)

    return fn

@new_fn
def bar(x):
    return x ** 2

print(bar(2))
