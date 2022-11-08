import time
import numpy as np
import random
import matplotlib.pyplot as plt


class MathMagic():

    def __init__(self) -> None:
        self.series = []
        self.min = 2
        self.max = 2
        self.len = 0

    def __test(self, n):
        for min in self.series:
            if n % min == 0:
                return False
        return True

    def findSeries(self, first: int, last: int):
        if first < 2:
            first = 2

        if first % 2 == 0:
            if self.__test(first):
                self.series.append(first)
                self.len += 1

            first += 1

        while (first < last):

            if self.__test(first):
                self.series.append(first)
                self.len += 1

            first += 2

        self.max = last
        return self.series

    def findPrimeFactors(self, number):

        if self.max < number:
            self.findSeries(self.max, number)

        newVal = number
        factors = []

        while (newVal > 1):

            for prime in self.series:
                if (prime > newVal):
                    break

                if newVal % prime == 0:
                    newVal /= prime
                    factors.append(prime)
                    break

        return factors

    def findAllFactorsByPrime(self, anyObj):
        if isinstance(anyObj, list):
            factors = anyObj
        elif isinstance(anyObj, int):
            factors = self.findPrimeFactors(anyObj)

        genPrime = set([1])

        for i in range(len(factors) + 1):

            for j in range(i + 1, len(factors) + 1):

                mul = 1

                for v in range(i, j):
                    mul *= factors[v]

                genPrime.add(mul)

        return list(genPrime)

    def findPrimeFactorsOptimisedSet(self, number):
        if isinstance(number, list):
            factores = number
        else:
            factores = self.findAllFactors(number)

        def checkForPrime(number):
            for i in range(2, number):
                if number % i == 0:
                    return False
            return False if number == 1 else True

        return list(filter(lambda x: checkForPrime(x), factores))

    def findAllFactors(self, number):

        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)

        return factors

    def getLen(self):
        return self.len


def printTest():

    arcs = 50
    tests = np.zeros(arcs, dtype=int)
    testNumber = 100000 * 5

    testResults1 = np.zeros(arcs, dtype=float)
    testResults2 = np.zeros(arcs, dtype=float)
    interwal = testNumber / arcs
    k = time.time_ns()
    obj = MathMagic()
    obj.findSeries(0, testNumber)
    k1 = time.time_ns()
    seriesGenTime = (k1 - k) * (10 ** -9)
    test2Time = 0

    print(testNumber, "<=", obj.getLen(), seriesGenTime)

    for i in range(arcs):

        xNumber = random.randint((i * interwal) + 1, (i + 1) * interwal)
        tests[i] = xNumber
        print(xNumber)

        # test 1
        # print("\ntest 1: find prime factors, comparing and dividing with prime")
        k = time.time_ns()
        set(obj.findAllFactorsByPrime(testNumber))
        k1 = time.time_ns()

        testResults1[i] = (k1 - k) * (10 ** -9)

        # test 2
        # print("\ntest 2: find prime factors, checking for prime from all factors set")
        k = time.time_ns()
        lis = obj.findAllFactors(testNumber)
        k1 = time.time_ns()

        testResults2[i] = (k1 - k) * (10 ** -9)

    del lis
    del obj

    avg1 = np.round(np.mean(testResults1), 5)
    plt.axes()
    plt.plot(tests, testResults1, '-.', label=f"testResults1: {avg1} sec")
    avg = np.round(np.mean(testResults2), 5)
    plt.plot(tests, testResults2, '-o', label=f"testResults2: {avg} sec")
    plt.title(
        f"find prime series gen ({seriesGenTime} sec) + gen factors vs try all factors ({np.sum(testResults2)} sec)")
    print(f"secondary avg: {(avg1 + seriesGenTime) / 2}")

    plt.legend()
    plt.show()


printTest()
