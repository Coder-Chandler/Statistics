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
        a = (0.3**n)*((1-0.3)**(x-n))
        denominator = math.factorial(n) * math.factorial((x - n))
        Numerator = math.factorial(x)
        b = Numerator / denominator
        Probability = a * b
        return Probability



